
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer

class PublicView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"message": "Hello, world!"})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({"user": serializer.data})
