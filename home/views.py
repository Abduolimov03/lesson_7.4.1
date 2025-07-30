from django.shortcuts import render
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Watch
from .serializers import WatchSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework import mixins

### genericAPIView
# class ListCreateApi(GenericAPIView):
#     queryset = Watch.objects.all()
#     serializer_class = WatchSerializer
#
#     def get(self, request):
#         watchs = self.get_queryset()
#         serializer = self.get_serializer(watchs, many=True)
#         data = {
#             'data':serializer.data,
#             'count':len(watchs),
#             'status':status.HTTP_200_OK
#         }
#         return Response(data)
#
#     def post(self, request):
#         serializer = WatchSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':status.HTTP_200_OK})
#         return Response({'status':status.HTTP_400_BAD_REQUEST})
#
#
# class DetailDeleteUpdateApi(GenericAPIView):
#     queryset = Watch.objects.all()
#     serializer_class = WatchSerializer
#
#     def get(self, request, pk):
#         watch = Watch.objects.get(id=pk)
#         return watch
#
#
#     def get(self, request, pk):
#         watch = self.get_object()
#         serializer = WatchSerializer(watch)
#         data = {
#             'data':serializer.data,
#             'status':status.HTTP_200_OK
#         }
#         return Response(data)
#
#     def put(self, request, pk):
#         watch = Watch.objects.get(pk=pk)
#         serializer = WatchSerializer(watch, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':status.HTTP_200_OK})
#         return Response({'status':status.HTTP_400_BAD_REQUEST})
#
#     def patch(self, request, pk):
#         watch = Watch.objects.get(pk=pk)
#         serializer = WatchSerializer(watch, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':status.HTTP_200_OK})
#         return Response({'status':status.HTTP_400_BAD_REQUEST})
#
#     def delete(self, request, pk):
#         try:
#             watch = Watch.objects.get(id=pk)
#         except Watch.DoesNotExist:
#             return Response({'status':status.HTTP_400_BAD_REQUEST})
#         watch.delete()
#         return Response({'status':status.HTTP_200_OK})


### mixins

class ListCreateApi(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class DetailDeleteUpdateApi(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer

    def get(self, request, pk):
        return self.retrieve(request, id=pk)

    def delete(self, request, pk):
        return self.destroy(request, id=pk)

    def put(self, request, pk):
        return self.update(request, id=pk)

    def patch(self, request, pk):
        return self.update(request, id=pk)

