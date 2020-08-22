from django.contrib.auth.models import User
from rest_framework import serializers


class AccountCreateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'],
        )

        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save(update_fields=['first_name', 'last_name'])

        return user

