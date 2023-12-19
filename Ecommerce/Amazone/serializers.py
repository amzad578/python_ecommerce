from rest_framework import  serializers

from . models import *

# Serializers define the API representation.
class registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = registration
        fields = '__all__'