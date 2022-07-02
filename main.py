from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
def read_root():
    return {"say": "Hello raghu"}


@app.get("/{id_no}")
def put_java(id_no: str):
    # number = id_no * id_no
    # return {f"power of {id_no} is ": f"{number}"}
    return {"Input is": id_no}
