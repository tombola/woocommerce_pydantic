from __future__ import annotations

from urllib.parse import urlparse

from requests import Response
from woocommerce import API as woocommmerce_api

from woocommerce_pydantic.wcapi.models import wc_collections, wc_endpoints, wc_resources


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
        return wc_endpoints.get_endpoint_model(self.url)

    def data(self) -> list[object] | object:
        """
        Return data validated as Pydantic model(s).

        Maps JSON data from the API response to a Pydantic model.

        Returns:
            list[object] | object: Pydantic model instance(s) with JSON data.

        Raises:
            ValueError: If the endpoint cannot be mapped to a Pydantic model.

        """
        if model := self.get_pydantic_model():
            # Initialize pydantic model with the JSON data
            if issubclass(model, wc_collections.WooCommerceCollection):
                return model(self.json())
            return model(**self.json())
        msg = f"Failed to map the WooCommerce API endpoint '{self.url}' to a Pydantic model."
        raise ValueError(msg)


class API(woocommmerce_api):
    """Extends the woocommerce API class to return a WooDataResponse object."""

    def get(self, endpoint: str, **kwargs) -> WooDataResponse:
        response = super().get(endpoint, **kwargs)
        return WooDataResponse(response)
