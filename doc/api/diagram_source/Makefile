
SRC_DIR = .
OUT_DIR = ../images

POSTFIX := _label
SVG := $(wildcard $(SRC_DIR)/*.svg)
PNG := $(patsubst $(SRC_DIR)/%.svg,$(OUT_DIR)/%$(POSTFIX).png,$(SVG))
DIR := ${CURDIR}

all: $(PNG)

clean:
	rm -f $(PNG)

$(OUT_DIR)/%$(POSTFIX).png: $(SRC_DIR)/%.svg
	inkscape --file=$(DIR)/$< --export-area-drawing --export-png=$(DIR)/$@
