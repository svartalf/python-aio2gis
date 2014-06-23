# python-aio2gis

A Python library for accessing the 2gis API (http://api.2gis.ru) powered with [asyncio](https://docs.python.org/3/library/asyncio.html).

## Usage

### Example

    import asyncio
    from aio2gis.client import API

    @asyncio.coroutine
    def get_projects_list():
        api = API('api-key')
        response = yield from api.project_list()
        print(response)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_projects_list())

## Contributing

If you want to contribute, follow the [pep8](http://www.python.org/dev/peps/pep-0008/) guideline.
