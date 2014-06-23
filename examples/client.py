import os
import asyncio

from aio2gis.client import API

try:
    key = os.environ['DGIS_KEY']
except KeyError:
    raise RuntimeError('Add an environment variable DGIS_KEY with 2gis API key')


@asyncio.coroutine
def test_projects_list():
    api = API(key)
    response = yield from api.project_list()
    assert response['response_code'] == '200'
    assert response['api_version'] == api.version
    print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(test_projects_list())
