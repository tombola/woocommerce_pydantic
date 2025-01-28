"""
Defines Pydantic response models for various WooCommerce API endpoints.

Attributes:
    response_models (dict): A dictionary mapping API endpoints to their
    corresponding response models.

"""

from pydantic import BaseModel

from woocommerce_pydantic.wcapi.models import resources


class ShopCouponList(BaseModel):
    __root__: list[resources.ShopCoupon]


class CustomerDownloadList(BaseModel):
    __root__: list[resources.CustomerDownload]


class CustomerList(BaseModel):
    __root__: list[resources.Customer]


class OrderNoteList(BaseModel):
    __root__: list[resources.OrderNote]


class ShopOrderRefundList(BaseModel):
    __root__: list[resources.ShopOrderRefund]


class ShopOrderList(BaseModel):
    __root__: list[resources.ShopOrder]


class ProductAttributeTermList(BaseModel):
    __root__: list[resources.ProductAttributeTerm]


class ProductAttributeList(BaseModel):
    __root__: list[resources.ProductAttribute]


class ProductCatList(BaseModel):
    __root__: list[resources.ProductCat]


class ProductReviewList(BaseModel):
    __root__: list[resources.ProductReview]


class ProductShippingClassList(BaseModel):
    __root__: list[resources.ProductShippingClass]


class ProductTagList(BaseModel):
    __root__: list[resources.ProductTag]


class ProductList(BaseModel):
    __root__: list[resources.Product]


class ProductVariationList(BaseModel):
    __root__: list[resources.ProductVariation]


class SalesReportList(BaseModel):
    __root__: list[resources.SalesReport]


class TopSellersReportList(BaseModel):
    __root__: list[resources.TopSellersReport]


class ReportOrderTotalList(BaseModel):
    __root__: list[resources.ReportOrderTotal]


class ReportProductTotalList(BaseModel):
    __root__: list[resources.ReportProductTotal]


class ReportCustomerTotalList(BaseModel):
    __root__: list[resources.ReportCustomerTotal]


class ReportCouponTotalList(BaseModel):
    __root__: list[resources.ReportCouponTotal]


class ReportReviewTotalList(BaseModel):
    __root__: list[resources.ReportReviewTotal]


class ReportList(BaseModel):
    __root__: list[resources.Report]


class ShippingZoneList(BaseModel):
    __root__: list[resources.ShippingZone]


class ShippingZoneLocationList(BaseModel):
    __root__: list[resources.ShippingZoneLocation]


class ShippingZoneMethodList(BaseModel):
    __root__: list[resources.ShippingZoneMethod]


class TaxClassList(BaseModel):
    __root__: list[resources.TaxClass]


class TaxList(BaseModel):
    __root__: list[resources.Tax]


class WebhookList(BaseModel):
    __root__: list[resources.Webhook]


class SystemStatusToolList(BaseModel):
    __root__: list[resources.SystemStatusTool]


class ShippingMethodList(BaseModel):
    __root__: list[resources.ShippingMethod]


class PaymentGatewayList(BaseModel):
    __root__: list[resources.PaymentGateway]


class DataContinentsList(BaseModel):
    __root__: list[resources.DataContinents]


class DataCountriesList(BaseModel):
    __root__: list[resources.DataCountries]


class DataCurrenciesList(BaseModel):
    __root__: list[resources.DataCurrencies]


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
