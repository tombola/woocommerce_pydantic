import json  # noqa: D100
import os
from pathlib import Path
import yaml
import responses
from responses import _recorder

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
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def load_recorded_response_json(yaml_file: str) -> dict | None:
    """Load the data from the recorded API response for comparison."""
    with open(yaml_file) as f:
        data = yaml.safe_load(f)
        if "responses" in data and data["responses"]:
            return json.loads(data["responses"][0]["response"]["body"])
        raise ValueError(f"No recorded data for request '{yaml_file}'")

def _recfile(name):
    """Return path of recorded response file."""
    # eg tests/data/responses/v3/order.yaml
    return f"tests/data/responses/v3/{name}.yaml"

# def get_response_filename(endpoint) -> str:
#     underscore_filename = endpoint.lstrip("/").replace("/", "_")
#     return f"data/responses/v3/{underscore_filename}.json"
#     """
#     Add a mock endpoint using responses.

#     Reads a JSON file corresponding to the given endpoint from the
#     "data/responses/v3/" directory.
#     Uses the `responses` library to mock a GET request to the WooCommerce API URL with the loaded JSON data.

#     Args:
#         endpoint (str): The endpoint to mock. This should be the name of the JSON
#                         file (without the .json extension) located in the
#                         "data/responses/v3/" directory.

#     Returns:
#         dict: The JSON data loaded from the file.

#     """

#     with (Path(CURRENT_DIRECTORY) / get_response_filename(endpoint)).open() as f:
#         data = json.load(f)
#     responses.add(
#         responses.GET,
#         f"{WC_API_URL}/{endpoint}",
#         json=data,
#         status=200,
#     )
#     return data

@responses.activate
# delete url params from yaml file
# @_recorder.record(file_path="tests/data/responses/v3/orders.yaml")
def test_get_orders():
    """Test that a request to endpoint "orders" returns validated ShopOrderList instance."""
    responses._add_from_file(file_path="tests/data/responses/v3/orders.yaml")
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
# @_recorder.record(file_path=_recfile("order"))
def test_get_order():
    """/orders/{id}: wc_resources.ShopOrder"""  # noqa: D400, D415
    recorded_response = _recfile("order")
    responses._add_from_file(file_path=recorded_response)
    order_data = load_recorded_response_json(recorded_response)

    order_id = 77
    response = wcapi.get(f"orders/{order_id}")
    assert response.status_code == 200
    order = response.data()
    assert isinstance(order, wc_resources.ShopOrder)
    assert order.id == order_data["id"]

# @responses.activate
# @_recorder.record(file_path=_recfile("coupons"))
# def test_get_coupons():
#   recorded_response = _recfile("coupons")
    # coupons_data = load_recorded_response_json(recorded_response)
    # responses._add_from_file(file_path=recorded_response)
    # response = wcapi.get("coupons")
    # coupons = response.data()
    # assert isinstance(coupons, wc_collections.ShopCouponList)
    # assert coupons_data[0]["id"] == coupons.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("coupon"))
# def test_get_coupon():
#     recorded_response = _recfile("coupon")
#     responses._add_from_file(file_path=recorded_response)
#     coupon_data = load_recorded_response_json(recorded_response)
#     coupon_id = 12
#     response = wcapi.get(f"coupons/{coupon_id}")
#     coupon = response.data()
#     assert isinstance(coupon, wc_resources.ShopCoupon)
#     assert coupon_data["id"] == coupon.id

