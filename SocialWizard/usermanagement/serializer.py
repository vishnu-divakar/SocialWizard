from rest_framework import serializers
from usermanagement.models import UserModel

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'user', 'dob', 'education', 'interests', 'relation_status')