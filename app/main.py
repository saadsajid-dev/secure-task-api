from fastapi import FastAPI, HTTPException
from typing import List

from app.models import Task, TaskCreate

app = FastAPI(title="Secure Task Management API")

tasks_db: List[Task] = []
task_id_counter = 1

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    global task_id_counter

    new_task = Task(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        completed=False
    )

    tasks_db.append(new_task)
    task_id_counter += 1

    return new_task

@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
        
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, udpated_task: TaskCreate):
    for task in tasks_db:
        if task.id == task_id:
            task.title = udpated_task.title
            task.description = udpated_task.description
            return task
    
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return
        
    raise HTTPException(status_code=404, detail="Task not found")

