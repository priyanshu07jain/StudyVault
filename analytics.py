from task_manager import list_tasks

def genrate_report():
    tasks =list_tasks()
    total=len(tasks)
    done=sum(1 for t in tasks if t["status"]=="Done")
    pending=total-done
    print(f"Productivity Report")
    print(f"Total Tasks:{total}")
    print(f"Completed : {done}")
    print(f"Pending : {pending}")
    if total:
        print(f"Succes Rate: {done/total*100:.1f}%")