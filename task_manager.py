import argparse
import json
import uuid
import datetime
import pathlib


def save_task(description: str) -> None:
    json_path = pathlib.Path("tasks.json")
    if not json_path.exists():
        json_path.touch()

    tasks = []
    
    if json_path.exists() and json_path.stat().st_size > 0:
        try:
            tasks = json.load(json_path.open('r', encoding='utf-8'))
        except json.JSONDecodeError as e:
            print(f"Error while opening json file: {str(e)}")
            return

    new_task = {
        'id': str(uuid.uuid4()),
        'description': description,
        'status': "pending",
        'created_at': datetime.datetime.now().isoformat()
    }
    tasks.append(new_task)

    with json_path.open('w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="managing the to-do list")
    subparsers = parser.add_subparsers(dest='command', help='available commands')

    parser_add = subparsers.add_parser('add', help='add a new task')
    parser_add.add_argument('description', type=str, help="task description")

    args = parser.parse_args()

    if args.command == "add":
        save_task(args.description)
        print(f'Task "{args.description}" added!')