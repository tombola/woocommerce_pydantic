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
    underscore_filename = endpoint.lstrip('/').replace('/', '_')
    example_file = f"data/responses/v3/{underscore_filename}.json"
    with (Path(current_directory) / example_file).open() as f:
        data = json.load(f)
    responses.add(
        responses.GET,
        f"{WC_API_URL}/{endpoint}",
        json=data,
        status=200,
    )
    return data

@responses.activate
def test_get_orders():
    """Test that a request to endpoint 'orders' returns validated ShopOrderList instance."""
    orders_data = mock_wcapi_get("orders")  # noqa: F841

    # Call the WooCommerce API
    response = wcapi.get("orders")
    response_json = response.json()
    first_json_item_id = response_json[0]["id"]
    json_length = len(response_json)

    assert response.status_code == 200
    # assert response_json[0]["id"] == first_item_id
    # assert response_json[0]["id"] == orders_data[0]["id"] # 727
    # assert len(response_json) == 2

    # Test validating pydantic model manually
    orders = wc_collections.ShopOrderList(response_json)
    assert isinstance(orders.root, list)
    assert len(orders.root) == json_length
    assert isinstance(orders.root[0], wc_resources.ShopOrder)
    assert isinstance(orders.root[0].id, int)
    assert orders.root[0].id == first_json_item_id

    # Test validating pydantic model using the data() method
    orders = response.data()
    assert isinstance(orders, wc_collections.ShopOrderList)
    assert isinstance(orders.root, list)
    assert len(orders.root) == json_length
    assert isinstance(orders.root[0], wc_resources.ShopOrder)
    assert isinstance(orders.root[0].id, int)

    first_collection_item = orders.root[0]
    assert first_collection_item.id == first_json_item_id

    # Check the response data can be identified as a woocommerce collection
    assert isinstance(orders, wc_collections.WooCommerceCollection)
    # Check that collection items can be identified as woocommerce resources
    assert isinstance(first_collection_item, wc_resources.WooCommerceResource)


@responses.activate
def test_get_order():
    # "/orders/{id}": wc_resources.ShopOrder,
    order_id = 123
    order_data = mock_wcapi_get(f"orders/{order_id}")
    response = wcapi.get(f"orders/{order_id}")
    order = response.data()
    assert isinstance(order, wc_resources.ShopOrder)
    assert order_data["id"] == order.id

# @responses.activate
# def test_get_coupons():
#     coupons_data = mock_wcapi_get("coupons")
#     response = wcapi.get("coupons")
#     coupons = response.data()
#     assert isinstance(coupons, wc_collections.ShopCouponList)
#     assert coupons_data[0]["id"] == coupons.root[0].id

# @responses.activate
# def test_get_coupon():
#     coupon_id = 123
#     coupon_data = mock_wcapi_get(f"coupons/{coupon_id}")
#     response = wcapi.get(f"coupons/{coupon_id}")
#     coupon = response.data()
#     assert isinstance(coupon, wc_resources.ShopCoupon)
#     assert coupon_data["id"] == coupon.id

# @responses.activate
# def test_get_customer_downloads():
#     customer_id = 123
#     downloads_data = mock_wcapi_get(f"customers/{customer_id}/downloads")
#     response = wcapi.get(f"customers/{customer_id}/downloads")
#     downloads = response.data()
#     assert isinstance(downloads, wc_collections.CustomerDownloadList)
#     assert downloads_data[0]["id"] == downloads.root[0].id

# @responses.activate
# def test_get_customers():
#     customers_data = mock_wcapi_get("customers")
#     response = wcapi.get("customers")
#     customers = response.data()
#     assert isinstance(customers, wc_collections.CustomerList)
#     assert customers_data[0]["id"] == customers.root[0].id

