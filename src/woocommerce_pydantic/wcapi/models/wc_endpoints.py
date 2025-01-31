"""Maps HTTP GET endpoints to their corresponding response models."""
from woocommerce_pydantic.wcapi.models import wc_collections, wc_resources
from urllib.parse import urlparse


RESPONSE_MODELS = {
    "get": {
        "/coupons": wc_collections.ShopCouponList,
        "/coupons/{id}": wc_resources.ShopCoupon,
        "/customers/{customer_id}/downloads": wc_collections.CustomerDownloadList,
        "/customers": wc_collections.CustomerList,
        "/customers/{id}": wc_resources.Customer,
        "/orders/{order_id}/notes": wc_collections.OrderNoteList,
        "/orders/{order_id}/notes/{id}": wc_resources.OrderNote,
        "/orders/{order_id}/refunds": wc_collections.ShopOrderRefundList,
        "/orders/{order_id}/refunds/{id}": wc_resources.ShopOrderRefund,
        "/orders": wc_collections.ShopOrderList,
        "/orders/{id}": wc_resources.ShopOrder,
        "/products/attributes/{attribute_id}/terms": wc_collections.ProductAttributeTermList,
        "/products/attributes/{attribute_id}/terms/{id}": wc_resources.ProductAttributeTerm,
        "/products/attributes": wc_collections.ProductAttributeList,
        "/products/attributes/{id}": wc_resources.ProductAttribute,
        "/products/categories": wc_collections.ProductCatList,
        "/products/categories/{id}": wc_resources.ProductCat,
        "/products/reviews": wc_collections.ProductReviewList,
        "/products/reviews/{id}": wc_resources.ProductReview,
        "/products/shipping_classes": wc_collections.ProductShippingClassList,
        "/products/shipping_classes/{id}": wc_resources.ProductShippingClass,
        "/products/tags": wc_collections.ProductTagList,
        "/products/tags/{id}": wc_resources.ProductTag,
        "/products": wc_collections.ProductList,
        "/products/{id}": wc_resources.Product,
        "/products/{product_id}/variations": wc_collections.ProductVariationList,
        "/products/{product_id}/variations/{id}": wc_resources.ProductVariation,
        "/reports/sales": wc_collections.SalesReportList,
        "/reports/top_sellers": wc_collections.TopSellersReportList,
        "/reports/orders/totals": wc_collections.ReportOrderTotalList,
        "/reports/products/totals": wc_collections.ReportProductTotalList,
        "/reports/customers/totals": wc_collections.ReportCustomerTotalList,
        "/reports/coupons/totals": wc_collections.ReportCouponTotalList,
        "/reports/reviews/totals": wc_collections.ReportReviewTotalList,
        "/reports": wc_collections.ReportList,
        "/shipping/zones": wc_collections.ShippingZoneList,
        "/shipping/zones/{id}": wc_resources.ShippingZone,
        "/shipping/zones/{id}/locations": wc_collections.ShippingZoneLocationList,
        "/shipping/zones/{zone_id}/methods": wc_collections.ShippingZoneMethodList,
        "/shipping/zones/{zone_id}/methods/{instance_id}": wc_resources.ShippingZoneMethod,
        "/taxes/classes": wc_collections.TaxClassList,
        "/taxes/classes/{slug}": wc_resources.TaxClass,
        "/taxes": wc_collections.TaxList,
        "/taxes/{id}": wc_resources.Tax,
        "/webhooks": wc_collections.WebhookList,
        "/webhooks/{id}": wc_resources.Webhook,
        "/system_status": wc_resources.SystemStatus,
        "/system_status/tools": wc_collections.SystemStatusToolList,
        "/system_status/tools/{id}": wc_resources.SystemStatusTool,
        "/shipping_methods": wc_collections.ShippingMethodList,
        "/shipping_methods/{id}": wc_resources.ShippingMethod,
        "/payment_gateways": wc_collections.PaymentGatewayList,
        "/payment_gateways/{id}": wc_resources.PaymentGateway,
        "/data": wc_resources.DataIndex,
        "/data/continents": wc_collections.DataContinentsList,
        "/data/continents/{location}": wc_resources.DataContinents,
        "/data/countries": wc_collections.DataCountriesList,
        "/data/countries/{location}": wc_resources.DataCountries,
        "/data/currencies": wc_collections.DataCurrenciesList,
        "/data/currencies/current": wc_resources.DataCurrencies,
        "/data/currencies/{currency}": wc_resources.DataCurrencies,
    },
}

def get_endpoint_components(url) -> list[str]:
    parsed_url = urlparse(url)
    path = parsed_url.path
    # Remove leading slash
    path = path.lstrip("/")
    components = path.split("/")
    # remove wp-json/wc/v3
    return components[3:]