# @responses.activate
# @_recorder.record(file_path=_recfile("customer_downloads"))
# def test_get_customer_downloads():
#     recorded_response = _recfile("customer_downloads")
#     responses._add_from_file(file_path=recorded_response)
#     customer_downloads_data = load_recorded_response_json(recorded_response)
#     customer_id = 12
#     response = wcapi.get(f"customers/{customer_id}/downloads")
#     downloads = response.data()
#     assert isinstance(downloads, wc_collections.CustomerDownloadList)
#     assert downloads_data[0]["id"] == downloads.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("customers"))
# def test_get_customers():
#     recorded_response = _recfile("customers")
#     responses._add_from_file(file_path=recorded_response)
#     customers_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("customers")
#     customers = response.data()
#     assert isinstance(customers, wc_collections.CustomerList)
#     assert customers_data[0]["id"] == customers.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("customer"))
# def test_get_customer():
#     recorded_response = _recfile("customer")
#     responses._add_from_file(file_path=recorded_response)
#     customer_data = load_recorded_response_json(recorded_response)
#     customer_id = 12
#     response = wcapi.get(f"customers/{customer_id}")
#     customer = response.data()
#     assert isinstance(customer, wc_resources.Customer)
#     assert customer_data["id"] == customer.id

# @responses.activate
# @_recorder.record(file_path=_recfile("order_notes"))
# def test_get_order_notes():
#     recorded_response = _recfile("order_notes")
#     responses._add_from_file(file_path=recorded_response)
#     order_notes_data = load_recorded_response_json(recorded_response)
#     order_id = 12
#     response = wcapi.get(f"orders/{order_id}/notes")
#     notes = response.data()
#     assert isinstance(notes, wc_collections.OrderNoteList)
#     assert notes_data[0]["id"] == notes.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("order_note"))
# def test_get_order_note():
#     recorded_response = _recfile("order_note")
#     responses._add_from_file(file_path=recorded_response)
#     order_note_data = load_recorded_response_json(recorded_response)
#     order_id = 123
#     note_id = 45
#     response = wcapi.get(f"orders/{order_id}/notes/{note_id}")
#     note = response.data()
#     assert isinstance(note, wc_resources.OrderNote)
#     assert note_data["id"] == note.id

