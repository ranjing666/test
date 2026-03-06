from pathlib import Path

from storage import DEFAULT_DATA_FILE, load_tasks, save_tasks


def print_menu() -> None:
    print("\n=== Learning Manager ===")
    print("1. List tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Show stats")
    print("0. Exit")


def list_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("No tasks yet.")
        return

    print("\nCurrent tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Todo"
        print(f"{index}. [{status}] {task['title']} - {task['notes']}")


def add_task(tasks: list[dict]) -> None:
    title = input("Task title: ").strip()
    notes = input("Notes: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    tasks.append({"title": title, "notes": notes or "No notes", "done": False})
    print("Task added.")


def choose_task_index(tasks: list[dict], action: str) -> int | None:
    if not tasks:
        print("No tasks available.")
        return None

    list_tasks(tasks)
    raw_value = input(f"Which task do you want to {action}? ").strip()

    if not raw_value.isdigit():
        print("Please enter a number.")
        return None

    index = int(raw_value) - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range.")
        return None

    return index


def complete_task(tasks: list[dict]) -> None:
    index = choose_task_index(tasks, "mark as done")
    if index is None:
        return

    tasks[index]["done"] = True
    print("Task marked as done.")


def delete_task(tasks: list[dict]) -> None:
    index = choose_task_index(tasks, "delete")
    if index is None:
        return

    removed = tasks.pop(index)
    print(f"Deleted: {removed['title']}")


def show_stats(tasks: list[dict]) -> None:
    total = len(tasks)
    done = sum(task["done"] for task in tasks)
    pending = total - done
    print(f"Total: {total}")
    print(f"Done: {done}")
    print(f"Pending: {pending}")


def main() -> None:
    data_file = Path(DEFAULT_DATA_FILE)
    tasks = load_tasks(data_file)
    print(f"Data file: {data_file.name}")

    while True:
        print_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(data_file, tasks)
        elif choice == "3":
            complete_task(tasks)
            save_tasks(data_file, tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(data_file, tasks)
        elif choice == "5":
            show_stats(tasks)
        elif choice == "0":
            save_tasks(data_file, tasks)
            print("Bye.")
            break
        else:
            print("Unknown option. Please choose 0-5.")


if __name__ == "__main__":
    main()
