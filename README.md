# EasyCredit API SDK (Python)

EasyCredit REST integration. 

Please note this is a **non-official** Amazon Pay Python SDK and can only be used for API calls to the EasyCredit
endpoint.

For more details about the API, please check
the [Official Documentation for Installment Purchases](https://developer.easycredit-ratenkauf.de/documentation/api-dokumentation-v3/).

```python
>>> from easy_credit import Client
>>> c = Client(webshop_id='YOUR_ID',token='AUTH_TOKEN')
>>> c.get_transaction('1.de.4145.1-0303135329-211').is_authorized()
True
>>> c.response.json().get('descision').get('decisionOutcome')
'EWZEN7'
>>> c.response.text # returns text from response object
'{"decision":{"transactionId" ...'
>>> c.response.json() 
{'decision': {'transactionId' ... }
```

## Requirements

* Python 3.x
* requests 

## Installation

Use PyPI to install the latest release of this SDK.

```shell
pip install EasyCreditClient
```

## Configuration

You will need to generate the API crednetials from the [easyCredit Partner Portal](partner.easycredit-ratenkauf.de).

```python
from easy_credit import Client

client = Client(
    webshop_id='YOUR_ID',
    token='AUTH_TOKEN'
)
```

