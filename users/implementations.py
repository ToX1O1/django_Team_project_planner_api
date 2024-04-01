from .user_base import UserBase
from .models import User
import json
from django.utils import timezone

class UserImplementation(UserBase):
    def create_user(self, request: str) -> str:
        data = json.loads(request)
        name = data.get('name')
        display_name = data.get('display_name')
        
        if not name or not display_name:
            raise ValueError("Name and display name are required fields.")
        
        if len(name) > 64:
            raise ValueError("Name cannot be more than 64 characters.")
        
        if len(display_name) > 64:
            raise ValueError("Display name cannot be more than 64 characters.")
        
        user = User.objects.create(name=name, display_name=display_name, creation_time=timezone.now())
        return json.dumps({"id": str(user.id)})

    def list_users(self) -> str:
        users = User.objects.all()
        return users

    def describe_user(self, data: str) -> str:
        user_id = data.get('id')
        
        if not user_id:
            raise ValueError("User ID is required.")
        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValueError(f"User with ID {user_id} does not exist.")
        
        return json.dumps({
            "name": user.name,
            "description": user.description,
            "creation_time": user.creation_time.strftime("%Y-%m-%d %H:%M:%S")
        })

    def update_user(self, data: str) -> str:
        
        user_id = data.get('id')
        user_data = data.get('user')
        
        if not user_id:
            raise ValueError("User ID is required.")
        
        if not user_data:
            raise ValueError("User data is required.")
        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValueError(f"User with ID {user_id} does not exist.")
        
        display_name = user_data.get('display_name')
        
        if len(display_name) > 128:
            raise ValueError("Display name cannot be more than 128 characters.")
        
        user.display_name = display_name
        user.save()
        
        return json.dumps({"success": True})

    def get_user_teams(self, request: str) -> str:
        data = json.loads(request)
        user_id = data.get('id')
        
        if not user_id:
            raise ValueError("User ID is required.")
        
        # Assuming you have a relationship between User and Team models
        user = User.objects.get(id=user_id)
        teams = user.teams.all()
        
        team_list = []
        for team in teams:
            team_list.append({
                "name": team.name,
                "description": team.description,
                "creation_time": team.creation_time.strftime("%Y-%m-%d %H:%M:%S")
            })
        
        return json.dumps(team_list)
