
# constants for bibliographic api
BIB_BASEURL = 'http://catalog.hathitrust.org/api/volumes/'


# constants for data api
_STUB = 'babel.hathitrust.org/cgi/htd/'
DATA_BASEURL = ''.join(['http://', _STUB])
SECURE_DATA_BASEURL = ''.join(['https://', _STUB])


# constants for solrproxy
_SOLR_HOST = "http://chinkapin.pti.indiana.edu"
_SOLR_PORT = 9994
_QUERY_STUB = "/solr/meta/select/"
_MARC_STUB = "/solr/MARC/"

QUERY_BASEURL = ''.join([_SOLR_HOST, ':', str(_SOLR_PORT), _QUERY_STUB])
MARC_BASEURL = ''.join([_SOLR_HOST, ':', str(_SOLR_PORT), _MARC_STUB])

