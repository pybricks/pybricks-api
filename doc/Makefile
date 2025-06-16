# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = -W
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Pybricks
SOURCEDIR     = main
BUILDDIR      = "$(SOURCEDIR)"/build
TAG           = main
LOCALEDIR     = locales

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(TAG) $(O)

.PHONY: help Makefile

diagrams:
	@$(MAKE) -C "$(SOURCEDIR)"/diagrams_source clean
	@$(MAKE) -C "$(SOURCEDIR)"/diagrams_source

# i18n targets
gettext:
	@$(SPHINXBUILD) -b gettext "$(SOURCEDIR)" "$(LOCALEDIR)/pot" -D gettext_compact=0 $(SPHINXOPTS) -t $(TAG) $(O)

update-po-%:
	@sphinx-intl update -p "$(LOCALEDIR)/pot" -l $*

html-%:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/$*" $(SPHINXOPTS) -t $(TAG) -D language=$* $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) -t $(TAG) $(O)

.PHONY: gettext update-po-% html-%