# @responses.activate
# @_recorder.record(file_path=_recfile("order_refunds"))
# def test_get_order_refunds():
#     recorded_response = _recfile("order_refunds")
#     responses._add_from_file(file_path=recorded_response)
#     order_refunds_data = load_recorded_response_json(recorded_response)
#     order_id = 12
#     response = wcapi.get(f"orders/{order_id}/refunds")
#     refunds = response.data()
#     assert isinstance(refunds, wc_collections.ShopOrderRefundList)
#     assert refunds_data[0]["id"] == refunds.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("order_refund"))
# def test_get_order_refund():
#     recorded_response = _recfile("order_refund")
#     responses._add_from_file(file_path=recorded_response)
#     order_refund_data = load_recorded_response_json(recorded_response)
#     order_id = 123
#     refund_id = 45
#     response = wcapi.get(f"orders/{order_id}/refunds/{refund_id}")
#     refund = response.data()
#     assert isinstance(refund, wc_resources.ShopOrderRefund)
#     assert refund_data["id"] == refund.id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_attribute_terms"))
# def test_get_product_attribute_terms():
#     recorded_response = _recfile("product_attribute_terms")
#     responses._add_from_file(file_path=recorded_response)
#     product_attribute_terms_data = load_recorded_response_json(recorded_response)
#     attribute_id = 12
#     response = wcapi.get(f"products/attributes/{attribute_id}/terms")
#     terms = response.data()
#     assert isinstance(terms, wc_collections.ProductAttributeTermList)
#     assert terms_data[0]["id"] == terms.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_attribute_term"))
# def test_get_product_attribute_term():
#     recorded_response = _recfile("product_attribute_term")
#     responses._add_from_file(file_path=recorded_response)
#     product_attribute_term_data = load_recorded_response_json(recorded_response)
#     attribute_id = 123
#     term_id = 45
#     response = wcapi.get(f"products/attributes/{attribute_id}/terms/{term_id}")
#     term = response.data()
#     assert isinstance(term, wc_resources.ProductAttributeTerm)
#     assert term_data["id"] == term.id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_attributes"))
# def test_get_product_attributes():
#     recorded_response = _recfile("product_attributes")
#     responses._add_from_file(file_path=recorded_response)
#     product_attributes_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("products/attributes")
#     attributes = response.data()
#     assert isinstance(attributes, wc_collections.ProductAttributeList)
#     assert attributes_data[0]["id"] == attributes.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_attribute"))
# def test_get_product_attribute():
#     recorded_response = _recfile("product_attribute")
#     responses._add_from_file(file_path=recorded_response)
#     product_attribute_data = load_recorded_response_json(recorded_response)
#     attribute_id = 12
#     response = wcapi.get(f"products/attributes/{attribute_id}")
#     attribute = response.data()
#     assert isinstance(attribute, wc_resources.ProductAttribute)
#     assert attribute_data["id"] == attribute.id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_categories"))
# def test_get_product_categories():
#     recorded_response = _recfile("product_categories")
#     responses._add_from_file(file_path=recorded_response)
#     product_categories_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("products/categories")
#     categories = response.data()
#     assert isinstance(categories, wc_collections.ProductCatList)
#     assert categories_data[0]["id"] == categories.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_category"))
# def test_get_product_category():
#     recorded_response = _recfile("product_category")
#     responses._add_from_file(file_path=recorded_response)
#     product_category_data = load_recorded_response_json(recorded_response)
#     category_id = 12
#     response = wcapi.get(f"products/categories/{category_id}")
#     category = response.data()
#     assert isinstance(category, wc_resources.ProductCat)
#     assert category_data["id"] == category.id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_reviews"))
# def test_get_product_reviews():
#     recorded_response = _recfile("product_reviews")
#     responses._add_from_file(file_path=recorded_response)
#     product_reviews_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("products/reviews")
#     reviews = response.data()
#     assert isinstance(reviews, wc_collections.ProductReviewList)
#     assert reviews_data[0]["id"] == reviews.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_review"))
# def test_get_product_review():
#     recorded_response = _recfile("product_review")
#     responses._add_from_file(file_path=recorded_response)
#     product_review_data = load_recorded_response_json(recorded_response)
#     review_id = 12
#     response = wcapi.get(f"products/reviews/{review_id}")
#     review = response.data()
#     assert isinstance(review, wc_resources.ProductReview)
#     assert review_data["id"] == review.id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_shipping_classes"))
# def test_get_product_shipping_classes():
#     recorded_response = _recfile("product_shipping_classes")
#     responses._add_from_file(file_path=recorded_response)
#     product_shipping_classes_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("products/shipping_classes")
#     shipping_classes = response.data()
#     assert isinstance(shipping_classes, wc_collections.ProductShippingClassList)
#     assert shipping_classes_data[0]["id"] == shipping_classes.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_shipping_class"))
# def test_get_product_shipping_class():
#     recorded_response = _recfile("product_shipping_class")
#     responses._add_from_file(file_path=recorded_response)
#     product_shipping_class_data = load_recorded_response_json(recorded_response)
#     shipping_class_id = 12
#     response = wcapi.get(f"products/shipping_classes/{shipping_class_id}")
#     shipping_class = response.data()
#     assert isinstance(shipping_class, wc_resources.ProductShippingClass)
#     assert shipping_class_data["id"] == shipping_class.id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_tags"))
# def test_get_product_tags():
#     recorded_response = _recfile("product_tags")
#     responses._add_from_file(file_path=recorded_response)
#     product_tags_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("products/tags")
#     tags = response.data()
#     assert isinstance(tags, wc_collections.ProductTagList)
#     assert tags_data[0]["id"] == tags.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_tag"))
# def test_get_product_tag():
#     recorded_response = _recfile("product_tag")
#     responses._add_from_file(file_path=recorded_response)
#     product_tag_data = load_recorded_response_json(recorded_response)
#     tag_id = 12
#     response = wcapi.get(f"products/tags/{tag_id}")
#     tag = response.data()
#     assert isinstance(tag, wc_resources.ProductTag)
#     assert tag_data["id"] == tag.id

