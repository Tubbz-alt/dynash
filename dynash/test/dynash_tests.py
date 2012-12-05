import unittest
from mock import MagicMock
from dynash.dynash import DynamoDBShell

import boto
from boto.dynamodb import connect_to_region

DYNASH_TEST_GET = 'dynash_test_get'

'''
Simple test to check setup of git + nosetests
'''
class DynashGetTests(unittest.TestCase):
    def setUp(self):
        # we assume that we have a DYNASH_TEST_GET already exists,
        # and it has a string hash and range key
        region_name = boto.config.get('dynamodb', 'region', 'us-east-1')        
        connection = connect_to_region(region_name)
        table = connection.get_table(DYNASH_TEST_GET)
        
        item_data = {
            'attr' : 'hello dynamo'
        }
        item = table.new_item(
            hash_key = 'key1',
            range_key = 'range1',
            attrs = item_data
        )
        item.put()
        
        self.dynash = DynamoDBShell()
    
    def test_do_get_with_key_and_range(self):
        self.dynash.pprint = MagicMock()
        expected_item = {'key_name': 'key1',
                         'range_key_name' : 'range1',
                         'attr': 'hello dynamo'}
        
        self.dynash.do_get(':'+DYNASH_TEST_GET + ' key1 range1')
        self.dynash.pprint.assert_called_once_with(expected_item)
