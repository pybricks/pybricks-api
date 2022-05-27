from docutils import nodes
from docutils.parsers.rst import Directive


class PybricksClasslinkDirective(Directive):

    required_arguments = 1
    optional_arguments = 1

    def run(self):
        # Get link and name from sphinx-directive
        name = self.arguments[0]
        link = name if len(self.arguments) == 1 else self.arguments[1]

        html = (
            '<a href="{0}.html">'.format(link.lower())
            + '<dl class="py class">'
            + "<dt>"
            + '<em class="property">class </em>'
            + '<code class="sig-name descname">'
            + name
            + "</code>"
            + "</dt>"
            + "<dd></dd>"
            + "</dl>"
            + "</a>"
        )

        # Return the node
        node = nodes.raw("", html, format="html")
        return [node]


def setup(app):
    app.add_directive_to_domain("py", "pybricks-classlink", PybricksClasslinkDirective)
