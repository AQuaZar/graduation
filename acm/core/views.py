from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .models import Attendance


class AccessView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            "message": f"Access granted to {request.user.first_name} {request.user.last_name}"
        }
        visit = Attendance(student=request.user.student)
        visit.save()
        return Response(content)


class CustomAuthToken(ObtainAuthToken):

    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})
