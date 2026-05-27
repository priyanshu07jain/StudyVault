import typer, threading
from file_manager import organize_files, find_duplicates, backup_folder
from task_manager  import add_task, complete_task, list_tasks
from search_engine import search_files
from analytics     import genrate_report
from scheduler     import start_scheduler
from rich.console  import Console
from rich.table    import Table

app     = Console()
cli     = typer.Typer()

@cli.command()
def organize(path: str):
    """Organize files in a directory"""
    organize_files(path)
    app.print("[green]Files organized![/green]")

@cli.command()
def duplicates(path: str):
    """Find duplicate files"""
    dups = find_duplicates(path)
    for d in dups:
        app.print(f"[red]Duplicate:[/red] [green]{d[0].name} == {d[1].name}[/green]")

@cli.command()
def add(task: str, deadline: str):
    """Add a new task"""
    t = add_task(task, deadline)
    app.print(f"[green]Task #{t['id']} added![/green]")

@cli.command()
def tasks():
    """List all tasks"""
    table = Table("ID", "Task", "Deadline", "Status")
    for t in list_tasks():
        table.add_row(str(t["id"]), t["task"], t["deadline"], t["status"])
    app.print(table)

@cli.command()
def done(task_id: int):
    """Mark task as complete"""
    complete_task(task_id)
    app.print("[green]Task marked done![/green]")

@cli.command()
def search(path: str, keyword: str):
    """Search for files"""
    results = search_files(path, keyword)
    for r in results:
        app.print(r)

@cli.command()
def report():
    """Show productivity report"""
    genrate_report()

@cli.command()
def backup(src: str, dest: str):
    """Backup a folder"""
    backup_folder(src, dest)

@cli.command()
def reminders():
    """Start background reminder service"""
    # t = threading.Thread(target=start_scheduler)
    # t.start()
    app.print("[blue]Reminder service started...[/blue]")
    start_scheduler()
    # t.join()

if __name__ == "__main__":
    cli()


    