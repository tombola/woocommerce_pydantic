# WooCommerce Pydantic

`woocommerce-pydantic` is a Python package that provides Pydantic models for WooCommerce API responses. This project aims to facilitate interaction with the WooCommerce REST API by providing structured data models.

This package is a wrapper around the [woocommerce](https://pypi.org/project/WooCommerce/) package.

The main addition from this package is adding a `data()` method to the response which turns validated pydantic models instead of JSON.

## Features

- Pydantic models for various WooCommerce API endpoints
- Easy integration with WooCommerce API responses
- Supports Python 3.9 and above
- Allows full editor autocomplete for the API responses using types

## Installation

```sh
pip install woocommerce-pydantic
```
or if you are on board with uv

```sh
uv add woocommerce-pydantic
```

## Usage

See [woocommerce](https://pypi.org/project/WooCommerce/) package for full
details.

The example below gives an indication of the response.

```python
from woocommerce_pydantic import wcapi

wcapi = API(
    url="http://example.com",
    consumer_key="ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    consumer_secret="cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    version="wc/v3"
)
```

```bash
>>> r = wcapi.get("products")
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=UTF-8'
>>> r.encoding
'UTF-8'
>>> r.text
u'{"products":[{"title":"Flying Ninja","id":70,...'
>>> r.json()
{u'products': [{u'sold_individually': False,...
```
