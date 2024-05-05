from rest_framework import serializers
from .models import Clv

class ClvSerializer(serializers.ModelSerializer):
  class Meta:
    model = Clv
    fields = '__all__'