# @responses.activate
# @_recorder.record(file_path=_recfile("products"))
# def test_get_products():
#     recorded_response = _recfile("products")
#     responses._add_from_file(file_path=recorded_response)
#     products_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("products")
#     products = response.data()
#     assert isinstance(products, wc_collections.ProductList)
#     assert products_data[0]["id"] == products.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("product"))
# def test_get_product():
#     recorded_response = _recfile("product")
#     responses._add_from_file(file_path=recorded_response)
#     product_data = load_recorded_response_json(recorded_response)
#     product_id = 12
#     response = wcapi.get(f"products/{product_id}")
#     product = response.data()
#     assert isinstance(product, wc_resources.Product)
#     assert product_data["id"] == product.id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_variations"))
# def test_get_product_variations():
#     recorded_response = _recfile("product_variations")
#     responses._add_from_file(file_path=recorded_response)
#     product_variations_data = load_recorded_response_json(recorded_response)
#     product_id = 12
#     response = wcapi.get(f"products/{product_id}/variations")
#     variations = response.data()
#     assert isinstance(variations, wc_collections.ProductVariationList)
#     assert variations_data[0]["id"] == variations.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("product_variation"))
# def test_get_product_variation():
#     recorded_response = _recfile("product_variation")
#     responses._add_from_file(file_path=recorded_response)
#     product_variation_data = load_recorded_response_json(recorded_response)
#     product_id = 123
#     variation_id = 45
#     response = wcapi.get(f"products/{product_id}/variations/{variation_id}")
#     variation = response.data()
#     assert isinstance(variation, wc_resources.ProductVariation)
#     assert variation_data["id"] == variation.id

# @responses.activate
# @_recorder.record(file_path=_recfile("reports_sales"))
# def test_get_reports_sales():
#     recorded_response = _recfile("reports_sales")
#     responses._add_from_file(file_path=recorded_response)
#     reports_sales_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("reports/sales")
#     sales = response.data()
#     assert isinstance(sales, wc_collections.SalesReportList)
#     assert sales_data[0]["id"] == sales.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("reports_top_sellers"))
# def test_get_reports_top_sellers():
#     recorded_response = _recfile("reports_top_sellers")
#     responses._add_from_file(file_path=recorded_response)
#     reports_top_sellers_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("reports/top_sellers")
#     top_sellers = response.data()
#     assert isinstance(top_sellers, wc_collections.TopSellersReportList)
#     assert top_sellers_data[0]["id"] == top_sellers.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("reports_orders_totals"))
# def test_get_reports_orders_totals():
#     recorded_response = _recfile("reports_orders_totals")
#     responses._add_from_file(file_path=recorded_response)
#     reports_orders_totals_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("reports/orders/totals")
#     orders_totals = response.data()
#     assert isinstance(orders_totals, wc_collections.ReportOrderTotalList)
#     assert orders_totals_data[0]["id"] == orders_totals.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("reports_products_totals"))
# def test_get_reports_products_totals():
#     recorded_response = _recfile("reports_products_totals")
#     responses._add_from_file(file_path=recorded_response)
#     reports_products_totals_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("reports/products/totals")
#     products_totals = response.data()
#     assert isinstance(products_totals, wc_collections.ReportProductTotalList)
#     assert products_totals_data[0]["id"] == products_totals.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("reports_customers_totals"))
# def test_get_reports_customers_totals():
#     recorded_response = _recfile("reports_customers_totals")
#     responses._add_from_file(file_path=recorded_response)
#     reports_customers_totals_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("reports/customers/totals")
#     customers_totals = response.data()
#     assert isinstance(customers_totals, wc_collections.ReportCustomerTotalList)
#     assert customers_totals_data[0]["id"] == customers_totals.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("reports_coupons_totals"))
# def test_get_reports_coupons_totals():
#     recorded_response = _recfile("reports_coupons_totals")
#     responses._add_from_file(file_path=recorded_response)
#     reports_coupons_totals_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("reports/coupons/totals")
#     coupons_totals = response.data()
#     assert isinstance(coupons_totals, wc_collections.ReportCouponTotalList)
#     assert coupons_totals_data[0]["id"] == coupons_totals.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("reports_reviews_totals"))
# def test_get_reports_reviews_totals():
#     recorded_response = _recfile("reports_reviews_totals")
#     responses._add_from_file(file_path=recorded_response)
#     reports_reviews_totals_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("reports/reviews/totals")
#     reviews_totals = response.data()
#     assert isinstance(reviews_totals, wc_collections.ReportReviewTotalList)
#     assert reviews_totals_data[0]["id"] == reviews_totals.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("reports"))
# def test_get_reports():
#     recorded_response = _recfile("reports")
#     responses._add_from_file(file_path=recorded_response)
#     reports_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("reports")
#     reports = response.data()
#     assert isinstance(reports, wc_collections.ReportList)
#     assert reports_data[0]["id"] == reports.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("shipping_zones"))
# def test_get_shipping_zones():
#     recorded_response = _recfile("shipping_zones")
#     responses._add_from_file(file_path=recorded_response)
#     shipping_zones_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("shipping/zones")
#     zones = response.data()
#     assert isinstance(zones, wc_collections.ShippingZoneList)
#     assert zones_data[0]["id"] == zones.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("shipping_zone"))
# def test_get_shipping_zone():
#     recorded_response = _recfile("shipping_zone")
#     responses._add_from_file(file_path=recorded_response)
#     shipping_zone_data = load_recorded_response_json(recorded_response)
#     zone_id = 12
#     response = wcapi.get(f"shipping/zones/{zone_id}")
#     zone = response.data()
#     assert isinstance(zone, wc_resources.ShippingZone)
#     assert zone_data["id"] == zone.id

