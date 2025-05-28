import psycopg2
from SecretConfig import PGHOST, PGDATABASE, PGUSER, PGPASSWORD, PGPORT

def get_connection():
    return psycopg2.connect(
        host=PGHOST,
        database=PGDATABASE,
        user=PGUSER,
        password=PGPASSWORD,
        port=PGPORT
    )
