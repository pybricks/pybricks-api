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

exec(open(os.path.abspath("../common/conf.py")).read())
