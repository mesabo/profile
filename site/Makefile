# Makefile — build and deploy mesabo.github.io
# Usage:
#   make           # build all pages into build/
#   make serve     # local preview at http://localhost:8000
#   make clean     # remove build/
#   make deploy    # push build/ to mesabo/mesabo.github.io (force, main branch)

JEMDOC := python3 tools/jemdoc
CONF   := mysite.conf
PAGES  := index publications research experiences awards other
BUILD  := build

EN_HTMLS := $(addprefix $(BUILD)/,$(addsuffix .html,$(PAGES)))
FR_HTMLS := $(addprefix $(BUILD)/fr/,$(addsuffix .html,$(PAGES)))
JA_HTMLS := $(addprefix $(BUILD)/ja/,$(addsuffix .html,$(PAGES)))
HTMLS    := $(EN_HTMLS) $(FR_HTMLS) $(JA_HTMLS)

REMOTE := https://github.com/mesabo/mesabo.github.io.git

.PHONY: all build serve clean deploy gallery

all: build

build: gallery $(BUILD) $(HTMLS) $(BUILD)/404.html $(BUILD)/mysite.css $(BUILD)/jemdoc-default.css $(BUILD)/assets $(BUILD)/README.md $(BUILD)/robots.txt $(BUILD)/sitemap.xml inject-date

$(BUILD)/README.md: deploy_README.md
	cp deploy_README.md $(BUILD)/README.md

$(BUILD)/robots.txt: robots.txt
	cp robots.txt $(BUILD)/robots.txt

$(BUILD)/sitemap.xml:
	@mkdir -p $(BUILD)
	@echo '<?xml version="1.0" encoding="UTF-8"?>' > $(BUILD)/sitemap.xml
	@echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' >> $(BUILD)/sitemap.xml
	@today=$$(date -u +%Y-%m-%d); \
	for path in '' fr/ ja/; do \
	  for page in index publications research experiences awards other; do \
	    echo "  <url><loc>https://mesabo.github.io/$${path}$${page}.html</loc><lastmod>$${today}</lastmod></url>" >> $(BUILD)/sitemap.xml; \
	  done; \
	done
	@echo '</urlset>' >> $(BUILD)/sitemap.xml

# Build the 404 page (no menu, sits at root, served by GitHub Pages on any miss)
$(BUILD)/404.html: 404.jemdoc $(CONF)
	@mkdir -p $(BUILD)
	$(JEMDOC) -c $(CONF) -o $@ $<

# Replace the __BUILD_DATE__ placeholder in every built HTML page with today's YYYY-MM
.PHONY: inject-date
inject-date:
	@d=$$(date -u +"%Y-%m"); \
	find $(BUILD) -name '*.html' -exec sed -i '' "s/__BUILD_DATE__/$$d/g" {} \;

gallery:
	@python3 tools/gen_gallery.py

$(BUILD):
	mkdir -p $(BUILD)

# === English (root) — static pattern rule ===
$(EN_HTMLS): $(BUILD)/%.html: %.jemdoc MENU $(CONF)
	@mkdir -p $(BUILD)
	$(JEMDOC) -c $(CONF) -o $@ $<
	@sed -i '' -e 's/target=&ldquo;blank&rdquo;/target="_blank" rel="noopener"/g' \
	           -e 's/target="blank"/target="_blank" rel="noopener"/g' \
	           -e 's|<a href="\(\.\./[^"]*\)" class="current">|<a href="\1">|g' $@

# === French (build/fr/) ===
$(FR_HTMLS): $(BUILD)/fr/%.html: fr/%.jemdoc fr/MENU $(CONF)
	@mkdir -p $(BUILD)/fr
	cd fr && python3 ../tools/jemdoc -c ../$(CONF) -o ../$@ $*.jemdoc
	@sed -i '' -e 's/target=&ldquo;blank&rdquo;/target="_blank" rel="noopener"/g' \
	           -e 's/target="blank"/target="_blank" rel="noopener"/g' \
	           -e 's|<a href="\(\.\./[^"]*\)" class="current">|<a href="\1">|g' $@

# === Japanese (build/ja/) ===
$(JA_HTMLS): $(BUILD)/ja/%.html: ja/%.jemdoc ja/MENU $(CONF)
	@mkdir -p $(BUILD)/ja
	cd ja && python3 ../tools/jemdoc -c ../$(CONF) -o ../$@ $*.jemdoc
	@sed -i '' -e 's/target=&ldquo;blank&rdquo;/target="_blank" rel="noopener"/g' \
	           -e 's/target="blank"/target="_blank" rel="noopener"/g' \
	           -e 's|<a href="\(\.\./[^"]*\)" class="current">|<a href="\1">|g' $@

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
