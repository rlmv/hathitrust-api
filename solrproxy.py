
import sys
import json
import argparse
import zipfile
from string import replace

import requests


SOLR_HOST = "http://chinkapin.pti.indiana.edu"
SOLR_PORT = 9994
QUERY_STUB = "/solr/select/"
MARC_STUB = "/solr/MARC/"
querybaseurl = "".join([SOLR_HOST, ":", str(SOLR_PORT), QUERY_STUB])
marcbaseurl = "".join([SOLR_HOST, ":", str(SOLR_PORT), MARC_STUB])


def _cleanquery(querystring):
    """ Cleans up the query - replaces internal
    single quotation marks with double quotes, so
    Solr produces correct results.
    
    Solr is sensitive to the difference between ' and " -
    it will regard terms surrounded with '...' as separate
    queryterms, but "..." as a single concatenated phrase.
    """
    return replace(querystring, '\'', '\"')

    
def query(querystring, rows=10, start=0, fields=[]):
    """
    Arguments:
        rows: the maximum number of results to return
        fields: an iterable of fields to return with the
            response, eg. fl=['title', 'author']

    Return:
        JSON resource
    """
    querystring = _cleanquery(querystring)
    
    terms = {}
    terms['q'] = querystring
    terms['rows'] = rows
    terms['start'] = start
    terms['qt'] = 'sharding'
    terms['wt'] = 'json'

    if fields:
        terms['fl'] = ','.join(fields)

    r = requests.get(querybaseurl, params=terms)
    r.raise_for_status()

    return r.json()


def iterquery(querystring, rows=10, fields=[]):
    """ Defines an generator over a query.
    
        This lets you stick the query in a for loop
        and iterate over all the results, like so:
        
        >>> for doc in iterquery(<querystring>):
        ...     print json.dumps(doc, indent=4)
        
        The return docs are python-interpreted json
        structures - the SOLR api spec defines the
        available fields:
        http://wiki.htrc.illinois.edu/display/COM/2.+Solr+API+User+Guide
        
        For now, errors get passed up from the query
        function...TODO: implement some handling.
    """
    
    for batch in batchquery(querystring, size=rows, fields=fields):
        for doc in batch:
            yield doc
        

def batchquery(querystring, size=10, fields=[]):
    """ Returns a generator over batches of query results.
    
    Yields an iterable of len [size] with each next() call.
    """
    
    num_retrieved = 0
    new_iter = True
    num_found = None
    
    while True:
        # send a query, then iterate over ['response']['docs']
        result = query(querystring, rows=size, start=num_retrieved, fields=fields)
        
        if new_iter:
            num_found = result['response']['numFound']
            new_iter = False
        
        if num_found == num_retrieved:
            raise StopIteration
        
        batch = [doc for doc in result['response']['docs']]
        num_retrieved += len(batch)
        
        yield batch
        
        
def batch_ids(querystring, num=10):
    """ Returns lists of ids for querystring of
        at most length [num]."""
    
    for batch in batchquery(querystring, num):
        yield [doc['id'] for doc in batch]
            

def getnumfound(querystring):
    """ Return the total number oqf matches for the query. """
    return int(query(querystring, rows=0)['response']['numFound'])


def getallids(querystring):
    """ Return an generator over all the document ids that
        match querystring."""
    for doc in iterquery(querystring, fields=['id']):
        yield doc['id']


def getmarc(ids):
    """ Retrieves MARC data from the Solr server.
        Returns zip content.
        
        ids - a list of document ids
    """
      
    idstring = "|".join(doc_id for doc_id in ids)
    params = {"volumeIDs" : idstring}
    
    r = requests.get(marcbaseurl, params=params)
    r.raise_for_status()
    return r.content
    

if __name__ == "__main__":
    #ids = [ 'mdp.39015026997125', 'uc1.31822021576848', 'uc2.ark:/13960/t3902080r']
      
    print _cleanquery("author : 'new zealand'")
