from rest_framework import serializers
from .models import Todo
from django.utils.timesince import timesince

class TodoSerializer(serializers.ModelSerializer):
  time_since_last_update = serializers.SerializerMethodField()
  class Meta: 
    model = Todo
    fields = "__all__"
    # fields = ['id',"task",'completed']
  def get_time_since_last_update(self, obj):
        return timesince(obj.updated_at)
