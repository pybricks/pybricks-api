#
# Pybricks documentation build configuration file
#
import os
import sys

# General information about the project.
project = "pybricks"
copyright = "2018-2026 The Pybricks Authors"
author = ""

_DISCLAIMER = "LEGO, the LEGO logo, MINDSTORMS and the MINDSTORMS EV3 logo are\
               trademarks and/or copyrights of the LEGO Group of companies \
               which does not sponsor, authorize or endorse this site."

html_favicon = "../common/images/favicon.ico"
html_logo = "../common/images/pybricks-logo-rtd.png"

# Build main docs for RTD by default.
# Since tags cannot be passed via the TAG make variable on read the docs,
# add it manually.
if os.environ.get("READTHEDOCS", None) == "True":
    tags.add("main")  # noqa F821

# HACK: this allows Number type alias to be imported by Sphinx
os.environ["SPHINX_BUILD"] = "True"

html_css_files = ["css/theme_overrides.css", "css/blocks.css"]

# Additional configuration of the IDE docs
if tags.has("ide"):  # noqa F821
    _DISCLAIMER = ""
    html_show_copyright = False
    html_show_sphinx = False
    html_css_files.append("css/ide.css")
    html_js_files = ["js/ide.js"]

# Shared config must run in this namespace so it sees the globals above.
with open(os.path.abspath("../common/conf.py")) as _f:
    exec(_f.read())  # noqa: S102

# Build hub specific example scripts.
sys.path.append(os.path.abspath("../../examples/pup/hub_common"))
import make_examples  # noqa F401, E402
