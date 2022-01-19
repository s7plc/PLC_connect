from cpppo.server.enip import client

# HOST = "192.168.32.68" banbury deprag(..)
HOST = "10.10.25.100"
TAGS = ["@4/100/3"]

with client.connector(host=HOST) as conn:
    operations=client.parse_operations(TAGS)
print(operations)

