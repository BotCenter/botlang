import base64
from urllib.parse import quote

import requests


def build_response_dict(request_response):

    response_dict = {
        'status-code': request_response.status_code,
        'headers': dict(request_response.headers),
        'encoding': request_response.encoding,
        'text': request_response.text
    }
    try:
        response_dict['json'] = request_response.json()
    except ValueError:
        pass

    return response_dict


def http_get_img(url, headers=None):
    response = requests.get(url, headers=headers)
    binary = response.content
    return base64.b64encode(binary).decode('utf-8')


def http_get(url, headers=None):

    response = requests.get(url, headers=headers)
    return build_response_dict(response)


def http_post_form(url, data, headers=None):
    response = requests.post(url, data=data, headers=headers)
    return build_response_dict(response)


def http_post_json(url, json, headers=None):

    response = requests.post(url, json=json, headers=headers)
    return build_response_dict(response)


def http_post(url, json, headers=None):

    return http_post_json(url, json, headers)


def http_delete(url, headers=None):

    response = requests.delete(url, headers=headers)
    return build_response_dict(response)


def uri_escape(uri_part):
    return quote(uri_part)


HTTP_PRIMITIVES = {
    'http-get': http_get,
    'http-post': http_post,
    'http-post-form': http_post_form,
    'http-delete': http_delete,
    'uri-escape': uri_escape,
    'http-get-img': http_get_img
}
