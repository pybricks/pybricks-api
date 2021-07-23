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
_DISCLAIMER = 'LEGO, the LEGO logo, MINDSTORMS and the MINDSTORMS EV3 logo are\
               trademarks and/or copyrights of the LEGO Group of companies \
               which does not sponsor, authorize or endorse this site.'

html_favicon = '../common/images/favicon.ico'
html_logo = '../common/images/pybricks-logo-rtd.png'
latex_logo = '../common/images/pybricks-logo-large.png'

# Build main docs for RTD by default.
# Since tags cannot be passed via SPHINXOPTS on read the docs, add it manually.
if os.environ.get('READTHEDOCS', None) == 'True':
    tags.add('main')  # noqa F821


# Addtional configuration of the IDE docs
if 'ide' in tags.tags:  # noqa F821
    _DISCLAIMER = ''
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

# Addtional configuration of the IDE docs
if 'ide' in tags.tags:  # noqa F821

    extensions.remove('sphinx.ext.mathjax')  # noqa F821
    extensions.append('sphinx.ext.imgmath')  # noqa F821
    html_theme_options['prev_next_buttons_location'] = None  # noqa F821
