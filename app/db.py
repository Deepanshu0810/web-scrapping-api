from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("DB_CLIENT_ID")
CLIENT_SECRET = os.getenv("DB_CLIENT_SECRET")


BASE_DIR = Path(__file__).parent
CLUSTER_BUNDLE = BASE_DIR / "ignored" / "secure-connect-fastapi-db.zip"


def get_cluster():
    cloud_config= {
        'secure_connect_bundle': CLUSTER_BUNDLE
    }
    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    return cluster

def get_cassandra_session():
    cluster = get_cluster()
    session = cluster.connect()
    return session

session = get_cassandra_session()
row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")