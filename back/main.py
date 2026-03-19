from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/api/data")
def get_data():
    return {"Hello world"}