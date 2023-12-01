python: asana_oas.yaml
	docker run --rm \
	--user $$(id -u):$$(id -g) \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i /local/$< \
	-g python \
	--library asyncio \
	--package-name asana_asyncio \
	-o /local/out/python-asyncio
	sed -i '/from asana_asyncio.models.object import object/d' out/python-asyncio/asana_asyncio/models/status_update_request.py

asana_oas.yaml:
	wget https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml -O $@


clean:
	rm -f asana_oas.yaml
	rm -rf out
