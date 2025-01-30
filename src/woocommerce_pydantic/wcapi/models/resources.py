"""
Defines Pydantic models for WooCommerce data structures.

Initially based on results of datamodel-code-generator.
See https://github.com/tombola/generate_woo_pydantic

Since reformatted and updated for readability (PEP 604)
"""
from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import AnyUrl, BaseModel, EmailStr, Field


class WooCommerceResource(BaseModel):
    pass

class DiscountType(Enum):
    percent = "percent"
    fixed_cart = "fixed_cart"
    fixed_product = "fixed_product"


class MetaDatum(WooCommerceResource):
    id: int | None = Field(None, description="Meta ID.")
    key: str | None = Field(None, description="Meta key.")
    value: str | dict[str, Any] | None = Field(None, description="Meta value.")


class ShopCoupon(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the object.")
    code: str | None = Field(None, description="Coupon code.")
    amount: str | None = Field(
        None,
        description="The amount of discount. Should always be numeric, even if setting a percentage.",
    )
    date_created: str | None = Field(
        None,
        description="The date the coupon was created, in the site's timezone.",
    )
    date_created_gmt: str | None = Field(
        None,
        description="The date the coupon was created, as GMT.",
    )
    date_modified: str | None = Field(
        None,
        description="The date the coupon was last modified, in the site's timezone.",
    )
    date_modified_gmt: str | None = Field(
        None,
        description="The date the coupon was last modified, as GMT.",
    )
    discount_type: DiscountType | None = Field(
        None,
        description="Determines the type of discount that will be applied.",
    )
    description: str | None = Field(None, description="Coupon description.")
    date_expires: str | None = Field(
        None,
        description="The date the coupon expires, in the site's timezone.",
    )
    date_expires_gmt: str | None = Field(
        None,
        description="The date the coupon expires, as GMT.",
    )
    usage_count: int | None = Field(
        None,
        description="Number of times the coupon has been used already.",
    )
    individual_use: bool | None = Field(
        None,
        description="If true, the coupon can only be used individually. Other applied coupons will be removed from the cart.",
    )
    product_ids: list[int] | None = Field(
        None,
        description="List of product IDs the coupon can be used on.",
    )
    excluded_product_ids: list[int] | None = Field(
        None,
        description="List of product IDs the coupon cannot be used on.",
    )
    usage_limit: int | None = Field(
        None,
        description="How many times the coupon can be used in total.",
    )
    usage_limit_per_user: int | None = Field(
        None,
        description="How many times the coupon can be used per customer.",
    )
    limit_usage_to_x_items: int | None = Field(
        None,
        description="Max number of items in the cart the coupon can be applied to.",
    )
    free_shipping: bool | None = Field(
        None,
        description="If true and if the free shipping method requires a coupon, this coupon will enable free shipping.",
    )
    product_categories: list[int] | None = Field(
        None,
        description="List of category IDs the coupon applies to.",
    )
    excluded_product_categories: list[int] | None = Field(
        None,
        description="List of category IDs the coupon does not apply to.",
    )
    exclude_sale_items: bool | None = Field(
        None,
        description="If true, this coupon will not be applied to items that have sale prices.",
    )
    minimum_amount: str | None = Field(
        None,
        description="Minimum order amount that needs to be in the cart before coupon applies.",
    )
    maximum_amount: str | None = Field(
        None,
        description="Maximum order amount allowed when using the coupon.",
    )
    email_restrictions: list[str] | None = Field(
        None,
        description="List of email addresses that can use this coupon.",
    )
    used_by: list[int] | None = Field(
        None,
        description="List of user IDs (or guest email addresses) that have used the coupon.",
    )
    meta_data: list[MetaDatum] | None = Field(None, description="Meta data.")


class File(WooCommerceResource):
    name: str | None = Field(None, description="File name.")
    file: str | None = Field(None, description="File URL.")


class CustomerDownload(WooCommerceResource):
    download_id: str | None = Field(None, description="Download ID.")
    download_url: str | None = Field(None, description="Download file URL.")
    product_id: int | None = Field(None, description="Downloadable product ID.")
    product_name: str | None = Field(None, description="Product name.")
    download_name: str | None = Field(None, description="Downloadable file name.")
    order_id: int | None = Field(None, description="Order ID.")
    order_key: str | None = Field(None, description="Order key.")
    downloads_remaining: str | None = Field(
        None,
        description="Number of downloads remaining.",
    )
    access_expires: str | None = Field(
        None,
        description="The date when download access expires, in the site's timezone.",
    )
    access_expires_gmt: str | None = Field(
        None,
        description="The date when download access expires, as GMT.",
    )
    file: File | None = Field(None, description="File details.")


class Billing(WooCommerceResource):
    first_name: str | None = Field(None, description="First name.")
    last_name: str | None = Field(None, description="Last name.")
    company: str | None = Field(None, description="Company name.")
    address_1: str | None = Field(None, description="Address line 1")
    address_2: str | None = Field(None, description="Address line 2")
    city: str | None = Field(None, description="City name.")
    state: str | None = Field(
        None,
        description="ISO code or name of the state, province or district.",
    )
    postcode: str | None = Field(None, description="Postal code.")
    country: str | None = Field(None, description="ISO code of the country.")
    email: EmailStr | None = Field(None, description="Email address.")
    phone: str | None = Field(None, description="Phone number.")


class Shipping(WooCommerceResource):
    first_name: str | None = Field(None, description="First name.")
    last_name: str | None = Field(None, description="Last name.")
    company: str | None = Field(None, description="Company name.")
    address_1: str | None = Field(None, description="Address line 1")
    address_2: str | None = Field(None, description="Address line 2")
    city: str | None = Field(None, description="City name.")
    state: str | None = Field(
        None,
        description="ISO code or name of the state, province or district.",
    )
    postcode: str | None = Field(None, description="Postal code.")
    country: str | None = Field(None, description="ISO code of the country.")
    phone: str | None = Field(None, description="Phone number.")


class Customer(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    date_created: str | None = Field(
        None,
        description="The date the customer was created, in the site's timezone.",
    )
    date_created_gmt: str | None = Field(
        None,
        description="The date the customer was created, as GMT.",
    )
    date_modified: str | None = Field(
        None,
        description="The date the customer was last modified, in the site's timezone.",
    )
    date_modified_gmt: str | None = Field(
        None,
        description="The date the customer was last modified, as GMT.",
    )
    email: EmailStr | None = Field(
        None,
        description="The email address for the customer.",
    )
    first_name: str | None = Field(None, description="Customer first name.")
    last_name: str | None = Field(None, description="Customer last name.")
    role: str | None = Field(None, description="Customer role.")
    username: str | None = Field(None, description="Customer login name.")
    password: str | None = Field(None, description="Customer password.")
    billing: Billing | None = Field(
        None,
        description="List of billing address data.",
    )
    shipping: Shipping | None = Field(
        None,
        description="List of shipping address data.",
    )
    is_paying_customer: bool | None = Field(
        None,
        description="Is the customer a paying customer?",
    )
    avatar_url: str | None = Field(None, description="Avatar URL.")
    meta_data: list[MetaDatum] | None = Field(None, description="Meta data.")


class OrderNote(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    author: str | None = Field(None, description="Order note author.")
    date_created: str | None = Field(
        None,
        description="The date the order note was created, in the site's timezone.",
    )
    date_created_gmt: str | None = Field(
        None,
        description="The date the order note was created, as GMT.",
    )
    note: str | None = Field(None, description="Order note content.")
    customer_note: bool | None = Field(
        None,
        description="If true, the note will be shown to customers and they will be notified. If false, the note will be for admin reference only.",
    )
    added_by_user: bool | None = Field(
        None,
        description="If true, this note will be attributed to the current user. If false, the note will be attributed to the system.",
    )


class Tax(WooCommerceResource):
    id: int | None = Field(None, description="Tax rate ID.")
    total: str | None = Field(None, description="Tax total.")
    subtotal: str | None = Field(None, description="Tax subtotal.")
    refund_total: float | None = Field(
        None,
        description="Amount that will be refunded for this tax.",
    )


class LineItem(WooCommerceResource):
    id: int | None = Field(None, description="Item ID.")
    name: str | None = Field(None, description="Product name.")
    product_id: int | None = Field(None, description="Product ID.")
    variation_id: int | None = Field(
        None,
        description="Variation ID, if applicable.",
    )
    quantity: int | None = Field(None, description="Quantity ordered.")
    tax_class: str | None = Field(None, description="Tax class of product.")
    subtotal: str | None = Field(
        None,
        description="Line subtotal (before discounts).",
    )
    subtotal_tax: str | None = Field(
        None,
        description="Line subtotal tax (before discounts).",
    )
    total: str | None = Field(None, description="Line total (after discounts).")
    total_tax: str | None = Field(
        None,
        description="Line total tax (after discounts).",
    )
    taxes: list[Tax] | None = Field(None, description="Line taxes.")
    meta_data: list[MetaDatum] | None = Field(None, description="Meta data.")
    sku: str | None = Field(None, description="Product SKU.")
    price: float | None = Field(None, description="Product price.")
    refund_total: float | None = Field(
        None,
        description="Amount that will be refunded for this line item (excluding taxes).",
    )


class ShopOrderRefund(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    date_created: str | None = Field(
        None,
        description="The date the order refund was created, in the site's timezone.",
    )
    date_created_gmt: str | None = Field(
        None,
        description="The date the order refund was created, as GMT.",
    )
    amount: str | None = Field(None, description="Refund amount.")
    reason: str | None = Field(None, description="Reason for refund.")
    refunded_by: int | None = Field(
        None,
        description="User ID of user who created the refund.",
    )
    refunded_payment: bool | None = Field(
        None,
        description="If the payment was refunded via the API.",
    )
    meta_data: list[MetaDatum] | None = Field(None, description="Meta data.")
    line_items: list[LineItem] | None = Field(None, description="Line items data.")
    api_refund: bool | None = Field(
        None,
        description="When true, the payment gateway API is used to generate the refund.",
    )
    api_restock: bool | None = Field(
        None,
        description="When true, refunded items are restocked.",
    )


class Status(Enum):
    pending = "pending"
    processing = "processing"
    on_hold = "on-hold"
    completed = "completed"
    cancelled = "cancelled"
    refunded = "refunded"
    failed = "failed"


class Currency(Enum):
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BRL = "BRL"
    BSD = "BSD"
    BTC = "BTC"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BYN = "BYN"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GGP = "GGP"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    IMP = "IMP"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    IRT = "IRT"
    ISK = "ISK"
    JEP = "JEP"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRU = "MRU"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PRB = "PRB"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STN = "STN"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VES = "VES"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XCD = "XCD"
    XOF = "XOF"
    XPF = "XPF"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"


class Billing1(WooCommerceResource):
    first_name: str | None = Field(None, description="First name.")
    last_name: str | None = Field(None, description="Last name.")
    company: str | None = Field(None, description="Company name.")
    address_1: str | None = Field(None, description="Address line 1")
    address_2: str | None = Field(None, description="Address line 2")
    city: str | None = Field(None, description="City name.")
    state: str | None = Field(
        None,
        description="ISO code or name of the state, province or district.",
    )
    postcode: str | None = Field(None, description="Postal code.")
    country: str | None = Field(
        None,
        description="Country code in ISO 3166-1 alpha-2 format.",
    )
    email: EmailStr | None = Field(None, description="Email address.")
    phone: str | None = Field(None, description="Phone number.")


class Shipping1(WooCommerceResource):
    first_name: str | None = Field(None, description="First name.")
    last_name: str | None = Field(None, description="Last name.")
    company: str | None = Field(None, description="Company name.")
    address_1: str | None = Field(None, description="Address line 1")
    address_2: str | None = Field(None, description="Address line 2")
    city: str | None = Field(None, description="City name.")
    state: str | None = Field(
        None,
        description="ISO code or name of the state, province or district.",
    )
    postcode: str | None = Field(None, description="Postal code.")
    country: str | None = Field(
        None,
        description="Country code in ISO 3166-1 alpha-2 format.",
    )


class Tax1(WooCommerceResource):
    id: int | None = Field(None, description="Tax rate ID.")
    total: str | None = Field(None, description="Tax total.")
    subtotal: str | None = Field(None, description="Tax subtotal.")


class MetaDatum5(WooCommerceResource):
    id: int | None = Field(None, description="Meta ID.")
    key: str | None = Field(None, description="Meta key.")
    value: str | dict[str, Any] | None = Field(None, description="Meta value.")
    display_key: str | None = Field(None, description="Meta key for UI display.")
    display_value: str | None = Field(None, description="Meta value for UI display.")


class LineItem1(WooCommerceResource):
    id: int | None = Field(None, description="Item ID.")
    name: str | None = Field(None, description="Product name.")
    parent_name: str | None = Field(
        None,
        description="Parent product name if the product is a variation.",
    )
    product_id: int | None = Field(None, description="Product ID.")
    variation_id: int | None = Field(
        None,
        description="Variation ID, if applicable.",
    )
    quantity: int | None = Field(None, description="Quantity ordered.")
    tax_class: str | None = Field(None, description="Tax class of product.")
    subtotal: str | None = Field(
        None,
        description="Line subtotal (before discounts).",
    )
    subtotal_tax: str | None = Field(
        None,
        description="Line subtotal tax (before discounts).",
    )
    total: str | None = Field(None, description="Line total (after discounts).")
    total_tax: str | None = Field(
        None,
        description="Line total tax (after discounts).",
    )
    taxes: list[Tax1] | None = Field(None, description="Line taxes.")
    meta_data: list[MetaDatum5] | None = Field(None, description="Meta data.")
    sku: str | None = Field(None, description="Product SKU.")
    price: float | None = Field(None, description="Product price.")


class MetaDatum6(WooCommerceResource):
    id: int | None = Field(None, description="Meta ID.")
    key: str | None = Field(None, description="Meta key.")
    value: str | dict[str, Any] | None = Field(None, description="Meta value.")


class TaxLine(WooCommerceResource):
    id: int | None = Field(None, description="Item ID.")
    rate_code: str | None = Field(None, description="Tax rate code.")
    rate_id: int | None = Field(None, description="Tax rate ID.")
    label: str | None = Field(None, description="Tax rate label.")
    compound: bool | None = Field(
        None,
        description="Show if is a compound tax rate.",
    )
    tax_total: str | None = Field(
        None,
        description="Tax total (not including shipping taxes).",
    )
    shipping_tax_total: str | None = Field(None, description="Shipping tax total.")
    meta_data: list[MetaDatum6] | None = Field(None, description="Meta data.")


class Tax2(WooCommerceResource):
    id: int | None = Field(None, description="Tax rate ID.")
    total: str | None = Field(None, description="Tax total.")


class ShippingLine(WooCommerceResource):
    id: int | None = Field(None, description="Item ID.")
    method_title: str | None = Field(None, description="Shipping method name.")
    method_id: str | None = Field(None, description="Shipping method ID.")
    instance_id: str | None = Field(None, description="Shipping instance ID.")
    total: str | None = Field(None, description="Line total (after discounts).")
    total_tax: str | None = Field(
        None,
        description="Line total tax (after discounts).",
    )
    taxes: list[Tax2] | None = Field(None, description="Line taxes.")
    meta_data: list[MetaDatum6] | None = Field(None, description="Meta data.")


class TaxStatus(Enum):
    taxable = "taxable"
    none = "none"


class Tax3(WooCommerceResource):
    id: int | None = Field(None, description="Tax rate ID.")
    total: str | None = Field(None, description="Tax total.")
    subtotal: str | None = Field(None, description="Tax subtotal.")


class FeeLine(WooCommerceResource):
    id: int | None = Field(None, description="Item ID.")
    name: str | None = Field(None, description="Fee name.")
    tax_class: str | None = Field(None, description="Tax class of fee.")
    tax_status: TaxStatus | None = Field(None, description="Tax status of fee.")
    total: str | None = Field(None, description="Line total (after discounts).")
    total_tax: str | None = Field(
        None,
        description="Line total tax (after discounts).",
    )
    taxes: list[Tax3] | None = Field(None, description="Line taxes.")
    meta_data: list[MetaDatum6] | None = Field(None, description="Meta data.")


class CouponLine(WooCommerceResource):
    id: int | None = Field(None, description="Item ID.")
    code: str | None = Field(None, description="Coupon code.")
    discount: str | None = Field(None, description="Discount total.")
    discount_tax: str | None = Field(None, description="Discount total tax.")
    meta_data: list[MetaDatum6] | None = Field(None, description="Meta data.")


class Refund(WooCommerceResource):
    id: int | None = Field(None, description="Refund ID.")
    reason: str | None = Field(None, description="Refund reason.")
    total: str | None = Field(None, description="Refund total.")


class ShopOrder(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    parent_id: int | None = Field(None, description="Parent order ID.")
    number: str | None = Field(None, description="Order number.")
    order_key: str | None = Field(None, description="Order key.")
    created_via: str | None = Field(
        None,
        description="Shows where the order was created.",
    )
    version: str | None = Field(
        None,
        description="Version of WooCommerce which last updated the order.",
    )
    status: Status | None = Field(None, description="Order status.")
    currency: Currency | None = Field(
        None,
        description="Currency the order was created with, in ISO format.",
    )
    date_created: str | None = Field(
        None,
        description="The date the order was created, in the site's timezone.",
    )
    date_created_gmt: str | None = Field(
        None,
        description="The date the order was created, as GMT.",
    )
    date_modified: str | None = Field(
        None,
        description="The date the order was last modified, in the site's timezone.",
    )
    date_modified_gmt: str | None = Field(
        None,
        description="The date the order was last modified, as GMT.",
    )
    discount_total: str | None = Field(
        None,
        description="Total discount amount for the order.",
    )
    discount_tax: str | None = Field(
        None,
        description="Total discount tax amount for the order.",
    )
    shipping_total: str | None = Field(
        None,
        description="Total shipping amount for the order.",
    )
    shipping_tax: str | None = Field(
        None,
        description="Total shipping tax amount for the order.",
    )
    cart_tax: str | None = Field(None, description="Sum of line item taxes only.")
    total: str | None = Field(None, description="Grand total.")
    total_tax: str | None = Field(None, description="Sum of all taxes.")
    prices_include_tax: bool | None = Field(
        None,
        description="True the prices included tax during checkout.",
    )
    customer_id: int | None = Field(
        None,
        description="User ID who owns the order. 0 for guests.",
    )
    customer_ip_address: str | None = Field(
        None,
        description="Customer's IP address.",
    )
    customer_user_agent: str | None = Field(
        None,
        description="User agent of the customer.",
    )
    customer_note: str | None = Field(
        None,
        description="Note left by customer during checkout.",
    )
    billing: Billing1 | None = Field(None, description="Billing address.")
    shipping: Shipping1 | None = Field(None, description="Shipping address.")
    payment_method: str | None = Field(None, description="Payment method ID.")
    payment_method_title: str | None = Field(
        None,
        description="Payment method title.",
    )
    transaction_id: str | None = Field(None, description="Unique transaction ID.")
    date_paid: str | None = Field(
        None,
        description="The date the order was paid, in the site's timezone.",
    )
    date_paid_gmt: str | None = Field(
        None,
        description="The date the order was paid, as GMT.",
    )
    date_completed: str | None = Field(
        None,
        description="The date the order was completed, in the site's timezone.",
    )
    date_completed_gmt: str | None = Field(
        None,
        description="The date the order was completed, as GMT.",
    )
    cart_hash: str | None = Field(
        None,
        description="MD5 hash of cart items to ensure orders are not modified.",
    )
    meta_data: list[MetaDatum] | None = Field(None, description="Meta data.")
    line_items: list[LineItem1] | None = Field(None, description="Line items data.")
    tax_lines: list[TaxLine] | None = Field(None, description="Tax lines data.")
    shipping_lines: list[ShippingLine] | None = Field(
        None,
        description="Shipping lines data.",
    )
    fee_lines: list[FeeLine] | None = Field(None, description="Fee lines data.")
    coupon_lines: list[CouponLine] | None = Field(
        None,
        description="Coupons line data.",
    )
    refunds: list[Refund] | None = Field(None, description="List of refunds.")
    set_paid: bool | None = Field(
        None,
        description="Define if the order is paid. It will set the status to processing and reduce stock items.",
    )


class ProductAttributeTerm(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    name: str | None = Field(None, description="Term name.")
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource unique to its type.",
    )
    description: str | None = Field(
        None,
        description="HTML description of the resource.",
    )
    menu_order: int | None = Field(
        None,
        description="Menu order, used to custom sort the resource.",
    )
    count: int | None = Field(
        None,
        description="Number of published products for the resource.",
    )


class Type(Enum):
    select = "select"


class OrderBy(Enum):
    menu_order = "menu_order"
    name = "name"
    name_num = "name_num"
    id = "id"


class ProductAttribute(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    name: str | None = Field(None, description="Attribute name.")
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource unique to its type.",
    )
    type: Type | None = Field(None, description="Type of attribute.")
    order_by: OrderBy | None = Field(None, description="Default sort order.")
    has_archives: bool | None = Field(
        None,
        description="Enable/Disable attribute archives.",
    )


class Display(Enum):
    default = "default"
    products = "products"
    subcategories = "subcategories"
    both = "both"


class Image(WooCommerceResource):
    id: int | None = Field(None, description="Image ID.")
    date_created: str | None = Field(
        None,
        description="The date the image was created, in the site's timezone.",
    )
    date_created_gmt: str | None = Field(
        None,
        description="The date the image was created, as GMT.",
    )
    date_modified: str | None = Field(
        None,
        description="The date the image was last modified, in the site's timezone.",
    )
    date_modified_gmt: str | None = Field(
        None,
        description="The date the image was last modified, as GMT.",
    )
    src: AnyUrl | None = Field(None, description="Image URL.")
    name: str | None = Field(None, description="Image name.")
    alt: str | None = Field(None, description="Image alternative text.")


class ProductCat(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    name: str | None = Field(None, description="Category name.")
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource unique to its type.",
    )
    parent: int | None = Field(
        None,
        description="The ID for the parent of the resource.",
    )
    description: str | None = Field(
        None,
        description="HTML description of the resource.",
    )
    display: Display | None = Field(
        None,
        description="Category archive display type.",
    )
    image: Image | None = Field(None, description="Image data.")
    menu_order: int | None = Field(
        None,
        description="Menu order, used to custom sort the resource.",
    )
    count: int | None = Field(
        None,
        description="Number of published products for the resource.",
    )


class Status1(Enum):
    approved = "approved"
    hold = "hold"
    spam = "spam"
    unspam = "unspam"
    trash = "trash"
    untrash = "untrash"


class ReviewerAvatarUrls(WooCommerceResource):
    field_24: AnyUrl | None = Field(
        None,
        alias="24",
        description="Avatar URL with image size of 24 pixels.",
    )
    field_48: AnyUrl | None = Field(
        None,
        alias="48",
        description="Avatar URL with image size of 48 pixels.",
    )
    field_96: AnyUrl | None = Field(
        None,
        alias="96",
        description="Avatar URL with image size of 96 pixels.",
    )


class ProductReview(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    date_created: str | None = Field(
        None,
        description="The date the review was created, in the site's timezone.",
    )
    date_created_gmt: str | None = Field(
        None,
        description="The date the review was created, as GMT.",
    )
    product_id: int | None = Field(
        None,
        description="Unique identifier for the product that the review belongs to.",
    )
    status: Status1 | None = Field(None, description="Status of the review.")
    reviewer: str | None = Field(None, description="Reviewer name.")
    reviewer_email: EmailStr | None = Field(None, description="Reviewer email.")
    review: str | None = Field(None, description="The content of the review.")
    rating: int | None = Field(None, description="Review rating (0 to 5).")
    verified: bool | None = Field(
        None,
        description="Shows if the reviewer bought the product or not.",
    )
    reviewer_avatar_urls: ReviewerAvatarUrls | None = Field(
        None,
        description="Avatar URLs for the object reviewer.",
    )


class ProductShippingClass(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    name: str | None = Field(None, description="Shipping class name.")
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource unique to its type.",
    )
    description: str | None = Field(
        None,
        description="HTML description of the resource.",
    )
    count: int | None = Field(
        None,
        description="Number of published products for the resource.",
    )


class ProductTag(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    name: str | None = Field(None, description="Tag name.")
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource unique to its type.",
    )
    description: str | None = Field(
        None,
        description="HTML description of the resource.",
    )
    count: int | None = Field(
        None,
        description="Number of published products for the resource.",
    )


class Type1(Enum):
    simple = "simple"
    grouped = "grouped"
    external = "external"
    variable = "variable"


class Status2(Enum):
    draft = "draft"
    pending = "pending"
    private = "private"
    publish = "publish"
    future = "future"


class CatalogVisibility(Enum):
    visible = "visible"
    catalog = "catalog"
    search = "search"
    hidden = "hidden"


class Download(WooCommerceResource):
    id: str | None = Field(None, description="File ID.")
    name: str | None = Field(None, description="File name.")
    file: str | None = Field(None, description="File URL.")


class TaxStatus1(Enum):
    taxable = "taxable"
    shipping = "shipping"
    none = "none"


class StockStatus(Enum):
    instock = "instock"
    outofstock = "outofstock"
    onbackorder = "onbackorder"


class Backorders(Enum):
    no = "no"
    notify = "notify"
    yes = "yes"


class Dimensions(WooCommerceResource):
    length: str | None = Field(None, description="Product length (cm).")
    width: str | None = Field(None, description="Product width (cm).")
    height: str | None = Field(None, description="Product height (cm).")


class Category(WooCommerceResource):
    id: int | None = Field(None, description="Category ID.")
    name: str | None = Field(None, description="Category name.")
    slug: str | None = Field(None, description="Category slug.")


class Tag(WooCommerceResource):
    id: int | None = Field(None, description="Tag ID.")
    name: str | None = Field(None, description="Tag name.")
    slug: str | None = Field(None, description="Tag slug.")


class Attribute(WooCommerceResource):
    id: int | None = Field(None, description="Attribute ID.")
    name: str | None = Field(None, description="Attribute name.")
    position: int | None = Field(None, description="Attribute position.")
    visible: bool | None = Field(
        None,
        description='Define if the attribute is visible on the "Additional information" tab in the product\'s page.',
    )
    variation: bool | None = Field(
        None,
        description="Define if the attribute can be used as variation.",
    )
    options: list[str] | None = Field(
        None,
        description="List of available term names of the attribute.",
    )


class DefaultAttribute(WooCommerceResource):
    id: int | None = Field(None, description="Attribute ID.")
    name: str | None = Field(None, description="Attribute name.")
    option: str | None = Field(None, description="Selected attribute term name.")


class Product(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    name: str | None = Field(None, description="Product name.")
    slug: str | None = Field(None, description="Product slug.")
    permalink: AnyUrl | None = Field(None, description="Product URL.")
    date_created: str | None = Field(
        None,
        description="The date the product was created, in the site's timezone.",
    )
    date_created_gmt: str | None = Field(
        None,
        description="The date the product was created, as GMT.",
    )
    date_modified: str | None = Field(
        None,
        description="The date the product was last modified, in the site's timezone.",
    )
    date_modified_gmt: str | None = Field(
        None,
        description="The date the product was last modified, as GMT.",
    )
    type: Type1 | None = Field(None, description="Product type.")
    status: Status2 | None = Field(None, description="Product status (post status).")
    featured: bool | None = Field(None, description="Featured product.")
    catalog_visibility: CatalogVisibility | None = Field(
        None,
        description="Catalog visibility.",
    )
    description: str | None = Field(None, description="Product description.")
    short_description: str | None = Field(
        None,
        description="Product short description.",
    )
    sku: str | None = Field(None, description="Unique identifier.")
    price: str | None = Field(None, description="Current product price.")
    regular_price: str | None = Field(None, description="Product regular price.")
    sale_price: str | None = Field(None, description="Product sale price.")
    date_on_sale_from: str | None = Field(
        None,
        description="Start date of sale price, in the site's timezone.",
    )
    date_on_sale_from_gmt: str | None = Field(
        None,
        description="Start date of sale price, as GMT.",
    )
    date_on_sale_to: str | None = Field(
        None,
        description="End date of sale price, in the site's timezone.",
    )
    date_on_sale_to_gmt: str | None = Field(
        None,
        description="End date of sale price, in the site's timezone.",
    )
    price_html: str | None = Field(None, description="Price formatted in HTML.")
    on_sale: bool | None = Field(
        None,
        description="Shows if the product is on sale.",
    )
    purchasable: bool | None = Field(
        None,
        description="Shows if the product can be bought.",
    )
    total_sales: int | None = Field(None, description="Amount of sales.")
    virtual: bool | None = Field(None, description="If the product is virtual.")
    downloadable: bool | None = Field(
        None,
        description="If the product is downloadable.",
    )
    downloads: list[Download] | None = Field(
        None,
        description="List of downloadable files.",
    )
    download_limit: int | None = Field(
        None,
        description="Number of times downloadable files can be downloaded after purchase.",
    )
    download_expiry: int | None = Field(
        None,
        description="Number of days until access to downloadable files expires.",
    )
    external_url: AnyUrl | None = Field(
        None,
        description="Product external URL. Only for external products.",
    )
    button_text: str | None = Field(
        None,
        description="Product external button text. Only for external products.",
    )
    tax_status: TaxStatus1 | None = Field(None, description="Tax status.")
    tax_class: str | None = Field(None, description="Tax class.")
    manage_stock: bool | None = Field(
        None,
        description="Stock management at product level.",
    )
    stock_quantity: int | None = Field(None, description="Stock quantity.")
    stock_status: StockStatus | None = Field(
        None,
        description="Controls the stock status of the product.",
    )
    backorders: Backorders | None = Field(
        None,
        description="If managing stock, this controls if backorders are allowed.",
    )
    backorders_allowed: bool | None = Field(
        None,
        description="Shows if backorders are allowed.",
    )
    backordered: bool | None = Field(
        None,
        description="Shows if the product is on backordered.",
    )
    low_stock_amount: int | None = Field(
        None,
        description="Low Stock amount for the product.",
    )
    sold_individually: bool | None = Field(
        None,
        description="Allow one item to be bought in a single order.",
    )
    weight: str | None = Field(None, description="Product weight (kg).")
    dimensions: Dimensions | None = Field(None, description="Product dimensions.")
    shipping_required: bool | None = Field(
        None,
        description="Shows if the product need to be shipped.",
    )
    shipping_taxable: bool | None = Field(
        None,
        description="Shows whether or not the product shipping is taxable.",
    )
    shipping_class: str | None = Field(None, description="Shipping class slug.")
    shipping_class_id: str | None = Field(None, description="Shipping class ID.")
    reviews_allowed: bool | None = Field(None, description="Allow reviews.")
    average_rating: str | None = Field(None, description="Reviews average rating.")
    rating_count: int | None = Field(
        None,
        description="Amount of reviews that the product have.",
    )
    related_ids: list[int] | None = Field(
        None,
        description="List of related products IDs.",
    )
    upsell_ids: list[int] | None = Field(
        None,
        description="List of up-sell products IDs.",
    )
    cross_sell_ids: list[int] | None = Field(
        None,
        description="List of cross-sell products IDs.",
    )
    parent_id: int | None = Field(None, description="Product parent ID.")
    purchase_note: str | None = Field(
        None,
        description="Optional note to send the customer after purchase.",
    )
    categories: list[Category] | None = Field(
        None,
        description="List of categories.",
    )
    tags: list[Tag] | None = Field(None, description="List of tags.")
    images: list[Image] | None = Field(None, description="List of images.")
    attributes: list[Attribute] | None = Field(
        None,
        description="List of attributes.",
    )
    default_attributes: list[DefaultAttribute] | None = Field(
        None,
        description="Defaults variation attributes.",
    )
    variations: list[int] | None = Field(None, description="List of variations IDs.")
    grouped_products: list[int] | None = Field(
        None,
        description="List of grouped products ID.",
    )
    menu_order: int | None = Field(
        None,
        description="Menu order, used to custom sort products.",
    )
    meta_data: list[MetaDatum6] | None = Field(None, description="Meta data.")


class Status3(Enum):
    draft = "draft"
    pending = "pending"
    private = "private"
    publish = "publish"


class Dimensions1(WooCommerceResource):
    length: str | None = Field(None, description="Variation length (cm).")
    width: str | None = Field(None, description="Variation width (cm).")
    height: str | None = Field(None, description="Variation height (cm).")


class Attribute1(WooCommerceResource):
    id: int | None = Field(None, description="Attribute ID.")
    name: str | None = Field(None, description="Attribute name.")
    option: str | None = Field(None, description="Selected attribute term name.")


class ProductVariation(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    date_created: str | None = Field(
        None,
        description="The date the variation was created, in the site's timezone.",
    )
    date_modified: str | None = Field(
        None,
        description="The date the variation was last modified, in the site's timezone.",
    )
    description: str | None = Field(None, description="Variation description.")
    permalink: AnyUrl | None = Field(None, description="Variation URL.")
    sku: str | None = Field(None, description="Unique identifier.")
    price: str | None = Field(None, description="Current variation price.")
    regular_price: str | None = Field(None, description="Variation regular price.")
    sale_price: str | None = Field(None, description="Variation sale price.")
    date_on_sale_from: str | None = Field(
        None,
        description="Start date of sale price, in the site's timezone.",
    )
    date_on_sale_from_gmt: str | None = Field(
        None,
        description="Start date of sale price, as GMT.",
    )
    date_on_sale_to: str | None = Field(
        None,
        description="End date of sale price, in the site's timezone.",
    )
    date_on_sale_to_gmt: str | None = Field(
        None,
        description="End date of sale price, in the site's timezone.",
    )
    on_sale: bool | None = Field(
        None,
        description="Shows if the variation is on sale.",
    )
    status: Status3 | None = Field(None, description="Variation status.")
    purchasable: bool | None = Field(
        None,
        description="Shows if the variation can be bought.",
    )
    virtual: bool | None = Field(None, description="If the variation is virtual.")
    downloadable: bool | None = Field(
        None,
        description="If the variation is downloadable.",
    )
    downloads: list[Download] | None = Field(
        None,
        description="List of downloadable files.",
    )
    download_limit: int | None = Field(
        None,
        description="Number of times downloadable files can be downloaded after purchase.",
    )
    download_expiry: int | None = Field(
        None,
        description="Number of days until access to downloadable files expires.",
    )
    tax_status: TaxStatus1 | None = Field(None, description="Tax status.")
    tax_class: str | None = Field(None, description="Tax class.")
    manage_stock: bool | None = Field(
        None,
        description="Stock management at variation level.",
    )
    stock_quantity: int | None = Field(None, description="Stock quantity.")
    stock_status: StockStatus | None = Field(
        None,
        description="Controls the stock status of the product.",
    )
    backorders: Backorders | None = Field(
        None,
        description="If managing stock, this controls if backorders are allowed.",
    )
    backorders_allowed: bool | None = Field(
        None,
        description="Shows if backorders are allowed.",
    )
    backordered: bool | None = Field(
        None,
        description="Shows if the variation is on backordered.",
    )
    low_stock_amount: int | None = Field(
        None,
        description="Low Stock amount for the variation.",
    )
    weight: str | None = Field(None, description="Variation weight (kg).")
    dimensions: Dimensions1 | None = Field(None, description="Variation dimensions.")
    shipping_class: str | None = Field(None, description="Shipping class slug.")
    shipping_class_id: str | None = Field(None, description="Shipping class ID.")
    image: Image | None = Field(None, description="Variation image data.")
    attributes: list[Attribute1] | None = Field(
        None,
        description="List of attributes.",
    )
    menu_order: int | None = Field(
        None,
        description="Menu order, used to custom sort products.",
    )
    meta_data: list[MetaDatum6] | None = Field(None, description="Meta data.")


class SalesReport(WooCommerceResource):
    total_sales: str | None = Field(None, description="Gross sales in the period.")
    net_sales: str | None = Field(None, description="Net sales in the period.")
    average_sales: str | None = Field(None, description="Average net daily sales.")
    total_orders: int | None = Field(None, description="Total of orders placed.")
    total_items: int | None = Field(None, description="Total of items purchased.")
    total_tax: str | None = Field(None, description="Total charged for taxes.")
    total_shipping: str | None = Field(
        None,
        description="Total charged for shipping.",
    )
    total_refunds: int | None = Field(None, description="Total of refunded orders.")
    total_discount: int | None = Field(None, description="Total of coupons used.")
    totals_grouped_by: str | None = Field(None, description="Group type.")
    totals: list[int] | None = Field(None, description="Totals.")


class TopSellersReport(WooCommerceResource):
    name: str | None = Field(None, description="Product name.")
    product_id: int | None = Field(None, description="Product ID.")
    quantity: int | None = Field(None, description="Total number of purchases.")


class ReportOrderTotal(WooCommerceResource):
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource.",
    )
    name: str | None = Field(None, description="Order status name.")
    total: str | None = Field(None, description="Amount of orders.")


class ReportProductTotal(WooCommerceResource):
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource.",
    )
    name: str | None = Field(None, description="Product type name.")
    total: str | None = Field(None, description="Amount of products.")


class ReportCustomerTotal(WooCommerceResource):
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource.",
    )
    name: str | None = Field(None, description="Customer type name.")
    total: str | None = Field(None, description="Amount of customers.")


class ReportCouponTotal(WooCommerceResource):
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource.",
    )
    name: str | None = Field(None, description="Coupon type name.")
    total: str | None = Field(None, description="Amount of coupons.")


class ReportReviewTotal(WooCommerceResource):
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource.",
    )
    name: str | None = Field(None, description="Review type name.")
    total: str | None = Field(None, description="Amount of reviews.")


class Report(WooCommerceResource):
    slug: str | None = Field(
        None,
        description="An alphanumeric identifier for the resource.",
    )
    description: str | None = Field(
        None,
        description="A human-readable description of the resource.",
    )


class SettingGroup(WooCommerceResource):
    id: str | None = Field(
        None,
        description="A unique identifier that can be used to link settings together.",
    )
    label: str | None = Field(
        None,
        description="A human readable label for the setting used in interfaces.",
    )
    description: str | None = Field(
        None,
        description="A human readable description for the setting used in interfaces.",
    )
    parent_id: str | None = Field(None, description="ID of parent grouping.")
    sub_groups: str | None = Field(None, description="IDs for settings sub groups.")


class Type2(Enum):
    text = "text"
    email = "email"
    number = "number"
    color = "color"
    password = "password"   # noqa: S105
    textarea = "textarea"
    select = "select"
    multiselect = "multiselect"
    radio = "radio"
    image_width = "image_width"
    checkbox = "checkbox"


class Setting(WooCommerceResource):
    id: str | None = Field(None, description="A unique identifier for the setting.")
    group_id: str | None = Field(
        None,
        description="An identifier for the group this setting belongs to.",
    )
    label: str | None = Field(
        None,
        description="A human readable label for the setting used in interfaces.",
    )
    description: str | None = Field(
        None,
        description="A human readable description for the setting used in interfaces.",
    )
    value: str | None = Field(None, description="Setting value.")
    default: str | None = Field(None, description="Default value for the setting.")
    tip: str | None = Field(
        None,
        description="Additional help text shown to the user about the setting.",
    )
    placeholder: str | None = Field(
        None,
        description="Placeholder text to be displayed in text inputs.",
    )
    type: Type2 | None = Field(None, description="Type of setting.")
    options: dict[str, Any] | None = Field(
        None,
        description="Array of options (key value pairs) for inputs such as select, multiselect, and radio buttons.",
    )


class ShippingZone(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    name: str | None = Field(None, description="Shipping zone name.")
    order: int | None = Field(None, description="Shipping zone order.")


class Type3(Enum):
    postcode = "postcode"
    state = "state"
    country = "country"
    continent = "continent"


class ShippingZoneLocation(WooCommerceResource):
    code: str | None = Field(None, description="Shipping zone location code.")
    type: Type3 | None = Field(None, description="Shipping zone location type.")


class Type4(Enum):
    text = "text"
    email = "email"
    number = "number"
    color = "color"
    password = "password"   # noqa: S105
    textarea = "textarea"
    select = "select"
    multiselect = "multiselect"
    radio = "radio"
    image_width = "image_width"
    checkbox = "checkbox"
    class_ = "class"
    order = "order"


class Settings(WooCommerceResource):
    id: str | None = Field(None, description="A unique identifier for the setting.")
    label: str | None = Field(
        None,
        description="A human readable label for the setting used in interfaces.",
    )
    description: str | None = Field(
        None,
        description="A human readable description for the setting used in interfaces.",
    )
    type: Type4 | None = Field(None, description="Type of setting.")
    value: str | None = Field(None, description="Setting value.")
    default: str | None = Field(None, description="Default value for the setting.")
    tip: str | None = Field(
        None,
        description="Additional help text shown to the user about the setting.",
    )
    placeholder: str | None = Field(
        None,
        description="Placeholder text to be displayed in text inputs.",
    )


class ShippingZoneMethod(WooCommerceResource):
    id: int | None = Field(None, description="Shipping method instance ID.")
    instance_id: int | None = Field(None, description="Shipping method instance ID.")
    title: str | None = Field(
        None,
        description="Shipping method customer facing title.",
    )
    order: int | None = Field(None, description="Shipping method sort order.")
    enabled: bool | None = Field(None, description="Shipping method enabled status.")
    method_id: str | None = Field(None, description="Shipping method ID.")
    method_title: str | None = Field(None, description="Shipping method title.")
    method_description: str | None = Field(
        None,
        description="Shipping method description.",
    )
    settings: Settings | None = Field(None, description="Shipping method settings.")


class TaxClass(WooCommerceResource):
    slug: str | None = Field(None, description="Unique identifier for the resource.")
    name: str = Field(..., description="Tax class name.")


class Class(Enum):
    standard = "standard"
    reduced_rate = "reduced-rate"
    zero_rate = "zero-rate"


class Tax4(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    country: str | None = Field(None, description="Country ISO 3166 code.")
    state: str | None = Field(None, description="State code.")
    postcode: str | None = Field(
        None,
        description="Postcode/ZIP, it doesn't support multiple values. Deprecated as of WooCommerce 5.3, 'postcodes' should be used instead.",
    )
    city: str | None = Field(
        None,
        description="City name, it doesn't support multiple values. Deprecated as of WooCommerce 5.3, 'cities' should be used instead.",
    )
    rate: str | None = Field(None, description="Tax rate.")
    name: str | None = Field(None, description="Tax rate name.")
    priority: int | None = Field(None, description="Tax priority.")
    compound: bool | None = Field(
        None,
        description="Whether or not this is a compound rate.",
    )
    shipping: bool | None = Field(
        None,
        description="Whether or not this tax rate also gets applied to shipping.",
    )
    order: int | None = Field(
        None,
        description="Indicates the order that will appear in queries.",
    )
    class_: Class | None = Field(None, alias="class", description="Tax class.")
    postcodes: list[str] | None = Field(
        None,
        description="List of postcodes / ZIPs. Introduced in WooCommerce 5.3.",
    )
    cities: list[str] | None = Field(
        None,
        description="List of city names. Introduced in WooCommerce 5.3.",
    )


class Status4(Enum):
    active = "active"
    paused = "paused"
    disabled = "disabled"


class Webhook(WooCommerceResource):
    id: int | None = Field(None, description="Unique identifier for the resource.")
    name: str | None = Field(None, description="A friendly name for the webhook.")
    status: Status4 | None = Field(None, description="Webhook status.")
    topic: str | None = Field(None, description="Webhook topic.")
    resource: str | None = Field(None, description="Webhook resource.")
    event: str | None = Field(None, description="Webhook event.")
    hooks: list[str] | None = Field(
        None,
        description="WooCommerce action names associated with the webhook.",
    )
    delivery_url: AnyUrl | None = Field(
        None,
        description="The URL where the webhook payload is delivered.",
    )
    secret: str | None = Field(
        None,
        description="Secret key used to generate a hash of the delivered webhook and provided in the request headers. This will default to a MD5 hash from the current user's ID|username if not provided.",
    )
    date_created: str | None = Field(
        None,
        description="The date the webhook was created, in the site's timezone.",
    )
    date_created_gmt: str | None = Field(
        None,
        description="The date the webhook was created, as GMT.",
    )
    date_modified: str | None = Field(
        None,
        description="The date the webhook was last modified, in the site's timezone.",
    )
    date_modified_gmt: str | None = Field(
        None,
        description="The date the webhook was last modified, as GMT.",
    )


class Environment(WooCommerceResource):
    home_url: AnyUrl | None = Field(None, description="Home URL.")
    site_url: AnyUrl | None = Field(None, description="Site URL.")
    version: str | None = Field(None, description="WooCommerce version.")
    log_directory: str | None = Field(None, description="Log directory.")
    log_directory_writable: bool | None = Field(
        None,
        description="Is log directory writable?",
    )
    wp_version: str | None = Field(None, description="WordPress version.")
    wp_multisite: bool | None = Field(None, description="Is WordPress multisite?")
    wp_memory_limit: int | None = Field(None, description="WordPress memory limit.")
    wp_debug_mode: bool | None = Field(
        None,
        description="Is WordPress debug mode active?",
    )
    wp_cron: bool | None = Field(
        None,
        description="Are WordPress cron jobs enabled?",
    )
    language: str | None = Field(None, description="WordPress language.")
    server_info: str | None = Field(None, description="Server info.")
    php_version: str | None = Field(None, description="PHP version.")
    php_post_max_size: int | None = Field(None, description="PHP post max size.")
    php_max_execution_time: int | None = Field(
        None,
        description="PHP max execution time.",
    )
    php_max_input_vars: int | None = Field(None, description="PHP max input vars.")
    curl_version: str | None = Field(None, description="cURL version.")
    suhosin_installed: bool | None = Field(None, description="Is SUHOSIN installed?")
    max_upload_size: int | None = Field(None, description="Max upload size.")
    mysql_version: str | None = Field(None, description="MySQL version.")
    mysql_version_string: str | None = Field(
        None,
        description="MySQL version string.",
    )
    default_timezone: str | None = Field(None, description="Default timezone.")
    fsockopen_or_curl_enabled: bool | None = Field(
        None,
        description="Is fsockopen/cURL enabled?",
    )
    soapclient_enabled: bool | None = Field(
        None,
        description="Is SoapClient class enabled?",
    )
    domdocument_enabled: bool | None = Field(
        None,
        description="Is DomDocument class enabled?",
    )
    gzip_enabled: bool | None = Field(None, description="Is GZip enabled?")
    mbstring_enabled: bool | None = Field(None, description="Is mbstring enabled?")
    remote_post_successful: bool | None = Field(
        None,
        description="Remote POST successful?",
    )
    remote_post_response: str | None = Field(
        None,
        description="Remote POST response.",
    )
    remote_get_successful: bool | None = Field(
        None,
        description="Remote GET successful?",
    )
    remote_get_response: str | None = Field(None, description="Remote GET response.")


class Database(WooCommerceResource):
    wc_database_version: str | None = Field(None, description="WC database version.")
    database_prefix: str | None = Field(None, description="Database prefix.")
    maxmind_geoip_database: str | None = Field(
        None,
        description="MaxMind GeoIP database.",
    )
    database_tables: list[str] | None = Field(None, description="Database tables.")


class Theme(WooCommerceResource):
    name: str | None = Field(None, description="Theme name.")
    version: str | None = Field(None, description="Theme version.")
    version_latest: str | None = Field(None, description="Latest version of theme.")
    author_url: AnyUrl | None = Field(None, description="Theme author URL.")
    is_child_theme: bool | None = Field(
        None,
        description="Is this theme a child theme?",
    )
    has_woocommerce_support: bool | None = Field(
        None,
        description="Does the theme declare WooCommerce support?",
    )
    has_woocommerce_file: bool | None = Field(
        None,
        description="Does the theme have a woocommerce.php file?",
    )
    has_outdated_templates: bool | None = Field(
        None,
        description="Does this theme have outdated templates?",
    )
    overrides: list[str] | None = Field(None, description="Template overrides.")
    parent_name: str | None = Field(None, description="Parent theme name.")
    parent_version: str | None = Field(None, description="Parent theme version.")
    parent_author_url: AnyUrl | None = Field(
        None,
        description="Parent theme author URL.",
    )


class Settings1(WooCommerceResource):
    api_enabled: bool | None = Field(None, description="REST API enabled?")
    force_ssl: bool | None = Field(None, description="SSL forced?")
    currency: str | None = Field(None, description="Currency.")
    currency_symbol: str | None = Field(None, description="Currency symbol.")
    currency_position: str | None = Field(None, description="Currency position.")
    thousand_separator: str | None = Field(None, description="Thousand separator.")
    decimal_separator: str | None = Field(None, description="Decimal separator.")
    number_of_decimals: int | None = Field(None, description="Number of decimals.")
    geolocation_enabled: bool | None = Field(
        None,
        description="Geolocation enabled?",
    )
    taxonomies: list[str] | None = Field(
        None,
        description="Taxonomy terms for product/order statuses.",
    )
    product_visibility_terms: list[str] | None = Field(
        None,
        description="Terms in the product visibility taxonomy.",
    )


class Security(WooCommerceResource):
    secure_connection: bool | None = Field(
        None,
        description="Is the connection to your store secure?",
    )
    hide_errors: bool | None = Field(None, description="Hide errors from visitors?")


class SystemStatus(WooCommerceResource):
    environment: Environment | None = Field(None, description="Environment.")
    database: Database | None = Field(None, description="Database.")
    active_plugins: list[str] | None = Field(None, description="Active plugins.")
    inactive_plugins: list[str] | None = Field(None, description="Inactive plugins.")
    dropins_mu_plugins: list[str] | None = Field(
        None,
        description="Dropins & MU plugins.",
    )
    theme: Theme | None = Field(None, description="Theme.")
    settings: Settings1 | None = Field(None, description="Settings.")
    security: Security | None = Field(None, description="Security.")
    pages: list[str] | None = Field(None, description="WooCommerce pages.")
    post_type_counts: list[str] | None = Field(None, description="Total post count.")


class SystemStatusTool(WooCommerceResource):
    id: str | None = Field(None, description="A unique identifier for the tool.")
    name: str | None = Field(None, description="Tool name.")
    action: str | None = Field(None, description="What running the tool will do.")
    description: str | None = Field(None, description="Tool description.")
    success: bool | None = Field(None, description="Did the tool run successfully?")
    message: str | None = Field(None, description="Tool return message.")


class ShippingMethod(WooCommerceResource):
    id: str | None = Field(None, description="Method ID.")
    title: str | None = Field(None, description="Shipping method title.")
    description: str | None = Field(None, description="Shipping method description.")


class Type5(Enum):
    text = "text"
    email = "email"
    number = "number"
    color = "color"
    password = "password"   # noqa: S105
    textarea = "textarea"
    select = "select"
    multiselect = "multiselect"
    radio = "radio"
    image_width = "image_width"
    checkbox = "checkbox"


class Settings2(WooCommerceResource):
    id: str | None = Field(None, description="A unique identifier for the setting.")
    label: str | None = Field(
        None,
        description="A human readable label for the setting used in interfaces.",
    )
    description: str | None = Field(
        None,
        description="A human readable description for the setting used in interfaces.",
    )
    type: Type5 | None = Field(None, description="Type of setting.")
    value: str | None = Field(None, description="Setting value.")
    default: str | None = Field(None, description="Default value for the setting.")
    tip: str | None = Field(
        None,
        description="Additional help text shown to the user about the setting.",
    )
    placeholder: str | None = Field(
        None,
        description="Placeholder text to be displayed in text inputs.",
    )


class PaymentGateway(WooCommerceResource):
    id: str | None = Field(None, description="Payment gateway ID.")
    title: str | None = Field(None, description="Payment gateway title on checkout.")
    description: str | None = Field(
        None,
        description="Payment gateway description on checkout.",
    )
    order: int | None = Field(None, description="Payment gateway sort order.")
    enabled: bool | None = Field(None, description="Payment gateway enabled status.")
    method_title: str | None = Field(
        None,
        description="Payment gateway method title.",
    )
    method_description: str | None = Field(
        None,
        description="Payment gateway method description.",
    )
    method_supports: list[str] | None = Field(
        None,
        description="Supported features for this payment gateway.",
    )
    settings: Settings2 | None = Field(None, description="Payment gateway settings.")


class DataIndex(WooCommerceResource):
    slug: str | None = Field(None, description="Data resource ID.")
    description: str | None = Field(None, description="Data resource description.")


class State(WooCommerceResource):
    code: str | None = Field(None, description="State code.")
    name: str | None = Field(None, description="Full name of state.")


class Country(WooCommerceResource):
    code: str | None = Field(None, description="ISO3166 alpha-2 country code.")
    currency_code: str | None = Field(
        None,
        description="Default ISO4127 alpha-3 currency code for the country.",
    )
    currency_pos: str | None = Field(
        None,
        description="Currency symbol position for this country.",
    )
    decimal_sep: str | None = Field(
        None,
        description="Decimal separator for displayed prices for this country.",
    )
    dimension_unit: str | None = Field(
        None,
        description="The unit lengths are defined in for this country.",
    )
    name: str | None = Field(None, description="Full name of country.")
    num_decimals: int | None = Field(
        None,
        description="Number of decimal points shown in displayed prices for this country.",
    )
    states: list[State] | None = Field(
        None,
        description="List of states in this country.",
    )
    thousand_sep: str | None = Field(
        None,
        description="Thousands separator for displayed prices in this country.",
    )
    weight_unit: str | None = Field(
        None,
        description="The unit weights are defined in for this country.",
    )


class DataContinents(WooCommerceResource):
    code: str | None = Field(None, description="2 character continent code.")
    name: str | None = Field(None, description="Full name of continent.")
    countries: list[Country] | None = Field(
        None,
        description="List of countries on this continent.",
    )


class DataCountries(WooCommerceResource):
    code: str | None = Field(None, description="ISO3166 alpha-2 country code.")
    name: str | None = Field(None, description="Full name of country.")
    states: list[State] | None = Field(
        None,
        description="List of states in this country.",
    )


class DataCurrencies(WooCommerceResource):
    code: str | None = Field(None, description="ISO4217 currency code.")
    name: str | None = Field(None, description="Full name of currency.")
    symbol: str | None = Field(None, description="Currency symbol.")
