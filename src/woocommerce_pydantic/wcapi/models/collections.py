"""
Defines Pydantic response models for various WooCommerce API endpoints.

Attributes:
    response_models (dict): A dictionary mapping API endpoints to their
    corresponding response models.

"""

from pydantic import RootModel

from woocommerce_pydantic.wcapi.models import resources


class WooCommerceCollection(RootModel):
    pass

class ShopCouponList(WooCommerceCollection[list[resources.ShopCoupon]]):
    pass


class CustomerDownloadList(WooCommerceCollection[list[resources.CustomerDownload]]):
    pass


class CustomerList(WooCommerceCollection[list[resources.Customer]]):
    pass


class OrderNoteList(WooCommerceCollection[list[resources.OrderNote]]):
    pass


class ShopOrderRefundList(WooCommerceCollection[list[resources.ShopOrderRefund]]):
    pass


class ShopOrderList(WooCommerceCollection[list[resources.ShopOrder]]):
    pass


class ProductAttributeTermList(WooCommerceCollection[list[resources.ProductAttributeTerm]]):
    pass


class ProductAttributeList(WooCommerceCollection[list[resources.ProductAttribute]]):
    pass


class ProductCatList(WooCommerceCollection[list[resources.ProductCat]]):
    pass


class ProductReviewList(WooCommerceCollection[list[resources.ProductReview]]):
    pass


class ProductShippingClassList(WooCommerceCollection[list[resources.ProductShippingClass]]):
    pass


class ProductTagList(WooCommerceCollection[list[resources.ProductTag]]):
    pass


class ProductList(WooCommerceCollection[list[resources.Product]]):
    pass


class ProductVariationList(WooCommerceCollection[list[resources.ProductVariation]]):
    pass


class SalesReportList(WooCommerceCollection[list[resources.SalesReport]]):
    pass


class TopSellersReportList(WooCommerceCollection[list[resources.TopSellersReport]]):
    pass


class ReportOrderTotalList(WooCommerceCollection[list[resources.ReportOrderTotal]]):
    pass


class ReportProductTotalList(WooCommerceCollection[list[resources.ReportProductTotal]]):
    pass


class ReportCustomerTotalList(WooCommerceCollection[list[resources.ReportCustomerTotal]]):
    pass


class ReportCouponTotalList(WooCommerceCollection[list[resources.ReportCouponTotal]]):
    pass


class ReportReviewTotalList(WooCommerceCollection[list[resources.ReportReviewTotal]]):
    pass


class ReportList(WooCommerceCollection[list[resources.Report]]):
    pass


class ShippingZoneList(WooCommerceCollection[list[resources.ShippingZone]]):
    pass


class ShippingZoneLocationList(WooCommerceCollection[list[resources.ShippingZoneLocation]]):
    pass


class ShippingZoneMethodList(WooCommerceCollection[list[resources.ShippingZoneMethod]]):
    pass


class TaxClassList(WooCommerceCollection[list[resources.TaxClass]]):
    pass


class TaxList(WooCommerceCollection[list[resources.Tax]]):
    pass


class WebhookList(WooCommerceCollection[list[resources.Webhook]]):
    pass


class SystemStatusToolList(WooCommerceCollection[list[resources.SystemStatusTool]]):
    pass


class ShippingMethodList(WooCommerceCollection[list[resources.ShippingMethod]]):
    pass


class PaymentGatewayList(WooCommerceCollection[list[resources.PaymentGateway]]):
    pass


class DataContinentsList(WooCommerceCollection[list[resources.DataContinents]]):
    pass


class DataCountriesList(WooCommerceCollection[list[resources.DataCountries]]):
    pass


class DataCurrenciesList(WooCommerceCollection[list[resources.DataCurrencies]]):
    pass


response_models = {
    "get": {
        "/coupons": ShopCouponList,
        "/coupons/{id}": resources.ShopCoupon,
        "/customers/{customer_id}/downloads": CustomerDownloadList,
        "/customers": CustomerList,
        "/customers/{id}": resources.Customer,
        "/orders/{order_id}/notes": OrderNoteList,
        "/orders/{order_id}/notes/{id}": resources.OrderNote,
        "/orders/{order_id}/refunds": ShopOrderRefundList,
        "/orders/{order_id}/refunds/{id}": resources.ShopOrderRefund,
        "/orders": ShopOrderList,
        "/orders/{id}": resources.ShopOrder,
        "/products/attributes/{attribute_id}/terms": ProductAttributeTermList,
        "/products/attributes/{attribute_id}/terms/{id}": resources.ProductAttributeTerm,
        "/products/attributes": ProductAttributeList,
        "/products/attributes/{id}": resources.ProductAttribute,
        "/products/categories": ProductCatList,
        "/products/categories/{id}": resources.ProductCat,
        "/products/reviews": ProductReviewList,
        "/products/reviews/{id}": resources.ProductReview,
        "/products/shipping_classes": ProductShippingClassList,
        "/products/shipping_classes/{id}": resources.ProductShippingClass,
        "/products/tags": ProductTagList,
        "/products/tags/{id}": resources.ProductTag,
        "/products": ProductList,
        "/products/{id}": resources.Product,
        "/products/{product_id}/variations": ProductVariationList,
        "/products/{product_id}/variations/{id}": resources.ProductVariation,
        "/reports/sales": SalesReportList,
        "/reports/top_sellers": TopSellersReportList,
        "/reports/orders/totals": ReportOrderTotalList,
        "/reports/products/totals": ReportProductTotalList,
        "/reports/customers/totals": ReportCustomerTotalList,
        "/reports/coupons/totals": ReportCouponTotalList,
        "/reports/reviews/totals": ReportReviewTotalList,
        "/reports": ReportList,
        "/shipping/zones": ShippingZoneList,
        "/shipping/zones/{id}": resources.ShippingZone,
        "/shipping/zones/{id}/locations": ShippingZoneLocationList,
        "/shipping/zones/{zone_id}/methods": ShippingZoneMethodList,
        "/shipping/zones/{zone_id}/methods/{instance_id}": resources.ShippingZoneMethod,
        "/taxes/classes": TaxClassList,
        "/taxes/classes/{slug}": resources.TaxClass,
        "/taxes": TaxList,
        "/taxes/{id}": resources.Tax,
        "/webhooks": WebhookList,
        "/webhooks/{id}": resources.Webhook,
        "/system_status": resources.SystemStatus,
        "/system_status/tools": SystemStatusToolList,
        "/system_status/tools/{id}": resources.SystemStatusTool,
        "/shipping_methods": ShippingMethodList,
        "/shipping_methods/{id}": resources.ShippingMethod,
        "/payment_gateways": PaymentGatewayList,
        "/payment_gateways/{id}": resources.PaymentGateway,
        "/data": resources.DataIndex,
        "/data/continents": DataContinentsList,
        "/data/continents/{location}": resources.DataContinents,
        "/data/countries": DataCountriesList,
        "/data/countries/{location}": resources.DataCountries,
        "/data/currencies": DataCurrenciesList,
        "/data/currencies/current": resources.DataCurrencies,
        "/data/currencies/{currency}": resources.DataCurrencies,
    },
}
