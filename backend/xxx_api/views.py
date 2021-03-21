from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, viewsets, generics
from django_celery_results.models import TaskResult
from xxx_api.tasks import do_something, do_parse_resource
from xxx_api.serializers import (
    ResourceRequestSerializer,
    BinaryResourceSerializer,
    BinaryResourceHeavySerializer,
    ParseResultSerializer,
)
from xxx_api.models import BinaryResource, ParseResult
from xxx_api.utils import do_index_to_column_name, is_exists_model_field
import pandas as pd
import io


class DoBackground(APIView):
    permission_classes = (permissions.AllowAny,)
    # http_method_names = ['get', 'post']
    http_method_names = ["get", "head"]

    def get(self, request, format=None):
        task_id = do_something.delay("any_params")
        return Response("start do something")

    # def post(self, request, format=None):
    #     return Response("Any")


class ResourceControl(APIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ["post", "get", "head"]
    # serializer_class = ResourceRequestSerializer

    def get(self, request):
        msg = r"resource_id: cc42c989-6813-456f-87ab-16858ef38fd9"
        return Response(f"postでresource_idを渡してください。例：{msg}", status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print(request.data)
        serializer = ResourceRequestSerializer(data=request.data)
        if serializer.is_valid():
            resource_id = serializer.validated_data["resource_id"]
            do_parse_resource.delay(resource_id)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BinaryResourceAPIView(generics.ListAPIView):
    """BinaryResourceのデータを取得するAPIです。
    バイナリデータは含まれません
    バイナリデータが必要な場合、BinaryHeavyResourceAPIViewを利用している
    v1/binary_heavy_resourcesにアクセスしてください
    """

    queryset = BinaryResource.objects.all()
    serializer_class = BinaryResourceSerializer
    permission_classes = (permissions.AllowAny,)


class BinaryHeavyResourceAPIView(generics.ListAPIView):
    """BinaryResourceのデータを取得するAPIです。
    バイナリデータを含むためパフォーマンスに注意してください。
    """

    queryset = BinaryResource.objects.all()
    serializer_class = BinaryResourceHeavySerializer
    permission_classes = (permissions.AllowAny,)


class ParseResultAPIView(generics.ListAPIView):
    """ParseResult用のデータを取得するAPIです"""

    queryset = ParseResult.objects.all()
    serializer_class = ParseResultSerializer
    permission_classes = (permissions.AllowAny,)


# class ResourceSpec(APIView):
#     permission_classes = (permissions.AllowAny,)
#     http_method_names = ["post", "get", "head"]
#
#     def get(self, request):
#         pk = "cc42c989-6813-456f-87ab-16858ef38fd9"
#         resource = BinaryResource.objects.get(id=pk)
#         df = pd.read_excel(io.BytesIO(resource.binary_data))
#
#         spec_task_result = TaskResult.objects.get(pk=1)
#
#         for index, row in df.iterrows():
#             result = ParseResult()
#             result.header = df.columns
#             for i in range(row.size):
#                 field_name = do_index_to_column_name(i + 1)
#                 if is_exists_model_field(ParseResult, field_name):
#                     # 結果オブジェクトの各汎用項目を設定する
#                     result.__setattr__(field_name, row[i])
#             result.mq_info = spec_task_result
#             result.save()
#
#         return Response("hoge")
