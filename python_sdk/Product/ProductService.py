import json
import requests
import Product
import sys
import httpx

from python_sdk.apiConfig import HTTPException, APIConfig
from ProductContext import *
from types import SimpleNamespace
from ProductMetaDeserializer import *

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

def getListOfProducts():
    api_config = APIConfig()

    base_path = api_config.base_path
    path = f"/entity/product"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json;charset=utf-8",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

        rawConvertedObject = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d)) # сырой объект листов продукта

        deserializedProductMeta = SerializeProductMeta(rawProductMeta=rawConvertedObject.meta)




def getProductById(productId):
    api_config = APIConfig()

    base_path = api_config.base_path
    path = "/entity/product/{}".format(productId)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json;charset=utf-8",
        "Authorization": f"Bearer {api_config.get_access_token()}",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    rawProduct = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))


