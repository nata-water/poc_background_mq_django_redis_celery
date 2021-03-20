from rest_framework import serializers
import uuid


class ResourceRequestSerializer(serializers.Serializer):
    resource_id = serializers.UUIDField(default=uuid.uuid4())
