hathitrust-api
=================

A simple interface for the HathiTrust APIs. The package contains basic classes and associated methods for querying the [Bibliographic API][bib api], [Data API][data api], and the [HTRC Solr Proxy][solr api].

[bib api]: http://www.hathitrust.org/bib_api
[data api]: http://www.hathitrust.org/data_api
[solr api]: http://wiki.htrc.illinois.edu/display/COM/Solr+Proxy+API+User+Guide

#### DataAPI
The Data API retrieves non-google public domain works from the HathiTrust.

An OAuth [keyset][kgs] from HathiTrust is required to use the Data API. 

Example usage:
```
>>> from hathitrust_api import DataAPI

>>> data_api = DataAPI(your_oauth_key, your_oauth_secret)

>>> ocrtext = data_api.getpageocr('dul1.ark:/13960/t00z82c1q', 14)
```

[kgs]: http://babel.hathitrust.org/cgi/kgs/request

#### BibAPI
The bibliographic API delivers HathiTrust bibliographic data and MARC records in JSON format.

Example:
```
>>> from hathitrust_api import BibAPI

>>> bib_api = BibAPI()

>>> bib_info = bib_api.get_single_record_json('htid', 'dul1.ark:/13960/t00z82c1q')

>>> bib_info.keys()
[u'records', u'items']

>>> bib_info['records']['010944133']['publishDates']
[u'1670']
```

#### SolrAPI
The HTRC Solr Proxy is a search index over the public domain collection.

``` 
>>> from hathitrust_api import SolrAPI

>>> solr = SolrAPI()

>>> results = solr.query("new zealand", fields=['title'])

>>> results
{u'responseHeader': {u'status': 0, u'QTime': 19}, u'response': {u'start': 0, u'numFound': 366613, u'docs': [{u'title': [u'The statues of New Zealand ...']}, {u'title': [u'New Zealand.']}, {u'title': [u"Wise's New Zealand index"]}, {u'title': [u'Palaeontological bulletin.']}, {u'title': [u'New Zealand,']}, {u'title': [u'The New Zealand official year-book.']}, {u'title': [u'The New Zealand official year-book.']}, {u'title': [u'The New Zealand official year-book.']}, {u'title': [u'The New Zealand official year-book.']}, {u'title': [u'The New Zealand official year-book.']}]}}
```



Packages:
---------
* [requests][requests] (available in PyPI)
* [requests-oauthlib][req oauth[]] (a Requests plugin; the version in PyPI had some errors, so you may need to get it straight from the source.)

[req oauth]: https://github.com/requests/requests-oauthlib
[requests]: http://docs.python-requests.org/en/latest/

Needed:
------
* Write test cases.
