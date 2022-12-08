# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -W
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Pybricks
SOURCEDIR     = main
BUILDDIR      = "$(SOURCEDIR)"/build
TAG           = main

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(TAG) $(O)

.PHONY: help Makefile

diagrams:
	@$(MAKE) -C "$(SOURCEDIR)"/diagrams_source clean
	@$(MAKE) -C "$(SOURCEDIR)"/diagrams_source

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) -t $(TAG) $(O)
