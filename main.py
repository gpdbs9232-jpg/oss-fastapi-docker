from fastapi import FastAPI

app = FastAPI()

courses = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "Java"}
]

@app.get("/")
def root():
    return {"message": "FastAPI Docker Server"}

@app.get("/courses")
def get_courses():
    return courses