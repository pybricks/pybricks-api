"""
Sphinx extension for including code files with translated comments.
"""
import os
from pathlib import Path
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.directives.code import LiteralInclude, container_wrapper
from sphinx.util import logging as sphinx_logging
from sphinx.util.nodes import set_source_info

logger = sphinx_logging.getLogger(__name__)

class TranslatedNode(nodes.literal_block):
    """Custom node that can be pickled."""
    def astext(self):
        return self.rawsource

class TranslatedLiteralInclude(LiteralInclude):
    """A LiteralInclude directive that supports translated comments."""
    
    option_spec = LiteralInclude.option_spec.copy()
    option_spec['language'] = directives.unchanged

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.translations = {}

    def load_translations(self, source_file: Path, language: str) -> dict:
        """Load translations for the given file and language.
        
        Args:
            source_file: Path to the source file
            language: Target language code
            
        Returns:
            Dictionary of original comments to translated comments
        """
        try:
            project_root = Path(__file__).parent.parent.parent
            rel_path = Path(source_file).relative_to(project_root)
            
            # Get path relative to examples directory
            try:
                examples_index = rel_path.parts.index('examples')
                rel_to_examples = Path(*rel_path.parts[examples_index + 1:])
            except ValueError:
                logger.error(f"Source file not in examples directory: {rel_path}")
                return {}
            
            trans_path = project_root / 'examples' / 'translations' / language / f"{rel_to_examples}.comments"
            
            if not trans_path.exists():
                logger.warning(f"No translation file found at: {trans_path}")
                return {}
                
            translations = {}
            for line in trans_path.read_text(encoding='utf-8').splitlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        orig, trans = line.split('=', 1)
                        translations[orig.strip()] = trans.strip()
                    except ValueError:
                        logger.warning(f"Invalid translation line: {line}")
            
            logger.info(f"Loaded {len(translations)} translations")
            return translations
            
        except Exception as e:
            logger.error(f"Error loading translations: {e}")
            return {}

    def translate_content(self, content: str, language: str) -> str:
        """Translate comments in the content using loaded translations."""
        if not language or language == 'en':
            return content
            
        result = []
        translations_used = 0
        
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith('#'):
                comment_text = stripped[1:].strip()
                if comment_text in self.translations:
                    indent = line[:len(line) - len(stripped)]
                    result.append(f"{indent}# {self.translations[comment_text]}")
                    translations_used += 1
                else:
                    result.append(line)
            else:
                result.append(line)
        
        logger.info(f"Applied {translations_used} translations")
        return '\n'.join(result)

    def run(self):
        env = self.state.document.settings.env
        language = (getattr(env.config, 'language', None) or 'en')[:2].lower()
        
        # Get absolute path of source file
        source_file = Path(env.srcdir) / self.arguments[0]
        if '..' in str(source_file):
            project_root = Path(__file__).parent.parent.parent
            parts = Path(self.arguments[0]).parts
            up_count = sum(1 for part in parts if part == '..')
            source_file = project_root.joinpath(*parts[up_count:])
        
        source_file = source_file.resolve()
        logger.info(f"Processing file: {source_file}")
        
        # Load translations for non-English languages
        if language != 'en':
            self.translations = self.load_translations(source_file, language)
        
        # Get original content and process nodes
        document = super().run()
        if not self.translations:
            return document
            
        result = []
        for node in document:
            if not isinstance(node, nodes.literal_block):
                result.append(node)
                continue
                
            translated_content = self.translate_content(node.rawsource, language)
            new_node = TranslatedNode(
                translated_content,
                translated_content,
                source=node.source,
                line=node.line
            )
            
            # Copy node attributes
            new_node['language'] = node.get('language', 'python')
            new_node['highlight_args'] = node.get('highlight_args', {})
            new_node['linenos'] = node.get('linenos', False)
            new_node['classes'] = node.get('classes', [])
            
            if 'caption' in node:
                new_node['caption'] = node['caption']
            
            set_source_info(self, new_node)
            
            # Apply container wrapper if needed
            caption = node.get('caption', '') or self.options.get('caption', '')
            if caption or node.get('linenos', False):
                new_node = container_wrapper(self, new_node, caption)
            
            result.append(new_node)
            
        return result

def setup(app):
    app.add_directive('translated-literalinclude', TranslatedLiteralInclude)
    app.add_node(TranslatedNode)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
