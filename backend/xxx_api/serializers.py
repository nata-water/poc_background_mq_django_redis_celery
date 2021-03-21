from rest_framework import serializers
from xxx_api.models import BinaryResource, ParseResult
import uuid


class ResourceRequestSerializer(serializers.Serializer):
    resource_id = serializers.UUIDField(default=uuid.uuid4())


class BinaryResourceSerializer(serializers.ModelSerializer):
    """BinaryResourceモデル用のシリアライザクラスです"""

    class Meta:
        model = BinaryResource
        exclude = ["binary_data"]

    def create(self, validated_data):
        return BinaryResource.objects.create(validated_data)


class BinaryResourceHeavySerializer(serializers.ModelSerializer):
    """BinaryResourceモデル用のシリアライザクラスです
    バイナリデータの実体を含みます
    """

    class Meta:
        model = BinaryResource
        fields = "__all__"


class ParseResultSerializer(serializers.ModelSerializer):
    """ParseResultモデル用のシリアライザクラスです"""

    class Meta:
        model = ParseResult
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")

    def create(self, validated_data):
        return ParseResult.objects.create(validated_data)
