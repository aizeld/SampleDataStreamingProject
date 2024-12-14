from spark_stream import create_cassandra_connection, create_keyspace, create_table
session = create_cassandra_connection()
if session:
    create_keyspace(session)
    create_table(session)
