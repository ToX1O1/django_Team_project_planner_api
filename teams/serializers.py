from teams.models import Team
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        # Override create method to handle admin user id
        admin_id = validated_data.pop('admin')
        team = Team.objects.create(admin_id=admin_id, **validated_data)
        return team
