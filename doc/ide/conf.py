#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pybricks documentation build configuration file
#
import os

# General information about the project.
project = 'pybricks'
copyright = '2018-2021 The Pybricks Authors'
author = ''

_TITLE = 'Pybricks Modules and Examples'
_DISCLAIMER = ''

html_favicon = '../common/images/favicon.ico'
html_logo = '../common/images/pybricks-logo-rtd.png'
html_show_copyright = False
html_show_sphinx = False
html_css_files = ['css/ide.css']
html_js_files = ['js/ide.js']

imgmath_image_format = 'svg'
imgmath_use_preview = True  # requires Sphinx v3
imgmath_latex_preamble = r'''
\usepackage{newtxsf}
'''

exec(open(os.path.abspath("../common/conf.py")).read())

extensions.remove('sphinx.ext.mathjax')  # noqa F821
extensions.append('sphinx.ext.imgmath')  # noqa F821
html_theme_options['prev_next_buttons_location'] = None  # noqa F821
