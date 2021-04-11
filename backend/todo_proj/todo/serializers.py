from django.contrib.auth.models import User, Group
from todo.models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import copy

class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = models.CharField(unique=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )


    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        val_data = copy.deepcopy(validated_data)
        instance = User.objects.create(**val_data)
        return instance

    def update(self, instance, validated_data):
        val_data = copy.deepcopy(validated_data)
        for key, value in val_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class TODOSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter())
    title = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    description = serializers.CharField(required=True, allow_blank=False, allow_null=False)

    class Meta:
        model = TODO
        fields = ['id', 'user', 'title', 'description']
