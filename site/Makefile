# Makefile — build and deploy mesabo.github.io
# Usage:
#   make           # build all pages into build/
#   make serve     # local preview at http://localhost:8000
#   make clean     # remove build/
#   make deploy    # push build/ to mesabo/mesabo.github.io (force, main branch)

JEMDOC := python3 tools/jemdoc
CONF   := mysite.conf
PAGES  := index publications research experiences awards other fr ja
BUILD  := build
HTMLS  := $(addprefix $(BUILD)/,$(addsuffix .html,$(PAGES)))

REMOTE := https://github.com/mesabo/mesabo.github.io.git

.PHONY: all build serve clean deploy

all: build

build: gallery $(BUILD) $(HTMLS) $(BUILD)/mysite.css $(BUILD)/jemdoc-default.css $(BUILD)/assets $(BUILD)/README.md

$(BUILD)/README.md: deploy_README.md
	cp deploy_README.md $(BUILD)/README.md

# regenerate the photo gallery in other.jemdoc from assets/photos/*
.PHONY: gallery
gallery:
	@python3 tools/gen_gallery.py

$(BUILD):
	mkdir -p $(BUILD)

$(BUILD)/%.html: %.jemdoc MENU $(CONF)
	@mkdir -p $(BUILD)
	$(JEMDOC) -c $(CONF) -o $@ $<
	@# fix jemdoc smart-quote bug on target attribute
	@sed -i '' 's/target=&ldquo;blank&rdquo;/target="_blank" rel="noopener"/g' $@
	@sed -i '' 's/target="blank"/target="_blank" rel="noopener"/g' $@

$(BUILD)/mysite.css: mysite.css
	cp mysite.css $(BUILD)/

$(BUILD)/jemdoc-default.css: tools/jemdoc-default.css
	cp tools/jemdoc-default.css $(BUILD)/

$(BUILD)/assets: assets
	rm -rf $(BUILD)/assets
	cp -R assets $(BUILD)/
	@# render every PDF in papers/ and awards/ to a same-name PNG thumbnail in build/ (96 DPI)
	@for dir in papers awards; do \
	  for pdf in $(BUILD)/assets/$$dir/*.pdf; do \
	    [ -f "$$pdf" ] || continue; \
	    out=$${pdf%.pdf}; \
	    pdftoppm -png -r 96 -singlefile "$$pdf" "$$out"; \
	  done; \
	done
	@echo "rendered $$(find $(BUILD)/assets/papers $(BUILD)/assets/awards -name '*.png' 2>/dev/null | wc -l | tr -d ' ') PDF thumbnails"

serve: build
	cd $(BUILD) && python3 -m http.server 8000

clean:
	rm -rf $(BUILD)

deploy: build
	@echo "Deploying $(BUILD)/ to $(REMOTE) main branch (force-push)..."
	cd $(BUILD) && \
	  rm -rf .git && \
	  git init -b main && \
	  git add -A && \
	  git -c user.name="$$(git config user.name)" -c user.email="$$(git config user.email)" commit -m "deploy" && \
	  git remote add origin $(REMOTE) && \
	  git push -f origin main
	@echo "Done. Site live at https://mesabo.github.io within ~1 minute."
