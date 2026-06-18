.PHONY: validate

validate:
	python3 tools/validate_manifests.py
	python3 tools/validate_python_assets.py
