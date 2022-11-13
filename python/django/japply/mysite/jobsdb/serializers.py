
from rest_framework import serializers
from .models import Jobs_db

class JobsDbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobs_db
        fields = ("id", "title", "link", "time")

