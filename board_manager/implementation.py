from .models import Board, Task
from .project_board_base import ProjectBoardBase
import json
import os

class ProjectBoardImplementation(ProjectBoardBase):

    def create_board(self, request: str):
        data = json.loads(request)
        name = data.get('name')
        description = data.get('description')
        team_id = data.get('team_id')

        # Implement validation logic here
        
        board = Board.objects.create(name=name, description=description, team_id=team_id)
        return {"id": board.id}

    def close_board(self, request: str) -> str:
        data = json.loads(request)
        board_id = data.get('id')

        # Implement logic to check if all tasks are complete

        board = Board.objects.get(id=board_id)
        board.status = 'CLOSED'
        board.save()
        return "Board closed successfully."

    def add_task(self,request: str) -> str:
        data = json.loads(request)
        title = data.get('title')
        description = data.get('description')
        board_id = data.get('user_id')
        board = Board.objects.get(id=board_id)
        # Implement validation logic here

        task = Task.objects.create(title=title, description=description, board=board)
        return {"id": task.id}

    def update_task_status(self, request: str):
        data = json.loads(request)
        task_id = data.get('id')
        status = data.get('status')

        # Implement validation logic here

        task = Task.objects.get(id=task_id)
        task.status = status
        task.save()
        return "Task status updated successfully."

    def list_boards(self, request: str) -> str:
        data = json.loads(request)
        team_id = data.get('id')

        # Implement logic to list all boards for a team
        boards = Board.objects.filter(team=team_id)
        board_list = [{"id": board.id, "name": board.name} for board in boards]
        return board_list

    def export_board(self, request: str) -> str:
        data = json.loads(request)
        board_id = data.get('id')

        try:
            board = Board.objects.get(id=board_id)
        except Board.DoesNotExist:
            raise ValueError("Board does not exist.")

        file_name = f"board_{board_id}.txt"
        file_path = os.path.join("out", file_name)

        with open(file_path, "w") as file:
            file.write(f"Board Name: {board.name}\n")
            file.write(f"Description: {board.description}\n")
            file.write("Tasks:\n")
            for task in board.task_set.all():
                file.write(f"- {task.title}: {task.description}\n")

        return {"out_file": file_name}
