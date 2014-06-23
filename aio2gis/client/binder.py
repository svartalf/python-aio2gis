# -*- coding: utf-8 -*-

import json
import asyncio
from urllib import parse

import aiohttp

from .exceptions import DgisError

__all__ = ('bind_api',)


def __init__(self, api):
    self.api = api


@asyncio.coroutine
def execute(self, *args, **kwargs):

    # Build GET parameters for query
    parameters = {}

    # Both positional
    for idx, arg in enumerate(args):
        if arg is None:
            continue

        try:
            parameters[self.allowed_param[idx]] = arg
        except IndexError:
            raise ValueError('Too many parameters supplied')

    # And keyword parameters
    for key, arg in kwargs.items():
        if arg is None:
            continue

        if key in parameters:
            raise ValueError('Multiple values for parameter %s supplied' % key)
        parameters[key] = arg

    parameters.update({
        'key': self.api.key,
        'version': self.api.version,
        'output': 'json',
    })

    url = parse.urlunparse(['http', self.api.host, self.path, None, parse.urlencode(parameters), None])

    response = yield from aiohttp.request('GET', url)
    body = yield from response.read_and_close()
    # Can't use `read_and_close(decode=True)` because of a https://github.com/KeepSafe/aiohttp/issues/18
    body = json.loads(body.decode('utf-8'))

    if body['response_code'] != '200':
        raise DgisError(int(body['response_code']), body['error_message'], body['error_code'])

    # Register view if required
    if self.register_views and self.api.register_views:
        response = yield from aiohttp.request('GET', body['register_bc_url'])
        if (yield from response.read_and_close()) == '0':
            raise DgisError(404, 'View registration cannot be processed', 'registerViewFailed')

    return body


def bind_api(**config):

    properties = {
        'path': config['path'],
        'method': config.get('method', 'GET'),
        'allowed_param': config['allowed_param'],
        'register_views': config.get('register_views', False),
        '__init__': __init__,
        'execute': execute,
        }

    cls = type('API%sMethod' % config['path'].title().replace('/', ''), (object,), properties)

    def _call(api, *args, **kwargs):
        return cls(api).execute(*args, **kwargs)

    return _call