# @responses.activate
# def test_get_customer():
#     customer_id = 123
#     customer_data = mock_wcapi_get(f"customers/{customer_id}")
#     response = wcapi.get(f"customers/{customer_id}")
#     customer = response.data()
#     assert isinstance(customer, wc_resources.Customer)
#     assert customer_data["id"] == customer.id

# @responses.activate
# def test_get_order_notes():
#     order_id = 123
#     notes_data = mock_wcapi_get(f"orders/{order_id}/notes")
#     response = wcapi.get(f"orders/{order_id}/notes")
#     notes = response.data()
#     assert isinstance(notes, wc_collections.OrderNoteList)
#     assert notes_data[0]["id"] == notes.root[0].id

# @responses.activate
# def test_get_order_note():
#     order_id = 123
#     note_id = 456
#     note_data = mock_wcapi_get(f"orders/{order_id}/notes/{note_id}")
#     response = wcapi.get(f"orders/{order_id}/notes/{note_id}")
#     note = response.data()
#     assert isinstance(note, wc_resources.OrderNote)
#     assert note_data["id"] == note.id

# @responses.activate
# def test_get_order_refunds():
#     order_id = 123
#     refunds_data = mock_wcapi_get(f"orders/{order_id}/refunds")
#     response = wcapi.get(f"orders/{order_id}/refunds")
#     refunds = response.data()
#     assert isinstance(refunds, wc_collections.ShopOrderRefundList)
#     assert refunds_data[0]["id"] == refunds.root[0].id

# @responses.activate
# def test_get_order_refund():
#     order_id = 123
#     refund_id = 456
#     refund_data = mock_wcapi_get(f"orders/{order_id}/refunds/{refund_id}")
#     response = wcapi.get(f"orders/{order_id}/refunds/{refund_id}")
#     refund = response.data()
#     assert isinstance(refund, wc_resources.ShopOrderRefund)
#     assert refund_data["id"] == refund.id

# @responses.activate
# def test_get_product_attribute_terms():
#     attribute_id = 123
#     terms_data = mock_wcapi_get(f"products/attributes/{attribute_id}/terms")
#     response = wcapi.get(f"products/attributes/{attribute_id}/terms")
#     terms = response.data()
#     assert isinstance(terms, wc_collections.ProductAttributeTermList)
#     assert terms_data[0]["id"] == terms.root[0].id

# @responses.activate
# def test_get_product_attribute_term():
#     attribute_id = 123
#     term_id = 456
#     term_data = mock_wcapi_get(f"products/attributes/{attribute_id}/terms/{term_id}")
#     response = wcapi.get(f"products/attributes/{attribute_id}/terms/{term_id}")
#     term = response.data()
#     assert isinstance(term, wc_resources.ProductAttributeTerm)
#     assert term_data["id"] == term.id

# @responses.activate
# def test_get_product_attributes():
#     attributes_data = mock_wcapi_get("products/attributes")
#     response = wcapi.get("products/attributes")
#     attributes = response.data()
#     assert isinstance(attributes, wc_collections.ProductAttributeList)
#     assert attributes_data[0]["id"] == attributes.root[0].id

# @responses.activate
# def test_get_product_attribute():
#     attribute_id = 123
#     attribute_data = mock_wcapi_get(f"products/attributes/{attribute_id}")
#     response = wcapi.get(f"products/attributes/{attribute_id}")
#     attribute = response.data()
#     assert isinstance(attribute, wc_resources.ProductAttribute)
#     assert attribute_data["id"] == attribute.id

# @responses.activate
# def test_get_product_categories():
#     categories_data = mock_wcapi_get("products/categories")
#     response = wcapi.get("products/categories")
#     categories = response.data()
#     assert isinstance(categories, wc_collections.ProductCatList)
#     assert categories_data[0]["id"] == categories.root[0].id

# @responses.activate
# def test_get_product_category():
#     category_id = 123
#     category_data = mock_wcapi_get(f"products/categories/{category_id}")
#     response = wcapi.get(f"products/categories/{category_id}")
#     category = response.data()
#     assert isinstance(category, wc_resources.ProductCat)
#     assert category_data["id"] == category.id

