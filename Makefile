VERSION := 1.0.0

OPENAPI_GENERATOR_CLI_VERSION := v7.13.0

out/python-asyncio/dist/asana_asyncio-${VERSION}-py3-none-any.whl: out/python-asyncio/setup.py
	cd out/python-asyncio; \
	docker run --rm \
	--user $$(id -u):$$(id -g) \
	-w /code \
	-v $$(pwd):/code \
	-e HOME=/code \
	python:3-slim \
	bash -c "pip3 install --user 'poetry<2' && ~/.local/bin/poetry build"

out/python-asyncio/setup.py: asana_oas.yaml
	docker run --rm \
	--user $$(id -u):$$(id -g) \
	-v ${PWD}:/local openapitools/openapi-generator-cli:$(OPENAPI_GENERATOR_CLI_VERSION) generate \
	-i /local/$< \
	-g python \
	--library asyncio \
	--package-name asana_asyncio \
	--additional-properties=packageVersion=${VERSION} \
	-o /local/out/python-asyncio

asana_oas.yaml:
	wget https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml -O $@

clean:
	rm -f asana_oas.yaml
	rm -rf out
