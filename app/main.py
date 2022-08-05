from typing import Union

from fastapi import FastAPI

from app.generate_password import random_password

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "I'm password generator"}


@app.get("/generate")
def generate_pass(plen: int = 8):
    pas, msg = random_password(plen)
    return {"pass": pas, "message": msg}
