from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from joblib import load


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Replace with your web app's domain
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class Person(BaseModel):
    age: int
    gender: int


model = load("music-recommender.joblib")

@app.get('/')
async def root():
    return {"msg": "Hello World!"}

@app.get('/{name}')
async def age(name:str):
    return {"msg": "hellp " + name}

@app.post('/')
async def person(p: Person):
    prediction = model.predict([[p.age, p.gender]])
    return {"prediction": prediction.tolist()}
    #return p