# @responses.activate
# @_recorder.record(file_path=_recfile("shipping_zone_locations"))
# def test_get_shipping_zone_locations():
#     recorded_response = _recfile("shipping_zone_locations")
#     responses._add_from_file(file_path=recorded_response)
#     shipping_zone_locations_data = load_recorded_response_json(recorded_response)
#     zone_id = 12
#     response = wcapi.get(f"shipping/zones/{zone_id}/locations")
#     locations = response.data()
#     assert isinstance(locations, wc_collections.ShippingZoneLocationList)
#     assert locations_data[0]["id"] == locations.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("shipping_zone_methods"))
# def test_get_shipping_zone_methods():
#     recorded_response = _recfile("shipping_zone_methods")
#     responses._add_from_file(file_path=recorded_response)
#     shipping_zone_methods_data = load_recorded_response_json(recorded_response)
#     zone_id = 12
#     response = wcapi.get(f"shipping/zones/{zone_id}/methods")
#     methods = response.data()
#     assert isinstance(methods, wc_collections.ShippingZoneMethodList)
#     assert methods_data[0]["id"] == methods.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("shipping_zone_method"))
# def test_get_shipping_zone_method():
#     recorded_response = _recfile("shipping_zone_method")
#     responses._add_from_file(file_path=recorded_response)
#     shipping_zone_method_data = load_recorded_response_json(recorded_response)
#     zone_id = 123
#     instance_id = 45
#     response = wcapi.get(f"shipping/zones/{zone_id}/methods/{instance_id}")
#     method = response.data()
#     assert isinstance(method, wc_resources.ShippingZoneMethod)
#     assert method_data["id"] == method.id

# @responses.activate
# @_recorder.record(file_path=_recfile("taxes_classes"))
# def test_get_taxes_classes():
#     recorded_response = _recfile("taxes_classes")
#     responses._add_from_file(file_path=recorded_response)
#     taxes_classes_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("taxes/classes")
#     classes = response.data()
#     assert isinstance(classes, wc_collections.TaxClassList)
#     assert classes_data[0]["id"] == classes.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("taxes_class"))
# def test_get_taxes_class():
#     recorded_response = _recfile("taxes_class")
#     responses._add_from_file(file_path=recorded_response)
#     taxes_class_data = load_recorded_response_json(recorded_response)
#     slug = "standard
#     response = wcapi.get(f"taxes/classes/{slug}")
#     tax_class = response.data()
#     assert isinstance(tax_class, wc_resources.TaxClass)
#     assert class_data["slug"] == tax_class.slug

