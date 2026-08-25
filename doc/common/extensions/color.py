from colorsys import hsv_to_rgb

from docutils import nodes
from docutils.parsers.rst import Directive

from pybricks.parameters import Color


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
        rgbhex = f"#{round(r * 255):02x}{round(g * 255):02x}{round(b * 255):02x}"

        # Render a small block of the given color
        css = f"background-color: {rgbhex}; color: {rgbhex}; width: 50px;"

        if name == "WHITE":
            css += (
                "border-style: solid; border-width: 0.5px;" + "border-color: #666666;"
            )

        html = f'<div id="test" style="{css}">_</div>'

        # Return the node
        node = nodes.raw("", html, format="html")
        return [node]


def setup(app):
    app.add_directive_to_domain("py", "pybricks-color", PybricksColorDirective)
