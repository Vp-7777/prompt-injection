from fastapi import FastAPI
from env import PromptInjectionEnv
from models import Action

app = FastAPI()

env = PromptInjectionEnv()


@app.get("/")
def home():
    return {"message": "Server is running"}


@app.get("/reset")
def reset(task: str = "easy"):
    state = env.reset(task)
    return state


@app.post("/step")
def step(action: Action):
    result = env.step(action)
    return result