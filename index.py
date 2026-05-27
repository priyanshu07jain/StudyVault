from file_manager import organize_files, find_duplicates, backup_folder
from task_manager import add_task, complete_task, list_tasks
from search_engine import search_files, search_in_content
from analytics import genrate_report
from scheduler import start_scheduler
from rich.console import Console
from rich.table    import Table

app = Console()

Menu = {
    "Organize": "1. Organize files",
    "Duplicate": "2. Find duplicate files",
    "Backup": "3. Backup files",
    "Add": "4. Add task",
    "Done": "5. complete task",
    "All tasks": "6. View all tasks",
    "Report": "7. task Report",
    "Search_file": "8. Search file",
    "Search keyword": "9. Search keyword",
}

while (True):
    app.print("[red]MENU![/red]")
    for task, desc in Menu.items():
        app.print(f"[green]{desc}[/green]")
    choice = input("Enter your choice   ")
    print("--"*50)
    if (choice == "1"):
        app.print(
            f"[yellow]you are now Organizing the files give path of the directory you want to organize[/yellow]")
        path = input("Enter Path ==> ")
        try:
            organize_files(path)
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")

        print("--"*50)
        input("To go back to Menu press Enter ...")
    elif (choice == "2"):
        app.print(f"[yellow]you are now finding duplicates files give path of the directory you want to find duplicate in.[/yellow]")
        path = input("Enter Path ==> ")
        try:
            dups=find_duplicates(path)
            for d in dups:
                app.print(f"[red]Duplicate:[/red] [green]{d[0].name} == {d[1].name}[/green]")
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")
        print("--"*50)
        input("To go back to Menu press Enter ...")
    elif (choice == "3"):
        app.print(f"[yellow]Now you want to backup a file enter the path of the file you want to backup and the destination where you want to backup[/yellow]")
        source_path = input(r"Enter Path ==> ")
        destination = input(r"Enter Destination ==> ")
        try:
            backup_folder(source_path, destination)
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")

        print("--"*50)
        input("To go back to Menu press Enter ...")
    elif (choice == "4"):
        app.print(
            f"[yellow]To add a Task enter the task and the deadline in this fomat 01-01-2026 (prefered way)[/yellow]")
        path = input("Enter Task detail ==> ")
        date = input("Enter the Date ")
        try:
            add_task(path, date)
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")
        else:
            app.print(f"[green]Task added succesfully[/green]")

        print("--"*50)
        input("To go back to Menu press Enter ...")
    elif (choice == "5"):
        app.print(f"[yellow]To complete a task enter the task id [/yellow]")
        path = int(input("Enter Task id ==> "))
        try:
            complete_task(path)
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")
        else:
            app.print(f"[green]Task Completed succesfully[/green]")
            
        print("--"*50)
        input("To go back to Menu press Enter ...")
    elif (choice == "6"):
        app.print(f"[yellow]View all tasks[/yellow]")
        try:
            table = Table("ID", "Task", "Deadline", "Status")
            for t in list_tasks():
                table.add_row(str(t["id"]), t["task"], t["deadline"], t["status"])
            app.print(table)
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")

        print("--"*50)
        input("To go back to Menu press Enter ...")
    elif (choice == "7"):
        app.print(f"[yellow]You are checking your task report[/yellow]")
        try:
            genrate_report()
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")

        print("--"*50)
        input("To go back to Menu press Enter ...")
    elif (choice == "8"):
        app.print(f"[yellow]You are now checking the directory[/yellow]")
        dire = input("Enter the directory ==> ")
        key = input("Enter the file name you want to search ==> ")
        try:
            results=search_files(dire,key)
            for r in results:
             app.print(f"[purple]{r}[/purple]")
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")
            input("To go back to Menu press Enter ...")
        print("--"*50)
    elif (choice == "9"):
        app.print(f"[yellow]You are now serching the keywords in directory[/yellow]")
        dire = input("Enter the directory ==> ")
        key = input("Enter the keyword you want to search ==> ")
        try:
            results=search_in_content(dire,key)
            for r in results:
             app.print(f"[purple]{r}[/purple]")
        except Exception as e:
            print(f"[ERROR] Something went wrong: {e}")
        print("--"*50)
        input("To go back to Menu press Enter ...")
    else:
        input("give valid Input from menu press enter to go Back")
