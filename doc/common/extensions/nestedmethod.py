"""Provides the ``autonestedmethod`` directive.

Like ``automethod``, but resolves dotted names such as ``control.limits``
relative to the class documented by the enclosing ``autoclass`` directive.
Plain ``automethod`` treats everything before the last dot as a module/class
path, so ``control.limits`` would be looked up as an attribute of the current
*module* instead of the current class. Resolving the class here keeps shared
include fragments module-neutral.
"""

from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

logger = logging.getLogger(__name__)


class AutoNestedMethodDirective(SphinxDirective):
    required_arguments = 1
    has_content = False

    def run(self):
        current = self.env.current_document
        module = current.autodoc_module or self.env.ref_context.get("py:module")
        cls = current.autodoc_class or self.env.ref_context.get("py:class")

        if not module or not cls:
            logger.warning(
                "autonestedmethod:: %s used outside of an autoclass context",
                self.arguments[0],
                location=self.get_location(),
            )
            return []

        return self.parse_text_to_nodes(
            f".. automethod:: {module}::{cls}.{self.arguments[0]}"
        )


def setup(app):
    app.add_directive("autonestedmethod", AutoNestedMethodDirective)
    return {"parallel_read_safe": True}
