from rest_framework.views import APIView
from usermanagement.models import UserModel
from usermanagement.serializer import UserModelSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
import traceback

class SignUp(APIView):

    def post(self, request, format = None):
        
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        dob = request.data['dob']
        education = request.data['education']
        interest = request.data['interest']
        relation_status = request.data['relation_status']

        try:
            user = User.objects.create_user(
                username = username, 
                password = password, 
                email = email, 
                first_name = first_name,
                last_name = last_name
            )
            user.save()
            Token.objects.get_or_create(user = user)
            payload = {
                "user": user.id,
                "dob": dob,
                "education" : education,
                "interest": interest,
                "relation_status": relation_status
            }
            serializer = UserModelSerializer(data = payload)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        except IntegrityError:
            return Response({"user": "already exists"}, status = status.HTTP_406_NOT_ACCEPTABLE) 
        except Exception as err:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)