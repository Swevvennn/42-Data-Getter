install:
	python3 -m venv /tmp/venv
	ln -s /tmp/venv .venv
	UV_CACHE_DIR=/tpm/uv_cache\
	uv sync
	cp .env.exemple .env
	touch .cache/data.json
	echo "{}" > .cache/data.json
	clear
	@echo "Setup finished !!!"

run:
	uv run python3 -m src

level:
	uv run python3 -m src level

logtime:
	uv run python3 -m src logtime

ratio:
	uv run python3 -m src ratio

table:
	uv run python3 -m src table

clean:
	rm -rf .venv /tmp/venv /tmp/uv_cache src/__pycache__

fclean: clean
	rm -f .cache/data.json .env