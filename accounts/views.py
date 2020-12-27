from django.contrib.auth import logout as django_logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer, JWTUserLoginSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly


class RegisterUser(GenericAPIView):
    """GenericAPIView to register a new user, used genericAPIVies instead ApiView as openapi doesn't support it """
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serialize_data = self.serializer_class(data=request.data)

        if serialize_data.is_valid():
            serialize_data.save()
            return Response({'message': 'Account created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize_data.errors, status=status.HTTP_400_BAD_REQUEST)


class JWTUserLoginView(GenericAPIView):
    """GenericApiView for use login and JWT generation"""
    permission_classes = (AllowAny,)
    serializer_class = JWTUserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


class LogoutApiView(APIView):
    """Logout ApiView """
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request):
        django_logout(request)
        return Response(status=204)
