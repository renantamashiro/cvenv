from rest_framework import serializers

from .models.logs import Log, Group, Level


class LogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = [
            'id',
            'title',
            'description', 
            'date_published',
            'events',
            'user',
            'level',
            'group',
        ]


class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name'
        ]


class LevelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = [
            'name'
        ]
