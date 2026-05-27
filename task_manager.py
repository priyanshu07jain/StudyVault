import json
from pathlib import Path
from logger import log

DATA_FILE = "data/tasks.json"


def load_tasks():
    Path(DATA_FILE).parent.mkdir(parents=True, exist_ok=True)

    if not Path(DATA_FILE).exists():
        return []

    if Path(DATA_FILE).stat().st_size == 0:
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task_name, deadline):
    tasks = load_tasks()

    new_id = max((t["id"] for t in tasks), default=0) + 1

    task = {
        "id": new_id,
        "task": task_name,
        "deadline": deadline,
        "status": "pending"
    }

    tasks.append(task)

    save_tasks(tasks)

    log(f"Task added: {task['task']}")

    return task


def complete_task(task_id):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Done"

    save_tasks(tasks)


def list_tasks():
    return load_tasks()


