from woocommerce import API as woocommmerce_api
from requests import Response

from woocommerce_pydantic.wcapi.models import resource_lists, resources
from urllib.parse import urlparse


class WooDataResponse(Response):
    """Wraps the Response object to add a data() method."""

    def __new__(cls, original_instance: Response):
        obj = super().__new__(cls)
        obj.__dict__.update(original_instance.__dict__)
        obj.__init__(original_instance)
        return obj

    def __init__(self, original_instance: Response):
        pass

    def get_endpoint_components(self, url):
        parsed_url = urlparse(url)
        path = parsed_url.path
        # Remove leading slash
        path = path.lstrip("/")
        components = path.split("/")
        # remove wp-json/wc/v3
        return components[3:]

    def get_pydantic_model(self):
        url_path = self.get_endpoint_components(self.url)
        # TODO: pattern match from mapping dict
        if url_path[-1] == "orders":
            return resource_lists.ShopOrderList
        return None

    def data(self):
        return self.get_pydantic_model()(self.json())


class API(woocommmerce_api):
    def get(self, endpoint, **kwargs):
        response = super().get(endpoint, **kwargs)
        return WooDataResponse(response)
