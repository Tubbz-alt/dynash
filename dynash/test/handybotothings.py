import boto
from boto.dynamodb import connect_to_region

connection = boto.connect_dynamodb()
print connection.list_tables()


region_name = boto.config.get('dynamodb', 'region', 'eu-west-1')
connection = connect_to_region(region_name)

print connection.list_tables()
def create_table():
    table_schema = connection.create_schema(
        hash_key_name='key_name',
        hash_key_proto_value='S',
        range_key_name='range_key_name',
        range_key_proto_value='S'
    )

    table = connection.create_table(
            name='dynash_test_hash_and_range',
            schema=table_schema,
            read_units=10,
            write_units=5
    )

def delete_table():
    table = connection.get_table('dynash_test_get')
    table.delete()
    
create_table()
