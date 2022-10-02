
SRC_DIR = .
OUT_DIR = ../diagrams
SVG := $(wildcard $(SRC_DIR)/*.svg)
DIAGRAMS := $(patsubst $(SRC_DIR)/%.svg,$(OUT_DIR)/%$(POSTFIX).png,$(SVG))
DIR := ${CURDIR}

all: $(DIAGRAMS)

clean:
	rm -f $(DIAGRAMS)

$(OUT_DIR)/%.png: $(SRC_DIR)/%.svg
	inkscape \
		--export-area-page \
		--export-background=none \
		--export-background-opacity=0.0 \
		--export-filename=$(DIR)/$@ \
		$(DIR)/$<; \