# @responses.activate
# @_recorder.record(file_path=_recfile("taxes"))
# def test_get_taxes():
#     recorded_response = _recfile("taxes")
#     responses._add_from_file(file_path=recorded_response)
#     taxes_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("taxes")
#     taxes = response.data()
#     assert isinstance(taxes, wc_collections.TaxList)
#     assert taxes_data[0]["id"] == taxes.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("tax"))
# def test_get_tax():
#     recorded_response = _recfile("tax")
#     responses._add_from_file(file_path=recorded_response)
#     tax_data = load_recorded_response_json(recorded_response)
#     tax_id = 12
#     response = wcapi.get(f"taxes/{tax_id}")
#     tax = response.data()
#     assert isinstance(tax, wc_resources.Tax)
#     assert tax_data["id"] == tax.id

# @responses.activate
# @_recorder.record(file_path=_recfile("webhooks"))
# def test_get_webhooks():
#     recorded_response = _recfile("webhooks")
#     responses._add_from_file(file_path=recorded_response)
#     webhooks_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("webhooks")
#     webhooks = response.data()
#     assert isinstance(webhooks, wc_collections.WebhookList)
#     assert webhooks_data[0]["id"] == webhooks.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("webhook"))
# def test_get_webhook():
#     recorded_response = _recfile("webhook")
#     responses._add_from_file(file_path=recorded_response)
#     webhook_data = load_recorded_response_json(recorded_response)
#     webhook_id = 12
#     response = wcapi.get(f"webhooks/{webhook_id}")
#     webhook = response.data()
#     assert isinstance(webhook, wc_resources.Webhook)
#     assert webhook_data["id"] == webhook.id

# @responses.activate
# @_recorder.record(file_path=_recfile("system_status"))
# def test_get_system_status():
#     recorded_response = _recfile("system_status")
#     responses._add_from_file(file_path=recorded_response)
#     system_status_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("system_status")
#     status = response.data()
#     assert isinstance(status, wc_resources.SystemStatus)
#     assert status_data["id"] == status.id

# @responses.activate
# @_recorder.record(file_path=_recfile("system_status_tools"))
# def test_get_system_status_tools():
#     recorded_response = _recfile("system_status_tools")
#     responses._add_from_file(file_path=recorded_response)
#     system_status_tools_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("system_status/tools")
#     tools = response.data()
#     assert isinstance(tools, wc_collections.SystemStatusToolList)
#     assert tools_data[0]["id"] == tools.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("system_status_tool"))
# def test_get_system_status_tool():
#     recorded_response = _recfile("system_status_tool")
#     responses._add_from_file(file_path=recorded_response)
#     system_status_tool_data = load_recorded_response_json(recorded_response)
#     tool_id = 12
#     response = wcapi.get(f"system_status/tools/{tool_id}")
#     tool = response.data()
#     assert isinstance(tool, wc_resources.SystemStatusTool)
#     assert tool_data["id"] == tool.id

# @responses.activate
# @_recorder.record(file_path=_recfile("shipping_methods"))
# def test_get_shipping_methods():
#     recorded_response = _recfile("shipping_methods")
#     responses._add_from_file(file_path=recorded_response)
#     shipping_methods_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("shipping_methods")
#     methods = response.data()
#     assert isinstance(methods, wc_collections.ShippingMethodList)
#     assert methods_data[0]["id"] == methods.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("shipping_method"))
# def test_get_shipping_method():
#     recorded_response = _recfile("shipping_method")
#     responses._add_from_file(file_path=recorded_response)
#     shipping_method_data = load_recorded_response_json(recorded_response)
#     method_id = 12
#     response = wcapi.get(f"shipping_methods/{method_id}")
#     method = response.data()
#     assert isinstance(method, wc_resources.ShippingMethod)
#     assert method_data["id"] == method.id

