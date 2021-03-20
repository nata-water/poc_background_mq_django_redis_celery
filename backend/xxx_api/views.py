from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from xxx_api.tasks import do_something


class DoBackground(APIView):
    permission_classes = (permissions.AllowAny,)
    # http_method_names = ['get', 'post']
    http_method_names = ["get", "head"]

    def get(self, request, format=None):
        task_id = do_something.delay("any_params")
        return Response("start do something")

    # def post(self, request, format=None):
    #     return Response("Any")
