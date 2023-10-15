from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommonSerializer


class CommonRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = CommonSerializer

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        common = self.get_object()
        serializer = self.get_serializer(common, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
