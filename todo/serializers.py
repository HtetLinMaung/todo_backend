from rest_framework import serializers
from .models import Todo

# Serializer
# class TodoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(
#         required=True, allow_blank=False, max_length=200)
#     description = serializers.CharField(required=True, allow_blank=False)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Todo` instance, given the validated data.
#         """
#         return Todo.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Todo` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.save()
#         return instance

# ModelSerializer


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'done']
