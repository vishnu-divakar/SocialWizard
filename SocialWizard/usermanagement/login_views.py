from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class LoginView(ObtainAuthToken):

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data, context={'request': request})
        if(serializer.is_valid()):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user = user)
            return Response(
                {
                    'token' : token.key,
                    'user_id': user.pk,
                    'email': user.email,
                    'username': user.username
                },
                status = status.HTTP_200_OK
            )
        return Response(serializer.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
