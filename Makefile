VERSION=1.0.0

out/python-asyncio/dist/asana_asyncio-${VERSION}-py3-none-any.whl: out/python-asyncio/setup.py
	cd out/python-asyncio; \
	docker run --rm \
	--user $$(id -u):$$(id -g) \
	-w /code \
	-v $$(pwd):/code \
	python:3-slim \
	python3 setup.py bdist_wheel

out/python-asyncio/setup.py: asana_oas.yaml
	docker run --rm \
	--user $$(id -u):$$(id -g) \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i /local/$< \
	-g python \
	--library asyncio \
	--package-name asana_asyncio \
	--additional-properties=packageVersion=${VERSION} \
	-o /local/out/python-asyncio
	sed -i '/from asana_asyncio.models.object import object/d' out/python-asyncio/asana_asyncio/models/status_update_request.py

asana_oas.yaml:
	wget https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml -O $@

clean:
	rm -f asana_oas.yaml
	rm -rf out
