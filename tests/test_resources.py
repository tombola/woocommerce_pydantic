import json  # noqa: D100
import os
from pathlib import Path

import responses

from woocommerce_pydantic.wcapi.wc_api import API
from woocommerce_pydantic.wcapi.models import wc_collections, wc_resources

WC_URL = os.environ.get("TEST_WC_URL", "http://example.com")
WC_API_URL = f"{WC_URL}/wp-json/wc/v3"

# Currently tests do not use the API tokens as mocks using responses
wcapi = API(
    url=os.environ.get("TEST_WC_URL", "http://example.com"),
    consumer_key=os.environ.get("TEST_WC_KEY", "ck_XXXXXXXX"),
    consumer_secret=os.environ.get("TEST_WC_SECRET", "cs_XXXXXXXX"),
    version="wc/v3",
)

# Get the local directory of the current file
current_directory = os.path.dirname(os.path.abspath(__file__))

def mock_wcapi_get(endpoint: str) -> dict:
    """
    Add a mock endpoint using responses.

    Reads a JSON file corresponding to the given endpoint from the
    'data/responses/v3/' directory.
    Uses the `responses` library to mock a GET request to the WooCommerce API URL with the loaded JSON data.

    Args:
        endpoint (str): The endpoint to mock. This should be the name of the JSON
                        file (without the .json extension) located in the
                        'data/responses/v3/' directory.

    Returns:
        dict: The JSON data loaded from the file.

    """
    with (Path(current_directory) / f"data/responses/v3/{endpoint}.json").open() as f:
        orders_data = json.load(f)
    responses.add(
        responses.GET,
        f"{WC_API_URL}/{endpoint}",
        json=orders_data,
        status=200,
    )
    return orders_data

@responses.activate
def test_get_orders():
    orders_data = mock_wcapi_get("orders")

    # Call the WooCommerce API
    response = wcapi.get("orders")
    response_json = response.json()

    assert response.status_code == 200
    assert response_json[0]["id"] == 727
    assert response_json[0]["id"] == orders_data[0]["id"] # 727
    assert len(response_json) == 2

    # Test validating pydantic model manually
    orders = wc_collections.ShopOrderList(response_json)
    assert isinstance(orders.root, list)
    assert len(orders.root) == 2
    assert isinstance(orders.root[0], wc_resources.ShopOrder)
    assert isinstance(orders.root[0].id, int)
    assert orders.root[0].id == 727

    # Test validating pydantic model using the data() method
    orders = response.data()
    assert isinstance(orders, wc_collections.ShopOrderList)
    assert isinstance(orders.root, list)
    assert len(orders.root) == 2
    assert isinstance(orders.root[0], wc_resources.ShopOrder)
    assert isinstance(orders.root[0].id, int)

    first_collection_item = orders.root[0]
    assert first_collection_item.id == 727

    # Check the response data can be identified as a woocommerce collection
    assert isinstance(orders, wc_collections.WooCommerceCollection)
    # Check that collection items can be identified as woocommerce resources
    assert isinstance(first_collection_item, wc_resources.WooCommerceResource)