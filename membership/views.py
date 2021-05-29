from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Member, Discharge
from .serializers import MemberSerializer, DischargeSerializer
# Create your views here.

# Create your views here.
# 문자열을 반환하는 API
@api_view(['GET'])
def helloAPI(request):
    return Response ("hello world!")

# 사용자 리스트 API
@api_view(['GET'])
def userList(request):
    users = Member.objects.all()
    serializer =MemberSerializer(users, many=True)
    return Response(serializer.data)

# 개인별 사용자 정보 제공 API - 사용자 포인트 정보 화면에 필요
@api_view(['GET'])
def getUser(request, id):
    userInfo = Member.objects.get(phone=id)
    serializer = MemberSerializer(userInfo)
    return Response(serializer.data)

@api_view(['GET'])
def getRank(request):
    rank = Member.objects.order_by('-points')
    serializer = MemberSerializer(rank, many=True)
    return Response(serializer.data)


