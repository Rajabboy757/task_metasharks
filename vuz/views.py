from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from vuz.models import User, Direction, StudentGroup, Subject
from vuz.serializers import UserSerializer, UserRegister, DirectionSerializer, GroupSerializer, SubjectSerializer
from vuz.permissions import AdminPermission


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, AdminPermission,)
    http_method_names = ('post', 'get', 'delete', 'patch')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRegister


class DirectionViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAuthenticated, AdminPermission,)
    http_method_names = ('post', 'get', 'delete', 'patch')


class GroupViewSet(ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,) #CuratorPermission
    http_method_names = ('post', 'get', 'delete', 'patch')


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, AdminPermission)
    http_method_names = ('post', 'get', 'delete', 'patch')