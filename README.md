hathitrust-api
=================

A simple interface for the HathiTrust APIs. The package contains two basic classes for querying the [Bibliographic API][bib api], [Data API][data api], and the [HTRC Solr Proxy][solr api]. For consistancy, each API is represented by a class with methods for querying the resource.

[bib api]: http://www.hathitrust.org/bib_api
[data api]: http://www.hathitrust.org/data_api
[solr api]: http://wiki.htrc.illinois.edu/display/COM/2.+Solr+API+User+Guide

data_api
--------
An OAuth keyset from HathiTrust is required to use the Data API.

bib_api
-------

solr_api
--------


Packages:
---------
* requests (available in PyPI)
* requests-oauthlib (a Requests plugin; the version in PyPI currently has some errors, so get it straight from the [source repo][req oauth].)

[req oauth]: https://github.com/requests/requests-oauthlib


Needed:
------
* Write test cases.
* Implement exceptions to identify HathiTrust response codes.