# MIT License

# Copyright (c) 2017 Robert, https://github.com/ulrobix/sphinxcontrib-requirements

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
from docutils.parsers.rst import Directive, directives
from docutils import nodes
from docutils.statemachine import StringList
from sphinx.util.osutil import copyfile
from sphinx.util import logging


CSS_FILE = "requirements.css"
JS_FILE = "requirements.js"


class PybricksRequirementsDirective(Directive):
    has_content = True
    option_spec = {"header": directives.unchanged}

    required_arguments = 0
    optional_arguments = 10

    def run(self):
        node = nodes.container()
        node["classes"].append("toggle-content")

        par = nodes.container()
        par["classes"].append("toggle-header")

        content = ".. pybricks-requirements-static:: " + " ".join(self.arguments)

        self.state.nested_parse(StringList([content]), self.content_offset, node)

        return [par, node]


def add_assets(app):
    app.add_css_file(CSS_FILE)
    app.add_js_file(JS_FILE)


def copy_assets(app, exception):
    if app.builder.name not in ["html", "readthedocs"] or exception:
        return
    logger = logging.getLogger(__name__)
    logger.info("Copying requirements stylesheet/javascript... ", nonl=True)
    dest = os.path.join(app.builder.outdir, "_static", CSS_FILE)
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)), CSS_FILE)
    copyfile(source, dest)
    dest = os.path.join(app.builder.outdir, "_static", JS_FILE)
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)), JS_FILE)
    copyfile(source, dest)
    logger.info("done")


def setup(app):
    app.add_directive("pybricks-requirements", PybricksRequirementsDirective)
    app.connect("builder-inited", add_assets)
    app.connect("build-finished", copy_assets)
