PROJECT ?=
SLUG ?=

.PHONY: init check-docs check-repo check-skill check-gallery ci release-package new-history new-plan

init:
	@if [ -z "$(PROJECT)" ]; then echo "usage: make init PROJECT=my-project"; exit 1; fi
	./scripts/init-project.sh "$(PROJECT)"

check-docs:
	./scripts/check-docs.sh

check-repo:
	./scripts/check-docs.sh
	./scripts/check-repo-hygiene.sh

check-skill:
	python3 skills/visual-html-gen-ui/scripts/validate_skill.py

check-gallery:
	python3 scripts/validate-gallery.py

ci:
	./scripts/ci.sh

release-package:
	./scripts/release-package.sh

new-history:
	@if [ -z "$(SLUG)" ]; then echo "usage: make new-history SLUG=my-change"; exit 1; fi
	./scripts/new-history.sh "$(SLUG)"

new-plan:
	@if [ -z "$(SLUG)" ]; then echo "usage: make new-plan SLUG=my-plan"; exit 1; fi
	./scripts/new-exec-plan.sh "$(SLUG)"
