from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Task
from schemas import TaskCreate, TaskResponse  # Import Pydantic models
from fastapi import FastAPI
from database import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()  # Create tables if not exist

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Taskify API Running"}

@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(title=task.title, description=task.description, completed=False)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
