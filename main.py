from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
# uvicorn main:app --reload
app = FastAPI()


@app.get("/")
def read_root():
    return {"say": "Hello raghu"}


@app.get("/{id_no}")
def put_java(id_no: int):
    number = id_no * id_no
    # return {f"power of {id_no} is ": f"{number}"}
    return {"power values is ": number}
