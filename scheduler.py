import asyncio
from datetime import datetime
from task_manager import list_tasks

reminded_tasks = set()

async def check_deadlines():
    while True:
        tasks=list_tasks()
        today = datetime.now().strftime("%d-%m-%Y").lstrip("0").replace("-0", "-")
        for t in tasks:
            task_id = t["id"]
            if t["deadline"] == today and t["status"] == "pending" and task_id not in reminded_tasks:
                print(f"REMINDER:'{t['task']} is due TODAY")
                reminded_tasks.add(task_id)
        await asyncio.sleep(5)


def start_scheduler():

    try:
        print("Scheduler started...")
        asyncio.run(check_deadlines())
    except KeyboardInterrupt:
        print("\nStopping scheduler safely...")
    finally:
        print("Scheduler exited.")