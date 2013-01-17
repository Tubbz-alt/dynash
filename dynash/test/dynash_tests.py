import unittest
from mock import MagicMock
from dynash.dynash import DynamoDBShell

import boto
from boto.dynamodb import connect_to_region

DYNASH_TEST_HASH_AND_RANGE = 'dynash_test_hash_and_range'
HASH_KEY_STR = 'key1'
RANGE_KEY_STR = 'range1'
ATTRIBUTES = {'attr':'hello dynamo'}

class DynashTest(unittest.TestCase):
    def setUp(self):
        region_name = boto.config.get('dynamodb', 'region', 'us-east-1')        
        self.connection = connect_to_region(region_name)

'''
Tests to check the functionality of the do_get method
'''
class DynashGetTests(DynashTest):
    def setUp(self):
        DynashTest.setUp(self)
        # we assume that we have a DYNASH_TEST_HASH_AND_RANGE already exists,
        # and it has a string hash and range key
        table = self.connection.get_table(DYNASH_TEST_HASH_AND_RANGE)
        
        item = table.new_item(hash_key = HASH_KEY_STR,
                              range_key = RANGE_KEY_STR,
                              attrs = ATTRIBUTES)
        item.put()
        
        self.dynash = DynamoDBShell()
        self.dynash.pprint = MagicMock()

#    def test_do_get_with_str_key(self):
#        expected_item = dict({'key_name': HASH_KEY_STR,
#                              'range_key_name' : RANGE_KEY_STR},
#                              **ATTRIBUTES)
#
#        self.do_get(DYNASH_TEST_HASH_AND_RANGE, HASH_KEY_STR)
#        self.dynash.pprint.assert_called_once_with(expected_item)
    
    def test_do_get_with_str_key_and_str_range(self):
        expected_item = dict({'key_name': HASH_KEY_STR,
                              'range_key_name' : RANGE_KEY_STR},
                              **ATTRIBUTES)
        
        self.do_get(DYNASH_TEST_HASH_AND_RANGE, HASH_KEY_STR, RANGE_KEY_STR)
        self.dynash.pprint.assert_called_once_with(expected_item)
        
    def do_get(self, table_name, hash_key, range_key=None):
        line = ':' + DYNASH_TEST_HASH_AND_RANGE + ' ' + hash_key
        if range_key:
            line = line + ' ' + range_key
        self.dynash.do_get(line)

    def tearDown(self):
        table = self.connection.get_table(DYNASH_TEST_HASH_AND_RANGE)
        item = table.get_item(hash_key=HASH_KEY_STR, range_key=RANGE_KEY_STR)
        item.delete()
        # delete tables?
        
class DynashQueryTests(DynashTest):
    def setUp(self):
        DynashTest.setUp(self)
        # we assume that we have a DYNASH_TEST_HASH_AND_RANGE already exists,
        # and it has a string hash and range key
        
        attrs1 = {'attr':'hello'}
        attrs2 = {'attr':'dynamo'}
        
        self.__insert_item('key1', 'range1', attrs1)
        self.__insert_item('key1', 'range2', attrs2)
        
        self.dynash = DynamoDBShell()
        self.dynash.pprint = MagicMock()
           
    def test_query_returns_results(self):
        expected_results = [
                            {'key_name':'key1',
                             'range_key_name':'range1',
                             'attr':'hello'},
                            {'key_name':'key1',
                             'range_key_name':'range2',
                             'attr':'dynamo'}]
        line = ':' + DYNASH_TEST_HASH_AND_RANGE + ' key1' 
        self.dynash.do_query(line)
        self.dynash.pprint.assert_called_once_with(expected_results)
    
    def __insert_item(self, hash_key, range_key, attributes):
        table = self.connection.get_table(DYNASH_TEST_HASH_AND_RANGE)
        
        item = table.new_item(hash_key = HASH_KEY_STR,
                              range_key = RANGE_KEY_STR,
                              attrs = ATTRIBUTES)
        item.put()
        