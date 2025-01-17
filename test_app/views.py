from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from drf_spectacular.utils import OpenApiParameter, extend_schema
from drf_spectacular.types import OpenApiTypes
from rest_framework.viewsets import GenericViewSet

from rest_framework.decorators import action
from test_app.send_base import SendBase


class TestView(GenericViewSet):
    @extend_schema(
        parameters=[
            OpenApiParameter('name', OpenApiTypes.STR, OpenApiParameter.QUERY),
        ],
    )
    @action(detail=False, methods=['get'])
    def set_name(self, request):
        name = self.request.query_params.get('name')

        task = SendBase(task_name='TestRC.task.add_name',args=[name])
        result = task.get_result()

        return JsonResponse({'message':result })

    @extend_schema(
        parameters=[
            OpenApiParameter('age', OpenApiTypes.STR, OpenApiParameter.QUERY),
        ]
    )
    @action(detail=False, methods=['get'])
    def set_age(self, request):
        age = self.request.query_params.get('age')

        task = SendBase(task_name='TestRC.task.add_age',args=[age], priority=6)
        result = task.get_result()

        return JsonResponse({'message':result })

class SecondTestView(GenericViewSet):
    @extend_schema(
        parameters=[
            OpenApiParameter('cost', OpenApiTypes.STR, OpenApiParameter.QUERY),
        ],
    )
    @action(detail=False, methods=['get'])
    def second_set_cost(self, request):
        cost = self.request.query_params.get('cost')

        task = SendBase(task_name='SecondTestRC.task.add_cost',args=[cost])
        result = task.get_result()

        return JsonResponse({'message': result})
    @extend_schema(
        parameters=[
            OpenApiParameter('value', OpenApiTypes.STR, OpenApiParameter.QUERY),
        ]
    )
    @action(detail=False, methods=['get'])
    def second_set_bool(self, request):
        value = self.request.query_params.get('value')

        task = SendBase(task_name='SecondTestRC.task.add_bool',args=[value])
        result = task.get_result()

        return JsonResponse({'result': result})

    @action(detail=False, methods=['get'])
    def always_200(self,request):
        return Response()