

__author__ = 'robertmarchman'


# constants for bibliographic api
BIB_BASEURL = 'http://catalog.hathitrust.org/api/volumes/'
ID_TYPES = ['oclc',
            'lccn',
            'issn',
            'isbn',
            'htid',
            'recordnumber',
            ]


# constants for data api
DATA_BASEURL = 'http://babel.hathitrust.org/cgi/htd/'
SECURE_DATA_BASEURL = 'https://babel.hathitrust.org/cgi/htd/'


# constants for solrproxy
SOLR_HOST = "http://chinkapin.pti.indiana.edu"
SOLR_PORT = 9994
QUERY_STUB = "/solr/select/"
MARC_STUB = "/solr/MARC/"


