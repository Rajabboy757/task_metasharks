from rest_framework import serializers
from vuz.models import User, StudentGroup, Direction, Subject
from rest_framework.validators import ValidationError


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('name', 'student_count', 'group_direction')


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ('name',)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', 'direction_subject')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRegister(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('password1', 'password2', 'username', 'type', 'direction_curator')

        extra_kwargs = {

        }

    def create(self, validated_data):
        password1 = validated_data.pop('password1')
        password2 = validated_data.pop('password2')
        if password1 == password2:
            validated_data["password"] = password1
        else:
            raise ValidationError({'detail': 'password1 != password2'})
        instance = super().create(validated_data)
        instance.set_password(password1)
        instance.save()
        return instance
