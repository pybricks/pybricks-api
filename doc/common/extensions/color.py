from docutils import nodes
from docutils.parsers.rst import Directive
from pybricks.parameters import Color
from colorsys import hsv_to_rgb


class PybricksColorDirective(Directive):

    required_arguments = 1

    def run(self):
        # Get color name from sphinx-directive
        name = self.arguments[0]

        # Get Color class attribute
        color = getattr(Color, name)

        # Convert HSV to RGB
        r, g, b = hsv_to_rgb(color.h / 360, color.s / 100, color.v / 100)

        # Convert RGB to HEX
        rgbhex = "#{0:02x}{1:02x}{2:02x}".format(
            round(r * 255), round(g * 255), round(b * 255)
        )

        # Render a small block of the given color
        css = "background-color: {0}; color: {0}; width: 50px;".format(rgbhex)

        if name == "WHITE":
            css += (
                "border-style: solid; border-width: 0.5px;" + "border-color: #666666;"
            )

        html = '<div id="test" style="{0}">_</div>'.format(css)

        # Return the node
        node = nodes.raw("", html, format="html")
        return [node]


def setup(app):
    app.add_directive_to_domain("py", "pybricks-color", PybricksColorDirective)
