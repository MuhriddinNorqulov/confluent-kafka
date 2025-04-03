from ksqldb import KSQLdbClient

# ksqlDB server manzili
KSQLDB_SERVER = "http://localhost:8088"

# KsqlDB bilan ulanish
client = KSQLdbClient(KSQLDB_SERVER)

print(
    client.query_sync("select * from MY_STREAM;", stream_properties={"ksql.streams.auto.offset.reset": "earliest"},
                      timeout=None))

