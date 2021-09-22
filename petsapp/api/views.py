
from rest_framework.decorators import api_view
from petsapp.models import Account
from petsapp.api.serializers import AccountRegisterSerializer,AccountLoginSerializer
from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from django.contrib.auth.hashers import make_password
from django.conf import settings


class AccountRegisterView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRegisterSerializer
    # parser_classes = [JSONParser,MultiPartParser,FormParser]


@api_view(['POST'])
def login_view(request):
    if request.method=='POST':
        AccountLoginSerializer(data=request.data)

        require_fields = {
            "email" : "email"
        }

        qs_fields_data = {}

        for k,v  in require_fields.items():
            qs_fields_data[v] = request.data.get(k)

        pwd = request.data.get('password') # admin123

        password = make_password(pwd, salt=settings.SECRET_KEY) # 'adsdd544fdfs...'

        qs_fields_data['password'] = password

        account_instance = Account.objects.filter(**qs_fields_data) # object memory | None

        response = {}

        if account_instance:
            response['message'] = "User successfully Login"
            response['status'] = status.HTTP_200_OK
            return Response(response, status=status.HTTP_200_OK)
        else:
            response['message'] = "You have entered an invalid username|password"
            response['status'] = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status.HTTP_400_BAD_REQUEST)














