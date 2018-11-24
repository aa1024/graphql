#The example below shows executing queries against a local schema.

from gql import gql, Client

client = Client(schema=schema)
query = gql('''
{
  hello
}
''')

client.execute(query)
