from __future__ import annotations
from woocommerce import API as woocommmerce_api
from requests import Response

from woocommerce_pydantic.wcapi.models import wc_collections, wc_resources
from urllib.parse import urlparse


class WooDataResponse(Response):
    """Wraps the Response object to add a data() method."""

    def __new__(cls, original_response: Response) -> "WooDataResponse":
        """
        Create a new instance, copying attributes from an original Response instance.

        Args:
            original_response (Response): The original Response instance.

        """
        obj = super().__new__(cls)
        obj.__dict__.update(original_response.__dict__)
        obj.__init__(original_response)
        return obj

    def __init__(self, original_response: Response) -> None:  # noqa: D107
        pass

    def get_endpoint_components(self, url) -> list[str]:
        parsed_url = urlparse(url)
        path = parsed_url.path
        # Remove leading slash
        path = path.lstrip("/")
        components = path.split("/")
        # remove wp-json/wc/v3
        return components[3:]

    def get_pydantic_model(self) -> type | None:
        url_path = self.get_endpoint_components(self.url)
        # TODO: pattern match from mapping dict
        if url_path[-1] == "orders":
            return wc_collections.ShopOrderList
        return None

    def data(self) -> list[object] | object:
        return self.get_pydantic_model()(self.json())


class API(woocommmerce_api):
    """Extends the woocommerce API class to return a WooDataResponse object."""

    def get(self, endpoint: str, **kwargs) -> WooDataResponse:
        response = super().get(endpoint, **kwargs)
        return WooDataResponse(response)
