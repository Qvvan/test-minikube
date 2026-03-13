from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"status": "ok!"}

@app.get("/db-test")
def db_test():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    conn.close()
    return {"postgres_version": version[0]}