# @responses.activate
# def test_get_product_reviews():
#     reviews_data = mock_wcapi_get("products/reviews")
#     response = wcapi.get("products/reviews")
#     reviews = response.data()
#     assert isinstance(reviews, wc_collections.ProductReviewList)
#     assert reviews_data[0]["id"] == reviews.root[0].id

# @responses.activate
# def test_get_product_review():
#     review_id = 123
#     review_data = mock_wcapi_get(f"products/reviews/{review_id}")
#     response = wcapi.get(f"products/reviews/{review_id}")
#     review = response.data()
#     assert isinstance(review, wc_resources.ProductReview)
#     assert review_data["id"] == review.id

# @responses.activate
# def test_get_product_shipping_classes():
#     shipping_classes_data = mock_wcapi_get("products/shipping_classes")
#     response = wcapi.get("products/shipping_classes")
#     shipping_classes = response.data()
#     assert isinstance(shipping_classes, wc_collections.ProductShippingClassList)
#     assert shipping_classes_data[0]["id"] == shipping_classes.root[0].id

# @responses.activate
# def test_get_product_shipping_class():
#     shipping_class_id = 123
#     shipping_class_data = mock_wcapi_get(f"products/shipping_classes/{shipping_class_id}")
#     response = wcapi.get(f"products/shipping_classes/{shipping_class_id}")
#     shipping_class = response.data()
#     assert isinstance(shipping_class, wc_resources.ProductShippingClass)
#     assert shipping_class_data["id"] == shipping_class.id

# @responses.activate
# def test_get_product_tags():
#     tags_data = mock_wcapi_get("products/tags")
#     response = wcapi.get("products/tags")
#     tags = response.data()
#     assert isinstance(tags, wc_collections.ProductTagList)
#     assert tags_data[0]["id"] == tags.root[0].id

# @responses.activate
# def test_get_product_tag():
#     tag_id = 123
#     tag_data = mock_wcapi_get(f"products/tags/{tag_id}")
#     response = wcapi.get(f"products/tags/{tag_id}")
#     tag = response.data()
#     assert isinstance(tag, wc_resources.ProductTag)
#     assert tag_data["id"] == tag.id

# @responses.activate
# def test_get_products():
#     products_data = mock_wcapi_get("products")
#     response = wcapi.get("products")
#     products = response.data()
#     assert isinstance(products, wc_collections.ProductList)
#     assert products_data[0]["id"] == products.root[0].id

# @responses.activate
# def test_get_product():
#     product_id = 123
#     product_data = mock_wcapi_get(f"products/{product_id}")
#     response = wcapi.get(f"products/{product_id}")
#     product = response.data()
#     assert isinstance(product, wc_resources.Product)
#     assert product_data["id"] == product.id

# @responses.activate
# def test_get_product_variations():
#     product_id = 123
#     variations_data = mock_wcapi_get(f"products/{product_id}/variations")
#     response = wcapi.get(f"products/{product_id}/variations")
#     variations = response.data()
#     assert isinstance(variations, wc_collections.ProductVariationList)
#     assert variations_data[0]["id"] == variations.root[0].id

# @responses.activate
# def test_get_product_variation():
#     product_id = 123
#     variation_id = 456
#     variation_data = mock_wcapi_get(f"products/{product_id}/variations/{variation_id}")
#     response = wcapi.get(f"products/{product_id}/variations/{variation_id}")
#     variation = response.data()
#     assert isinstance(variation, wc_resources.ProductVariation)
#     assert variation_data["id"] == variation.id

# @responses.activate
# def test_get_reports_sales():
#     sales_data = mock_wcapi_get("reports/sales")
#     response = wcapi.get("reports/sales")
#     sales = response.data()
#     assert isinstance(sales, wc_collections.SalesReportList)
#     assert sales_data[0]["id"] == sales.root[0].id

