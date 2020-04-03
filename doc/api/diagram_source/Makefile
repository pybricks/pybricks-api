
SRC_DIR = .
OUT_DIR = ../images

POSTFIX := _label
SVG := $(wildcard $(SRC_DIR)/*.svg)
DIAGRAMS := $(patsubst $(SRC_DIR)/%.svg,$(OUT_DIR)/%$(POSTFIX).png,$(SVG))
DIR := ${CURDIR}

all: $(DIAGRAMS)

clean:
	rm -f $(DIAGRAMS)

$(OUT_DIR)/%$(POSTFIX).png: $(SRC_DIR)/%.svg
	if inkscape --version | grep -q "Inkscape 0"; then \
		inkscape --file=$(DIR)/$< --export-area-drawing --export-png=$(DIR)/$@; \
	else \
		inkscape \
			--export-area-drawing \
			--export-background=white \
			--export-background-opacity=1.0 \
			--export-file=$(DIR)/$@ \
			$(DIR)/$<; \
	fi
