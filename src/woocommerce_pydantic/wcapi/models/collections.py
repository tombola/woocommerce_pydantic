"""
Defines Pydantic response models for various WooCommerce API endpoints.

Attributes:
    response_models (dict): A dictionary mapping API endpoints to their
    corresponding response models.

"""

from pydantic import RootModel

from woocommerce_pydantic.wcapi.models import resources


class ShopCouponList(RootModel[list[resources.ShopCoupon]]):
    pass


class CustomerDownloadList(RootModel[list[resources.CustomerDownload]]):
    pass


class CustomerList(RootModel[list[resources.Customer]]):
    pass


class OrderNoteList(RootModel[list[resources.OrderNote]]):
    pass


class ShopOrderRefundList(RootModel[list[resources.ShopOrderRefund]]):
    pass


class ShopOrderList(RootModel[list[resources.ShopOrder]]):
    pass


class ProductAttributeTermList(RootModel[list[resources.ProductAttributeTerm]]):
    pass


class ProductAttributeList(RootModel[list[resources.ProductAttribute]]):
    pass


class ProductCatList(RootModel[list[resources.ProductCat]]):
    pass


class ProductReviewList(RootModel[list[resources.ProductReview]]):
    pass


class ProductShippingClassList(RootModel[list[resources.ProductShippingClass]]):
    pass


class ProductTagList(RootModel[list[resources.ProductTag]]):
    pass


class ProductList(RootModel[list[resources.Product]]):
    pass


class ProductVariationList(RootModel[list[resources.ProductVariation]]):
    pass


class SalesReportList(RootModel[list[resources.SalesReport]]):
    pass


class TopSellersReportList(RootModel[list[resources.TopSellersReport]]):
    pass


class ReportOrderTotalList(RootModel[list[resources.ReportOrderTotal]]):
    pass


class ReportProductTotalList(RootModel[list[resources.ReportProductTotal]]):
    pass


class ReportCustomerTotalList(RootModel[list[resources.ReportCustomerTotal]]):
    pass


class ReportCouponTotalList(RootModel[list[resources.ReportCouponTotal]]):
    pass


class ReportReviewTotalList(RootModel[list[resources.ReportReviewTotal]]):
    pass


class ReportList(RootModel[list[resources.Report]]):
    pass


class ShippingZoneList(RootModel[list[resources.ShippingZone]]):
    pass


class ShippingZoneLocationList(RootModel[list[resources.ShippingZoneLocation]]):
    pass


class ShippingZoneMethodList(RootModel[list[resources.ShippingZoneMethod]]):
    pass


class TaxClassList(RootModel[list[resources.TaxClass]]):
    pass


class TaxList(RootModel[list[resources.Tax]]):
    pass


class WebhookList(RootModel[list[resources.Webhook]]):
    pass


class SystemStatusToolList(RootModel[list[resources.SystemStatusTool]]):
    pass


class ShippingMethodList(RootModel[list[resources.ShippingMethod]]):
    pass


class PaymentGatewayList(RootModel[list[resources.PaymentGateway]]):
    pass


class DataContinentsList(RootModel[list[resources.DataContinents]]):
    pass


class DataCountriesList(RootModel[list[resources.DataCountries]]):
    pass


class DataCurrenciesList(RootModel[list[resources.DataCurrencies]]):
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
