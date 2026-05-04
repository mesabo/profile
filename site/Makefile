# Makefile — build and deploy mesabo.github.io
# Usage:
#   make           # build all pages into build/
#   make serve     # local preview at http://localhost:8000
#   make clean     # remove build/
#   make deploy    # push build/ to mesabo/mesabo.github.io (force, main branch)

JEMDOC := python3 tools/jemdoc
CONF   := mysite.conf
PAGES  := index publications research experiences skills awards other
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

# Replace the __BUILD_DATE__ placeholder + inject per-page hreflang tags + cache-bust CSS.
.PHONY: inject-date
inject-date:
	@d=$$(date -u +"%Y-%m"); \
	v=$$(date -u +"%Y%m%d%H%M"); \
	find $(BUILD) -name '*.html' -exec sed -i '' "s/__BUILD_DATE__/$$d/g" {} \; ; \
	find $(BUILD) -name '*.html' -exec sed -i '' "s|/mysite.css\"|/mysite.css?v=$$v\"|g" {} \; ; \
	find $(BUILD) -name '*.html' -exec sed -i '' "s|/assets/photo.png\"|/assets/photo.png?v=$$v\"|g" {} \;
	@# inject per-page hreflang tags (only for pages that have all 3 language versions)
	@for page in index publications research experiences skills awards other; do \
	  for f in $(BUILD)/$$page.html $(BUILD)/fr/$$page.html $(BUILD)/ja/$$page.html; do \
	    [ -f "$$f" ] || continue; \
	    sed -i '' "s|<!--HREFLANG-->|<link rel=\"alternate\" hreflang=\"en\" href=\"https://mesabo.github.io/$$page.html\" />\\$$(printf '\n')<link rel=\"alternate\" hreflang=\"fr\" href=\"https://mesabo.github.io/fr/$$page.html\" />\\$$(printf '\n')<link rel=\"alternate\" hreflang=\"ja\" href=\"https://mesabo.github.io/ja/$$page.html\" />\\$$(printf '\n')<link rel=\"alternate\" hreflang=\"x-default\" href=\"https://mesabo.github.io/$$page.html\" />|" "$$f"; \
	  done; \
	done
	@# strip stray <!--HREFLANG--> from any other pages (404 etc.)
	@find $(BUILD) -name '*.html' -exec sed -i '' 's|<!--HREFLANG-->||g' {} \;

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
	@# Strip target="_blank" from internal .html links (jemdoc adds it to body links incorrectly)
	@sed -i '' -E -e 's|<a href="([^"]+\.html)" target="_blank" rel="noopener">|<a href="\1">|g' $@

# === French (build/fr/) ===
$(FR_HTMLS): $(BUILD)/fr/%.html: fr/%.jemdoc fr/MENU $(CONF)
	@mkdir -p $(BUILD)/fr
	cd fr && python3 ../tools/jemdoc -c ../$(CONF) -o ../$@ $*.jemdoc
	@sed -i '' -e 's/target=&ldquo;blank&rdquo;/target="_blank" rel="noopener"/g' \
	           -e 's/target="blank"/target="_blank" rel="noopener"/g' \
	           -e 's|<a href="\(\.\./[^"]*\)" class="current">|<a href="\1">|g' $@
	@# Strip target="_blank" from internal .html links (jemdoc adds it to body links incorrectly)
	@sed -i '' -E -e 's|<a href="([^"]+\.html)" target="_blank" rel="noopener">|<a href="\1">|g' $@

# === Japanese (build/ja/) ===
$(JA_HTMLS): $(BUILD)/ja/%.html: ja/%.jemdoc ja/MENU $(CONF)
	@mkdir -p $(BUILD)/ja
	cd ja && python3 ../tools/jemdoc -c ../$(CONF) -o ../$@ $*.jemdoc
	@sed -i '' -e 's/target=&ldquo;blank&rdquo;/target="_blank" rel="noopener"/g' \
	           -e 's/target="blank"/target="_blank" rel="noopener"/g' \
	           -e 's|<a href="\(\.\./[^"]*\)" class="current">|<a href="\1">|g' $@
	@# Strip target="_blank" from internal .html links (jemdoc adds it to body links incorrectly)
	@sed -i '' -E -e 's|<a href="([^"]+\.html)" target="_blank" rel="noopener">|<a href="\1">|g' $@

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

