python: asana_oas.yaml
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i /local/$< \
	-g python \
	--library asyncio \
	-o /local/out/python-async

asana_oas.yaml:
	wget https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml -O $@
