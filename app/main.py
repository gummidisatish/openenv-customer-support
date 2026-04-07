from fastapi import FastAPI
from app.env import OpenEnv

app = FastAPI()

env = OpenEnv()


@app.get("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(action: dict):
    return env.step(action)


@app.get("/state")
def state():
    return env.state()


@app.get("/tasks")
def tasks():
    return env.get_tasks()


@app.get("/grader")
def grader():
    return env.get_score()


@app.get("/baseline")
def baseline():
    from app.baseline.run import run_baseline
    return run_baseline()
@app.get("/")
def home():
    return {"message": "OpenEnv Customer Support API is running"}