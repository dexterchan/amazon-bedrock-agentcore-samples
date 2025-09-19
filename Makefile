.PHONY: init

init:
	uv venv -p python3.12 .venv
	source .venv/bin/activate && uv pip install -r requirements.txt