import argparse


def save_task(description: str) -> None:
    import json
    import uuid
    import datetime
    import pathlib

    json_path = pathlib.Path("tasks.json")
    if not json_path.exists():
        json_path.touch()

    data = {
        'id': str(uuid.uuid4()),
        'description': description,
        'status': "pending",
        'created_at': datetime.datetime.now().isoformat()
    }

    with json_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

parser = argparse.ArgumentParser(description="managing the to-do list")
subparsers = parser.add_subparsers(dest='command', help='available commands')

parser_add = subparsers.add_parser('add', help='add a new task')
parser_add.add_argument('description', type=str, help="task description")

args = parser.parse_args()

if args.command == "add":
    save_task(args.description)
    print(f'Task "{args.description}" added!')