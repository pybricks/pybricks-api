import xml.etree.ElementTree as ET

from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.images import Image
from docutils.nodes import image, paragraph
from pathlib import Path

SPHINX_IMAGE_PATH = "blockimg"

SVG_SCALE = 0.9


def get_svg_size(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    width = root.attrib.get("width")
    height = root.attrib.get("height")

    return float(width), float(height)


# Global variable to store the app object
app = None


class BlockImageDirective(Image):
    option_spec = Image.option_spec.copy()
    option_spec["stack"] = directives.flag

    def run(self):
        # Adjust the image path
        file_name = self.arguments[0] + ".svg"
        self.arguments[0] = "/" + SPHINX_IMAGE_PATH + "/" + file_name
        path = Path(app.srcdir) / SPHINX_IMAGE_PATH / file_name

        # Set it to the scaled SVG size unless width explicitly set.
        if self.options.get("width") is None:
            width, height = get_svg_size(path)
            self.options["width"] = str(round(width * SVG_SCALE)) + "px"
            self.options["height"] = str(round(height * SVG_SCALE)) + "px"

        # Call the parent class's run method
        nodes = super().run()

        # Wrap each image node in a paragraph node
        for i, node in enumerate(nodes):
            if isinstance(node, image):
                if "stack" not in self.options:
                    node["classes"].append("block-image")
                nodes[i] = paragraph("", "", node)

        return nodes


def setup(apparg):
    global app
    app = apparg
    app.add_directive("blockimg", BlockImageDirective)
