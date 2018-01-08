# -*- coding: utf-8 -*-
import base64

import requests


class Http:

    @staticmethod
    def _transform(response, transformation):
        if transformation == 'base64':
            return base64.b64decode(response.text)
        elif transformation == 'json':
            return response.json()
        return response.text

    @classmethod
    def _call(cls, method, url, transformation=None, **kwargs):
        request = getattr(requests, method)
        response = request(url, **kwargs)
        response.raise_for_status()
        return cls._transform(response, transformation)

    @classmethod
    def get(cls, url, transformation=None, **kwargs):
        return cls._call('get', url, transformation=transformation, **kwargs)

    @classmethod
    def post(cls, url, transformation=None, **kwargs):
        return cls._call('post', url, transformation=transformation, **kwargs)