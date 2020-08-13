from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import UserModel


class UserView(APIView):

    def get(self, request):
        data = UserModel.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
