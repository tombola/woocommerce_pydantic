"""Defines Pydantic response models for WooCommerce API endpoints that return a list."""

from pydantic import RootModel

from woocommerce_pydantic.wcapi.models import wc_resources


class WooCommerceCollection(RootModel):
    pass

class ShopCouponList(WooCommerceCollection[list[wc_resources.ShopCoupon]]):
    pass


class CustomerDownloadList(WooCommerceCollection[list[wc_resources.CustomerDownload]]):
    pass


class CustomerList(WooCommerceCollection[list[wc_resources.Customer]]):
    pass


class OrderNoteList(WooCommerceCollection[list[wc_resources.OrderNote]]):
    pass


class ShopOrderRefundList(WooCommerceCollection[list[wc_resources.ShopOrderRefund]]):
    pass


class ShopOrderList(WooCommerceCollection[list[wc_resources.ShopOrder]]):
    pass


class ProductAttributeTermList(WooCommerceCollection[list[wc_resources.ProductAttributeTerm]]):
    pass


class ProductAttributeList(WooCommerceCollection[list[wc_resources.ProductAttribute]]):
    pass


class ProductCatList(WooCommerceCollection[list[wc_resources.ProductCat]]):
    pass


class ProductReviewList(WooCommerceCollection[list[wc_resources.ProductReview]]):
    pass


class ProductShippingClassList(WooCommerceCollection[list[wc_resources.ProductShippingClass]]):
    pass


class ProductTagList(WooCommerceCollection[list[wc_resources.ProductTag]]):
    pass


class ProductList(WooCommerceCollection[list[wc_resources.Product]]):
    pass


class ProductVariationList(WooCommerceCollection[list[wc_resources.ProductVariation]]):
    pass


class SalesReportList(WooCommerceCollection[list[wc_resources.SalesReport]]):
    pass


class TopSellersReportList(WooCommerceCollection[list[wc_resources.TopSellersReport]]):
    pass


class ReportOrderTotalList(WooCommerceCollection[list[wc_resources.ReportOrderTotal]]):
    pass


class ReportProductTotalList(WooCommerceCollection[list[wc_resources.ReportProductTotal]]):
    pass


class ReportCustomerTotalList(WooCommerceCollection[list[wc_resources.ReportCustomerTotal]]):
    pass


class ReportCouponTotalList(WooCommerceCollection[list[wc_resources.ReportCouponTotal]]):
    pass


class ReportReviewTotalList(WooCommerceCollection[list[wc_resources.ReportReviewTotal]]):
    pass


class ReportList(WooCommerceCollection[list[wc_resources.Report]]):
    pass


class ShippingZoneList(WooCommerceCollection[list[wc_resources.ShippingZone]]):
    pass


class ShippingZoneLocationList(WooCommerceCollection[list[wc_resources.ShippingZoneLocation]]):
    pass


class ShippingZoneMethodList(WooCommerceCollection[list[wc_resources.ShippingZoneMethod]]):
    pass


class TaxClassList(WooCommerceCollection[list[wc_resources.TaxClass]]):
    pass


class TaxList(WooCommerceCollection[list[wc_resources.Tax]]):
    pass


class WebhookList(WooCommerceCollection[list[wc_resources.Webhook]]):
    pass


class SystemStatusToolList(WooCommerceCollection[list[wc_resources.SystemStatusTool]]):
    pass


class ShippingMethodList(WooCommerceCollection[list[wc_resources.ShippingMethod]]):
    pass


class PaymentGatewayList(WooCommerceCollection[list[wc_resources.PaymentGateway]]):
    pass


class DataContinentsList(WooCommerceCollection[list[wc_resources.DataContinents]]):
    pass


class DataCountriesList(WooCommerceCollection[list[wc_resources.DataCountries]]):
    pass


class DataCurrenciesList(WooCommerceCollection[list[wc_resources.DataCurrencies]]):
    pass
