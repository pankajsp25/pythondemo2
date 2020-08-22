from rest_framework import generics

# Create your views here.
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from accounts.serializers import AccountCreateSerializer


class AccountCreateView(generics.GenericAPIView):
    serializer_class = AccountCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": AccountCreateSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.create(user=user).key
        })
