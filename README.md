hathitrust-api
=================

A simple interface for the HathiTrust APIs. The package contains basic classes and associated methods for querying the [Bibliographic API][bib api], [Data API][data api], and the [HTRC Solr Proxy][solr api].

[bib api]: http://www.hathitrust.org/bib_api
[data api]: http://www.hathitrust.org/data_api
[solr api]: http://wiki.htrc.illinois.edu/display/COM/Solr+Proxy+API+User+Guide

#### DataAPI

An OAuth keyset from HathiTrust is required to use the Data API.

#### BibAPI

#### SolrAPI





Packages:
---------
* requests (available in PyPI)
* requests-oauthlib (a Requests plugin; the version in PyPI had some errors, so you may need to get it straight from the [source][req oauth].)

[req oauth]: https://github.com/requests/requests-oauthlib


Needed:
------
* Write test cases.
* Implement exceptions to identify HathiTrust response codes.