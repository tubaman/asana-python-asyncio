# asana-python-asyncio

This is a Python asyncio client for the [Asana API](https://developers.asana.com/reference/rest-api-reference).  This client is generated from the [OpenAPI definition](https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml) using [OpenAPI Generator](https://openapi-generator.tech).


## Dependencies

   * GNU Make
   * Docker
   * wget

## Regenerate the client

    make VERSION=20231201.0

The generated client is in `./out/python-asyncio`.  The python wheel is in `./out/python-asyncio/dist`

## Install

The client is generated in a branch by date(ex: [20231201](https://github.com/tubaman/asana-python-asyncio/tree/20231201)) and tagged similarly (ex: [20231201.0](https://github.com/tubaman/asana-python-asyncio/releases/tag/20231201.0)).  You can install a tagged release like:

    pip install https://github.com/tubaman/asana-python-asyncio/releases/download/20231201.0/asana_asyncio-20231201.0-py3-none-any.whl

Documentation is in the generated README.md.  Ex: https://github.com/tubaman/asana-python-asyncio/blob/20231201.0/out/python-asyncio/README.md
