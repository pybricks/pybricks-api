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

exec(open(os.path.abspath("../common/conf.py")).read())
