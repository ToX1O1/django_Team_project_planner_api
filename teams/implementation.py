from .team_base import TeamBase
from .models import Team , TeamUser
from users.models import User as AuthUser
import json
from django.core.exceptions import ObjectDoesNotExist
from .serializers import TeamSerializer

class TeamImplementation(TeamBase):
    def create_team(self, request: str) -> str:
        data = json.loads(request)
        admin_id = data.pop('admin')
        try:
            admin = AuthUser.objects.get(id=admin_id)
        except ObjectDoesNotExist:
            raise ValueError("Admin user does not exist.")
        
        try :
            team = Team.objects.create(admin=admin,**data)
        except Exception as e:
            raise ValueError("Error",e)
        
        TeamUser.objects.create(team=team,user=admin)
        return json.dumps({"id": team.id})

    def list_teams(self) -> str:
        teams = Team.objects.all()
        response = []
        for team in teams:
            response.append({
                "name": team.name,
                "description": team.description,
                "creation_time": team.creation_time.strftime("%Y-%m-%d %H:%M:%S"),
                "admin": team.admin.id
            })
        return response

    def describe_team(self, data: str) -> str:

        team_id = data['id']
        try:
            team = Team.objects.get(id=team_id)
            ser = TeamSerializer(team)
            team = ser.data

        except ObjectDoesNotExist:
            raise ValueError("Team does not exist.")
        return ({
            "name": team['name'],
            "description": team['description'],
            "admin": team['admin']
        })

    def update_team(self, data: str) -> str:
        team_id = data['id']
        team_data = data['team']
        name = team_data['name']
        description = team_data['description']
        admin_id = team_data['admin']
        try:
            admin = AuthUser.objects.get(id=admin_id)
        except ObjectDoesNotExist:
            raise ValueError("Admin user does not exist.")
        try:
            team = Team.objects.get(id=team_id)
        except ObjectDoesNotExist:
            raise ValueError("Team does not exist.")
        team.name = name
        team.description = description
        team.admin = admin
        team.save()

    def add_users_to_team(self, data: str):
        team_id = data['id']
        users = data['users']
        try:
            team = Team.objects.get(id=team_id)
        except ObjectDoesNotExist:
            raise ValueError("Team does not exist.")
        if len(users) > 50:
            raise ValueError("Cannot add more than 50 users to a team.")
        for user_id in users:
            try:
                user = AuthUser.objects.get(id=user_id)
            except ObjectDoesNotExist:
                raise ValueError(f"User with id {user_id} does not exist.")
            TeamUser.objects.create(team=team, user=user)

    def remove_users_from_team(self, data: str):
        team_id = data['id']
        users = data['users']
        try:
            team = Team.objects.get(id=team_id)
        except ObjectDoesNotExist:
            raise ValueError("Team does not exist.")
        for user_id in users:
            try:
                user = AuthUser.objects.get(id=user_id)
            except ObjectDoesNotExist:
                raise ValueError(f"User with id {user_id} does not exist.")
            try:
                team_user = TeamUser.objects.get(team=team, user=user)
                team_user.delete()
            except ObjectDoesNotExist:
                pass

    def list_team_users(self, data: str):
    
        team_id = data['id']
        try:
            team = Team.objects.get(id=team_id)
        except ObjectDoesNotExist:
            raise ValueError("Team does not exist.")
        
        
        team_users = TeamUser.objects.filter(team=team)

        # Prepare the response data
        users_list = []
        for team_user in team_users:
            user_data = {
                "id": team_user.user.id,
                "name": team_user.user.name,
                "display_name": team_user.user.display_name
            }
            users_list.append(user_data)

        return (users_list)