def get_endpoint_model(url):
    parts = get_endpoint_components(url)
    match parts:
        case ["coupons"]:
            return wc_collections.ShopCouponList
        case ["coupons", id]:
            return wc_resources.ShopCoupon
        case ["customers", customer_id, "downloads"]:
            return wc_collections.CustomerDownloadList
        case ["customers"]:
            return wc_collections.CustomerList
        case ["customers", id]:
            return wc_resources.Customer
        case ["orders", order_id, "notes"]:
            return wc_collections.OrderNoteList
        case ["orders", order_id, "notes", id]:
            return wc_resources.OrderNote
        case ["orders", order_id, "refunds"]:
            return wc_collections.ShopOrderRefundList
        case ["orders", order_id, "refunds", id]:
            return wc_resources.ShopOrderRefund
        case ["orders"]:
            return wc_collections.ShopOrderList
        case ["orders", id]:
            return wc_resources.ShopOrder
        case ["products", "attributes", attribute_id, "terms"]:
            return wc_collections.ProductAttributeTermList
        case ["products", "attributes", attribute_id, "terms", id]:
            return wc_resources.ProductAttributeTerm
        case ["products", "attributes"]:
            return wc_collections.ProductAttributeList
        case ["products", "attributes", id]:
            return wc_resources.ProductAttribute
        case ["products", "categories"]:
            return wc_collections.ProductCatList
        case ["products", "categories", id]:
            return wc_resources.ProductCat
        case ["products", "reviews"]:
            return wc_collections.ProductReviewList
        case ["products", "reviews", id]:
            return wc_resources.ProductReview
        case ["products", "shipping_classes"]:
            return wc_collections.ProductShippingClassList
        case ["products", "shipping_classes", id]:
            return wc_resources.ProductShippingClass
        case ["products", "tags"]:
            return wc_collections.ProductTagList
        case ["products", "tags", id]:
            return wc_resources.ProductTag
        case ["products"]:
            return wc_collections.ProductList
        case ["products", id]:
            return wc_resources.Product
        case ["products", product_id, "variations"]:
            return wc_collections.ProductVariationList
        case ["products", product_id, "variations", id]:
            return wc_resources.ProductVariation
        case ["reports", "sales"]:
            return wc_collections.SalesReportList
        case ["reports", "top_sellers"]:
            return wc_collections.TopSellersReportList
        case ["reports", "orders", "totals"]:
            return wc_collections.ReportOrderTotalList
        case ["reports", "products", "totals"]:
            return wc_collections.ReportProductTotalList
        case ["reports", "customers", "totals"]:
            return wc_collections.ReportCustomerTotalList
        case ["reports", "coupons", "totals"]:
            return wc_collections.ReportCouponTotalList
        case ["reports", "reviews", "totals"]:
            return wc_collections.ReportReviewTotalList
        case ["reports"]:
            return wc_collections.ReportList
        case ["shipping", "zones"]:
            return wc_collections.ShippingZoneList
        case ["shipping", "zones", id]:
            return wc_resources.ShippingZone
        case ["shipping", "zones", id, "locations"]:
            return wc_collections.ShippingZoneLocationList
        case ["shipping", "zones", zone_id, "methods"]:
            return wc_collections.ShippingZoneMethodList
        case ["shipping", "zones", zone_id, "methods", instance_id]:
            return wc_resources.ShippingZoneMethod
        case ["taxes", "classes"]:
            return wc_collections.TaxClassList
        case ["taxes", "classes", slug]:
            return wc_resources.TaxClass
        case ["taxes"]:
            return wc_collections.TaxList
        case ["taxes", id]:
            return wc_resources.Tax
        case ["webhooks"]:
            return wc_collections.WebhookList
        case ["webhooks", id]:
            return wc_resources.Webhook
        case ["system_status"]:
            return wc_resources.SystemStatus
        case ["system_status", "tools"]:
            return wc_collections.SystemStatusToolList
        case ["system_status", "tools", id]:
            return wc_resources.SystemStatusTool
        case ["shipping_methods"]:
            return wc_collections.ShippingMethodList
        case ["shipping_methods", id]:
            return wc_resources.ShippingMethod
        case ["payment_gateways"]:
            return wc_collections.PaymentGatewayList
        case ["payment_gateways", id]:
            return wc_resources.PaymentGateway
        case ["data"]:
            return wc_resources.DataIndex
        case ["data", "continents"]:
            return wc_collections.DataContinentsList
        case ["data", "continents", location]:
            return wc_resources.DataContinents
        case ["data", "countries"]:
            return wc_collections.DataCountriesList
        case ["data", "countries", location]:
            return wc_resources.DataCountries
        case ["data", "currencies"]:
            return wc_collections.DataCurrenciesList
        case ["data", "currencies", "current"]:
            return wc_resources.DataCurrencies
        case ["data", "currencies", currency]:
            return wc_resources.DataCurrencies
        case _:
            return None
