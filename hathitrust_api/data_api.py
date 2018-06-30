from __future__ import absolute_import

import requests
from requests_oauthlib import OAuth1

from .constants import DATA_BASEURL, SECURE_DATA_BASEURL


class DataAPI(object):

    def __init__(self, client_key, client_secret, secure=True):
        """ Initialize a DataAPI object.
        Args:
            client_key: OAuth client key (registered with HathiTrust)
            client_secret: secret OAuth key
            secure: toggles http/https session. Defaults to
                 http, use https for access to restricted content.
        Initializes a persistent Requests session and attaches 
        OAuth credentials to the session. All queries are performed as 
        method calls on the HTDataInterface object.
        For now, all queries return the raw content string, rather than
        processing the json or xml structures.
        """

        self.client_key = client_key
        self.client_secret = client_secret
        self.oauth = OAuth1(client_key=client_key, 
                            client_secret=client_secret, 
                            signature_type='query')

        self.rsession = requests.Session()
        self.rsession.auth = self.oauth

        if secure:
            self.baseurl = SECURE_DATA_BASEURL
        else: 
            self.baseurl = DATA_BASEURL


    def _makerequest(self, resource, doc_id, doc_type='volume', sequence=None, 
                        v=2, json=False, callback=None):
        """ Construct and perform URI request.
        Args:
            resource: resource type
            doc_id: document identifier of target
            doc_type: type of document: volume or article
            sequence: page number for single page resources
            v: API version 
            json: if json=True, the json representation of
                the resource is returned. Only valid for resources that 
                are xml or xml+atom by default.
            callback: optional javascript callback function, 
                which only has an effect if json=True.
        Return: 
            content of the response, in bytes
        Note there's not much error checking on url construction, 
        but errors do get raised after badly formed requests. 
        To do: implement some exception checking here, and identify 
        what sort of errors are being returned (eg. BadRequest, 
        Unauthorized, NotFound, etc.)   
        """

        url = "".join([self.baseurl, doc_type, '/', resource, '/', doc_id])
        
        if sequence:
            url += '/' + str(sequence)

        params = {'v': str(v)}
        if json:
            params['format'] = 'json'
            if callback:
                params['callback'] = callback
        
        r = self.rsession.get(url, params=params)
        r.raise_for_status()

        return r.content


    def getmeta(self, doc_id, doc_type='volume', json=False):
        """ Retrieve Volume and Rights Metadata resources.
        Args:
            doc_id: document identifier
            json: if json=True, the json representation of
                the resource is returned, otherwise efaults to an atom+xml 
                format.
        Return: 
            xml or json string
        """
        return self._makerequest('meta', doc_id, doc_type=doc_type, json=json)


    def getstructure(self, doc_id, doc_type='volume', json=False):
        """ Retrieve a METS document.
        Args:
            doc_id: target document
            json: toggles json/xml 
        Return:
            xml or json string
        """
        return self._makerequest('structure', doc_id, doc_type=doc_type, json=json)


    def getpagemeta(self, doc_id, seq, doc_type='volume', json=False):
        """ Retrieve single page metadata. """
        return self._makerequest('pagemeta', doc_id, doc_type=doc_type, sequence=seq, json=json)


    def getaggregate(self, doc_id, doc_type='volume'):
        """ Get aggregate record data. 
        Return: 
            zip content that contains tiff/jp2/jpeg, .txt OCR files,
                + Source METS (not the same as Hathi METS)
        """
        return self._makerequest('aggregate', doc_id, doc_type=doc_type)


    def getpageimage(self, doc_id, seq, doc_type='volume'):
        """ Retrieve Single Page Image.
        Return:
            response with tiff, jp2, or jpeg file
        """
        return self._makerequest('pageimage', doc_id, doc_type = doc_type, sequence=seq)


    def getpageocr(self, doc_id, sequence, doc_type='volume'):
        """  Get single-page OCR.
        Return:
            UTF-8 encoded OCR plain text
        """
        return self._makerequest('pageocr', doc_id, doc_type = doc_type, sequence=sequence)


    def getpagecoordocr(self, doc_id, sequence, doc_type='volume'):
        """ Get single-page coordinate OCR.
        Return:
            UTF-8 encoded XML OCR
        """
        return self._makerequest('pagecoordocr', doc_id, doc_type = doc_type, sequence=sequence)

    def getdocumentocr(self, doc_id, start_page = 1, end_page = 1e5 , doc_type = 'volume'):
        """  Get OCR for an entire document.
        Return:
            List of UTF-8 encoded OCR plain text from start_page to end_page (or entire work if no bounds provided)
        """
        outPages = []
        i = start_page
        while (i <= end_page):
            try:
                outPages.append(self.getpageocr(doc_id, i, doc_type=doc_type))
                i += 1
            except:
                break
        return outPages
        
    def getdocumentcoordocr(self, doc_id, start_page = 1, end_page = 1e5 , doc_type = 'volume'):
        """  Get coordinate OCR for an entire document.
        Return:
            List of UTF-8 encoded XML OCR plain text from start_page to end_page (or entire work if no bounds provided)
        """
        outPages = []
        i = start_page
        while (i <= end_page):
            try:
                outPages.append(self.getpagecoordocr(doc_id, i, doc_type=doc_type))
                i += 1
            except:
                break
        return outPages
        

   