# @responses.activate
# def test_get_reports_top_sellers():
#     top_sellers_data = mock_wcapi_get("reports/top_sellers")
#     response = wcapi.get("reports/top_sellers")
#     top_sellers = response.data()
#     assert isinstance(top_sellers, wc_collections.TopSellersReportList)
#     assert top_sellers_data[0]["id"] == top_sellers.root[0].id

# @responses.activate
# def test_get_reports_orders_totals():
#     orders_totals_data = mock_wcapi_get("reports/orders/totals")
#     response = wcapi.get("reports/orders/totals")
#     orders_totals = response.data()
#     assert isinstance(orders_totals, wc_collections.ReportOrderTotalList)
#     assert orders_totals_data[0]["id"] == orders_totals.root[0].id

# @responses.activate
# def test_get_reports_products_totals():
#     products_totals_data = mock_wcapi_get("reports/products/totals")
#     response = wcapi.get("reports/products/totals")
#     products_totals = response.data()
#     assert isinstance(products_totals, wc_collections.ReportProductTotalList)
#     assert products_totals_data[0]["id"] == products_totals.root[0].id

# @responses.activate
# def test_get_reports_customers_totals():
#     customers_totals_data = mock_wcapi_get("reports/customers/totals")
#     response = wcapi.get("reports/customers/totals")
#     customers_totals = response.data()
#     assert isinstance(customers_totals, wc_collections.ReportCustomerTotalList)
#     assert customers_totals_data[0]["id"] == customers_totals.root[0].id

# @responses.activate
# def test_get_reports_coupons_totals():
#     coupons_totals_data = mock_wcapi_get("reports/coupons/totals")
#     response = wcapi.get("reports/coupons/totals")
#     coupons_totals = response.data()
#     assert isinstance(coupons_totals, wc_collections.ReportCouponTotalList)
#     assert coupons_totals_data[0]["id"] == coupons_totals.root[0].id

# @responses.activate
# def test_get_reports_reviews_totals():
#     reviews_totals_data = mock_wcapi_get("reports/reviews/totals")
#     response = wcapi.get("reports/reviews/totals")
#     reviews_totals = response.data()
#     assert isinstance(reviews_totals, wc_collections.ReportReviewTotalList)
#     assert reviews_totals_data[0]["id"] == reviews_totals.root[0].id

# @responses.activate
# def test_get_reports():
#     reports_data = mock_wcapi_get("reports")
#     response = wcapi.get("reports")
#     reports = response.data()
#     assert isinstance(reports, wc_collections.ReportList)
#     assert reports_data[0]["id"] == reports.root[0].id

# @responses.activate
# def test_get_shipping_zones():
#     zones_data = mock_wcapi_get("shipping/zones")
#     response = wcapi.get("shipping/zones")
#     zones = response.data()
#     assert isinstance(zones, wc_collections.ShippingZoneList)
#     assert zones_data[0]["id"] == zones.root[0].id

# @responses.activate
# def test_get_shipping_zone():
#     zone_id = 123
#     zone_data = mock_wcapi_get(f"shipping/zones/{zone_id}")
#     response = wcapi.get(f"shipping/zones/{zone_id}")
#     zone = response.data()
#     assert isinstance(zone, wc_resources.ShippingZone)
#     assert zone_data["id"] == zone.id

# @responses.activate
# def test_get_shipping_zone_locations():
#     zone_id = 123
#     locations_data = mock_wcapi_get(f"shipping/zones/{zone_id}/locations")
#     response = wcapi.get(f"shipping/zones/{zone_id}/locations")
#     locations = response.data()
#     assert isinstance(locations, wc_collections.ShippingZoneLocationList)
#     assert locations_data[0]["id"] == locations.root[0].id