DEPLOY_DIR := .deploy

# Deploy: tag the current state as a rollback point, then commit + push the new build.
# History is preserved on every deploy AND every previous deploy is tagged for one-line rollback.
deploy: build
	@echo "Deploying $(BUILD)/ to $(REMOTE) main branch..."
	@if [ ! -d $(DEPLOY_DIR)/.git ]; then \
	  rm -rf $(DEPLOY_DIR); \
	  git clone $(REMOTE) $(DEPLOY_DIR); \
	fi
	@cd $(DEPLOY_DIR) && git fetch origin --tags && git checkout main && git reset --hard origin/main
	@# 1) Tag the current state as a rollback point BEFORE we change anything
	@cd $(DEPLOY_DIR) && tag="rollback-$$(date -u +%Y%m%d-%H%M%S)" && \
	  git tag -a "$$tag" -m "rollback point before deploy at $$(date -u +'%Y-%m-%d %H:%M UTC')" && \
	  git push origin "$$tag" && \
	  echo "  rollback tag pushed: $$tag"
	@# 2) Sync new build/ into the clone, deleting any files no longer present
	rsync -a --delete --exclude='.git' $(BUILD)/ $(DEPLOY_DIR)/
	@cd $(DEPLOY_DIR) && \
	  git add -A && \
	  if git diff --cached --quiet; then \
	    echo "  no changes — skipping commit."; \
	  else \
	    git commit -m "deploy: $$(date -u +'%Y-%m-%d %H:%M UTC')" && \
	    git push origin main; \
	  fi
	@echo "Done. Site live at https://mesabo.github.io within ~1 minute."
	@echo "Rollback any time with: make rollback           (revert last deploy)"
	@echo "Or to a specific tag:   make rollback-to TAG=rollback-YYYYMMDD-HHMMSS"

# Roll back the deploy by reverting the last commit (one-click undo)
.PHONY: rollback
rollback:
	@echo "Rolling back the last deploy on $(REMOTE)..."
	@if [ ! -d $(DEPLOY_DIR)/.git ]; then \
	  rm -rf $(DEPLOY_DIR); \
	  git clone $(REMOTE) $(DEPLOY_DIR); \
	fi
	@cd $(DEPLOY_DIR) && git fetch origin && git checkout main && git reset --hard origin/main && \
	  git revert --no-edit HEAD && \
	  git push origin main
	@echo "Rolled back. Previous version live at https://mesabo.github.io within ~1 minute."

# Roll back to a specific rollback tag — usage: make rollback-to TAG=rollback-YYYYMMDD-HHMMSS
.PHONY: rollback-to
rollback-to:
	@if [ -z "$(TAG)" ]; then echo "Usage: make rollback-to TAG=rollback-YYYYMMDD-HHMMSS"; exit 1; fi
	@if [ ! -d $(DEPLOY_DIR)/.git ]; then \
	  rm -rf $(DEPLOY_DIR); \
	  git clone $(REMOTE) $(DEPLOY_DIR); \
	fi
	@cd $(DEPLOY_DIR) && git fetch origin --tags && git checkout main && \
	  git reset --hard "$(TAG)" && \
	  git push --force-with-lease origin main
	@echo "Rolled back to $(TAG). Site live within ~1 minute."

# Show available rollback tags (newest first)
.PHONY: rollback-list
rollback-list:
	@if [ ! -d $(DEPLOY_DIR)/.git ]; then git clone $(REMOTE) $(DEPLOY_DIR); fi
	@cd $(DEPLOY_DIR) && git fetch origin --tags >/dev/null 2>&1 && \
	  git tag -l 'rollback-*' --sort=-creatordate | head -20

# History of the deploy repo (each commit = one deploy)
.PHONY: log
log:
	@if [ ! -d $(DEPLOY_DIR)/.git ]; then git clone $(REMOTE) $(DEPLOY_DIR); fi
	@cd $(DEPLOY_DIR) && git fetch origin >/dev/null && git log --oneline origin/main -20
