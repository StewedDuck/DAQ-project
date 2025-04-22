import datetime, pymysql
from dbutils.pooled_db import PooledDB
from pymysql.cursors import DictCursor
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME

# 1) Set up your MySQL pool
pool = PooledDB(
    creator=pymysql,
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWD,
    database=DB_NAME,
    cursorclass=DictCursor,
    maxconnections=5,
    blocking=True
)

def get_primary_data():
    """Returns all KidBright readings as a list of dicts."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ID, ts, lat, lon, temp, dust_value, place_type
            FROM `Project_Pikha_D&D`
        """)
        rows = cs.fetchall()

    # Convert datetime to ISO strings
    for r in rows:
        if isinstance(r.get("ts"), datetime.datetime):
            r["ts"] = r["ts"].isoformat()
    return rows

def get_secondary_data():
    """Returns all TMD readings, filling temp=None since no temp column."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ID, ts, lat, lon, dust_value, place_type
            FROM Project_secondary
        """)
        rows = cs.fetchall()

    for r in rows:
        if isinstance(r.get("ts"), datetime.datetime):
            r["ts"] = r["ts"].isoformat()
        r["temp"] = None
    return rows

def get_predictions():
    """Stubbed trend‑based predictions."""
    return {
        "dustPrediction": 42.0,
        "tempPrediction": 25.5
    }
