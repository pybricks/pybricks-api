"""This directive hides the builtin directives
    * versionchanged
    * versionadded
    * deprecated
when building documentation with the 'ide' tag.
"""

from docutils import nodes
from docutils.parsers.rst import Directive


class PybricksVersionDirective(Directive):
    has_content = True

    def run(self):
        html = ""
        node = nodes.raw("", html, format="html")
        return [node]


def setup(app):
    if app.tags.has("ide"):
        app.add_directive_to_domain(
            "py", "deprecated", PybricksVersionDirective, override=True
        )
        app.add_directive_to_domain(
            "py", "versionadded", PybricksVersionDirective, override=True
        )
        app.add_directive_to_domain(
            "py", "versionchanged", PybricksVersionDirective, override=True
        )
