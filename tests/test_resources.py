import json  # noqa: D100
import os
from pathlib import Path

import pytest
import responses
from woocommerce import API

from woocommerce_pydantic.wcapi.models import resource_lists, resources

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


@responses.activate
def test_get_orders():
    # Mock the API response
    with (Path(current_directory) / "data/responses/v3/orders.json").open() as f:
        orders_data = json.load(f)

    responses.add(
        responses.GET,
        f"{WC_API_URL}/orders",
        json=orders_data,
        status=200,
    )

    # Call the WooCommerce API
    response = wcapi.get("orders")
    data = response.json()

    assert response.status_code == 200
    assert data[0]["id"] == 727
    assert data[0]["id"] == orders_data[0]["id"] # 727
    assert len(data) == 2

    # Test validated pydantic model

    orders = resource_lists.ShopOrderList(data)
    assert isinstance(orders.root, list)
    assert len(orders.root) == 2
    assert isinstance(orders.root[0], resources.ShopOrder)
    assert isinstance(orders.root[0].id, int)
    assert orders.root[0].id == 727