# @responses.activate
# def test_get_shipping_zone_methods():
#     zone_id = 123
#     methods_data = mock_wcapi_get(f"shipping/zones/{zone_id}/methods")
#     response = wcapi.get(f"shipping/zones/{zone_id}/methods")
#     methods = response.data()
#     assert isinstance(methods, wc_collections.ShippingZoneMethodList)
#     assert methods_data[0]["id"] == methods.root[0].id

# @responses.activate
# def test_get_shipping_zone_method():
#     zone_id = 123
#     instance_id = 456
#     method_data = mock_wcapi_get(f"shipping/zones/{zone_id}/methods/{instance_id}")
#     response = wcapi.get(f"shipping/zones/{zone_id}/methods/{instance_id}")
#     method = response.data()
#     assert isinstance(method, wc_resources.ShippingZoneMethod)
#     assert method_data["id"] == method.id

# @responses.activate
# def test_get_taxes_classes():
#     classes_data = mock_wcapi_get("taxes/classes")
#     response = wcapi.get("taxes/classes")
#     classes = response.data()
#     assert isinstance(classes, wc_collections.TaxClassList)
#     assert classes_data[0]["id"] == classes.root[0].id

# @responses.activate
# def test_get_taxes_class():
#     slug = "standard"
#     class_data = mock_wcapi_get(f"taxes/classes/{slug}")
#     response = wcapi.get(f"taxes/classes/{slug}")
#     tax_class = response.data()
#     assert isinstance(tax_class, wc_resources.TaxClass)
#     assert class_data["slug"] == tax_class.slug

# @responses.activate
# def test_get_taxes():
#     taxes_data = mock_wcapi_get("taxes")
#     response = wcapi.get("taxes")
#     taxes = response.data()
#     assert isinstance(taxes, wc_collections.TaxList)
#     assert taxes_data[0]["id"] == taxes.root[0].id

# @responses.activate
# def test_get_tax():
#     tax_id = 123
#     tax_data = mock_wcapi_get(f"taxes/{tax_id}")
#     response = wcapi.get(f"taxes/{tax_id}")
#     tax = response.data()
#     assert isinstance(tax, wc_resources.Tax)
#     assert tax_data["id"] == tax.id

# @responses.activate
# def test_get_webhooks():
#     webhooks_data = mock_wcapi_get("webhooks")
#     response = wcapi.get("webhooks")
#     webhooks = response.data()
#     assert isinstance(webhooks, wc_collections.WebhookList)
#     assert webhooks_data[0]["id"] == webhooks.root[0].id

# @responses.activate
# def test_get_webhook():
#     webhook_id = 123
#     webhook_data = mock_wcapi_get(f"webhooks/{webhook_id}")
#     response = wcapi.get(f"webhooks/{webhook_id}")
#     webhook = response.data()
#     assert isinstance(webhook, wc_resources.Webhook)
#     assert webhook_data["id"] == webhook.id

# @responses.activate
# def test_get_system_status():
#     status_data = mock_wcapi_get("system_status")
#     response = wcapi.get("system_status")
#     status = response.data()
#     assert isinstance(status, wc_resources.SystemStatus)
#     assert status_data["id"] == status.id

# @responses.activate
# def test_get_system_status_tools():
#     tools_data = mock_wcapi_get("system_status/tools")
#     response = wcapi.get("system_status/tools")
#     tools = response.data()
#     assert isinstance(tools, wc_collections.SystemStatusToolList)
#     assert tools_data[0]["id"] == tools.root[0].id

# @responses.activate
# def test_get_system_status_tool():
#     tool_id = 123
#     tool_data = mock_wcapi_get(f"system_status/tools/{tool_id}")
#     response = wcapi.get(f"system_status/tools/{tool_id}")
#     tool = response.data()
#     assert isinstance(tool, wc_resources.SystemStatusTool)
#     assert tool_data["id"] == tool.id

