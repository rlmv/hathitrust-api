
import unittest

import requests

# edit oauth_keys.py with your own key
from oauth_keys import client_key, client_secret
from htdataclient import HTDataClient


class TestDataClient(unittest.TestCase):

    def setUp(self):   
        self.dataclient = HTDataClient(client_key, 
                    client_secret, secure=False)

    def test_bad_doc_id(self):
        self.assertRaises(requests.HTTPError, self.dataclient.getstructure, 'bad doc id')


       

if __name__ == "__main__":
    unittest.main()