# @responses.activate
# @_recorder.record(file_path=_recfile("payment_gateways"))
# def test_get_payment_gateways():
#     recorded_response = _recfile("payment_gateways")
#     responses._add_from_file(file_path=recorded_response)
#     payment_gateways_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("payment_gateways")
#     gateways = response.data()
#     assert isinstance(gateways, wc_collections.PaymentGatewayList)
#     assert gateways_data[0]["id"] == gateways.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("payment_gateway"))
# def test_get_payment_gateway():
#     recorded_response = _recfile("payment_gateway")
#     responses._add_from_file(file_path=recorded_response)
#     payment_gateway_data = load_recorded_response_json(recorded_response)
#     gateway_id = 12
#     response = wcapi.get(f"payment_gateways/{gateway_id}")
#     gateway = response.data()
#     assert isinstance(gateway, wc_resources.PaymentGateway)
#     assert gateway_data["id"] == gateway.id

# @responses.activate
# @_recorder.record(file_path=_recfile("data"))
# def test_get_data():
#     recorded_response = _recfile("data")
#     responses._add_from_file(file_path=recorded_response)
#     data_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("data")
#     data_index = response.data()
#     assert isinstance(data_index, wc_resources.DataIndex)
#     assert data_index_data["id"] == data_index.id

# @responses.activate
# @_recorder.record(file_path=_recfile("data_continents"))
# def test_get_data_continents():
#     recorded_response = _recfile("data_continents")
#     responses._add_from_file(file_path=recorded_response)
#     data_continents_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("data/continents")
#     continents = response.data()
#     assert isinstance(continents, wc_collections.DataContinentsList)
#     assert continents_data[0]["id"] == continents.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("data_continent"))
# def test_get_data_continent():
#     recorded_response = _recfile("data_continent")
#     responses._add_from_file(file_path=recorded_response)
#     data_continent_data = load_recorded_response_json(recorded_response)
#     location = "EU
#     response = wcapi.get(f"data/continents/{location}")
#     continent = response.data()
#     assert isinstance(continent, wc_resources.DataContinents)
#     assert continent_data["location"] == continent.location

# @responses.activate
# @_recorder.record(file_path=_recfile("data_countries"))
# def test_get_data_countries():
#     recorded_response = _recfile("data_countries")
#     responses._add_from_file(file_path=recorded_response)
#     data_countries_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("data/countries")
#     countries = response.data()
#     assert isinstance(countries, wc_collections.DataCountriesList)
#     assert countries_data[0]["id"] == countries.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("data_country"))
# def test_get_data_country():
#     recorded_response = _recfile("data_country")
#     responses._add_from_file(file_path=recorded_response)
#     data_country_data = load_recorded_response_json(recorded_response)
#     location = "US
#     response = wcapi.get(f"data/countries/{location}")
#     country = response.data()
#     assert isinstance(country, wc_resources.DataCountries)
#     assert country_data["location"] == country.location

# @responses.activate
# @_recorder.record(file_path=_recfile("data_currencies"))
# def test_get_data_currencies():
#     recorded_response = _recfile("data_currencies")
#     responses._add_from_file(file_path=recorded_response)
#     data_currencies_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("data/currencies")
#     currencies = response.data()
#     assert isinstance(currencies, wc_collections.DataCurrenciesList)
#     assert currencies_data[0]["id"] == currencies.root[0].id

# @responses.activate
# @_recorder.record(file_path=_recfile("data_currency"))
# def test_get_data_currency():
#     recorded_response = _recfile("data_currency")
#     responses._add_from_file(file_path=recorded_response)
#     data_currency_data = load_recorded_response_json(recorded_response)
#     currency = "USD
#     response = wcapi.get(f"data/currencies/{currency}")
#     currency_obj = response.data()
#     assert isinstance(currency_obj, wc_resources.DataCurrencies)
#     assert currency_data["currency"] == currency_obj.currency

# @responses.activate
# @_recorder.record(file_path=_recfile("data_currencies_current"))
# def test_get_data_currencies_current():
#     recorded_response = _recfile("data_currencies_current")
#     responses._add_from_file(file_path=recorded_response)
#     data_currencies_current_data = load_recorded_response_json(recorded_response)
#     response = wcapi.get("data/currencies/current")
#     current_currency = response.data()
#     assert isinstance(current_currency, wc_resources.DataCurrencies)
#     assert current_currency_data["id"] == current_currency.id