# @responses.activate
# def test_get_shipping_methods():
#     methods_data = mock_wcapi_get("shipping_methods")
#     response = wcapi.get("shipping_methods")
#     methods = response.data()
#     assert isinstance(methods, wc_collections.ShippingMethodList)
#     assert methods_data[0]["id"] == methods.root[0].id

# @responses.activate
# def test_get_shipping_method():
#     method_id = 123
#     method_data = mock_wcapi_get(f"shipping_methods/{method_id}")
#     response = wcapi.get(f"shipping_methods/{method_id}")
#     method = response.data()
#     assert isinstance(method, wc_resources.ShippingMethod)
#     assert method_data["id"] == method.id

# @responses.activate
# def test_get_payment_gateways():
#     gateways_data = mock_wcapi_get("payment_gateways")
#     response = wcapi.get("payment_gateways")
#     gateways = response.data()
#     assert isinstance(gateways, wc_collections.PaymentGatewayList)
#     assert gateways_data[0]["id"] == gateways.root[0].id

# @responses.activate
# def test_get_payment_gateway():
#     gateway_id = 123
#     gateway_data = mock_wcapi_get(f"payment_gateways/{gateway_id}")
#     response = wcapi.get(f"payment_gateways/{gateway_id}")
#     gateway = response.data()
#     assert isinstance(gateway, wc_resources.PaymentGateway)
#     assert gateway_data["id"] == gateway.id

# @responses.activate
# def test_get_data():
#     data_index_data = mock_wcapi_get("data")
#     response = wcapi.get("data")
#     data_index = response.data()
#     assert isinstance(data_index, wc_resources.DataIndex)
#     assert data_index_data["id"] == data_index.id

# @responses.activate
# def test_get_data_continents():
#     continents_data = mock_wcapi_get("data/continents")
#     response = wcapi.get("data/continents")
#     continents = response.data()
#     assert isinstance(continents, wc_collections.DataContinentsList)
#     assert continents_data[0]["id"] == continents.root[0].id

# @responses.activate
# def test_get_data_continent():
#     location = "EU"
#     continent_data = mock_wcapi_get(f"data/continents/{location}")
#     response = wcapi.get(f"data/continents/{location}")
#     continent = response.data()
#     assert isinstance(continent, wc_resources.DataContinents)
#     assert continent_data["location"] == continent.location

# @responses.activate
# def test_get_data_countries():
#     countries_data = mock_wcapi_get("data/countries")
#     response = wcapi.get("data/countries")
#     countries = response.data()
#     assert isinstance(countries, wc_collections.DataCountriesList)
#     assert countries_data[0]["id"] == countries.root[0].id

# @responses.activate
# def test_get_data_country():
#     location = "US"
#     country_data = mock_wcapi_get(f"data/countries/{location}")
#     response = wcapi.get(f"data/countries/{location}")
#     country = response.data()
#     assert isinstance(country, wc_resources.DataCountries)
#     assert country_data["location"] == country.location

# @responses.activate
# def test_get_data_currencies():
#     currencies_data = mock_wcapi_get("data/currencies")
#     response = wcapi.get("data/currencies")
#     currencies = response.data()
#     assert isinstance(currencies, wc_collections.DataCurrenciesList)
#     assert currencies_data[0]["id"] == currencies.root[0].id

# @responses.activate
# def test_get_data_currency():
#     currency = "USD"
#     currency_data = mock_wcapi_get(f"data/currencies/{currency}")
#     response = wcapi.get(f"data/currencies/{currency}")
#     currency_obj = response.data()
#     assert isinstance(currency_obj, wc_resources.DataCurrencies)
#     assert currency_data["currency"] == currency_obj.currency

# @responses.activate
# def test_get_data_currencies_current():
#     current_currency_data = mock_wcapi_get("data/currencies/current")
#     response = wcapi.get("data/currencies/current")
#     current_currency = response.data()
#     assert isinstance(current_currency, wc_resources.DataCurrencies)
#     assert current_currency_data["id"] == current_currency.id