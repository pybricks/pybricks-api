from docutils.parsers.rst import Directive
from docutils import nodes
from pathlib import Path

SPHINX_IMAGE_PATH = "blockimg"


def get_svg_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Global variable to store the app object
app = None


class BlockImageDirective(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0

    def run(self):
        # Adjust the image path
        file_name = self.arguments[0] + ".svg"
        file_path = Path(app.srcdir) / SPHINX_IMAGE_PATH / file_name

        # Read the SVG content
        svg_content = get_svg_content(file_path)

        # Create a raw HTML node with the SVG content
        raw_html = f'<div class="svg-container">{svg_content}</div>'
        raw_node = nodes.raw("", raw_html, format="html")

        return [raw_node]


def setup(apparg):
    global app
    app = apparg
    app.add_directive("blockimg", BlockImageDirective)
