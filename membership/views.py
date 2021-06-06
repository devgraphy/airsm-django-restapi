from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Member, Discharge
from .serializers import MemberSerializer, DischargeSerializer
from django.core.exceptions import ObjectDoesNotExist
import json
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
    serializer = MemberSerializer(users, many=True)
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
    print(rank)
    return Response(serializer.data)

# 회원가입
@api_view(['POST'])
def memberCreate(request):
    print(request.data)
    p = request.data.get('phone')
    try:                        # 계정이 존재하면
        obj = Member.objects.get(phone=p)
    except ObjectDoesNotExist:  # 계정이 존재하지 않으면
        serializer = MemberSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response("회원가입에 성공하였습니다.",status=200)
        else:
            return Response("올바르지 않은 데이터입니다.",status=400)

    if(len(obj.password) > 1):
            return Response("이미 가입한 계정입니다.", status=400)
    else:
        obj.password = request.data.get('password')
        obj.name = request.data.get('name')
        obj.save()
        return Response("회원가입에 성공하였습니다.",status=200)    

# 로그인
@api_view(['POST'])
def login(request):
    print(request.data)
    # value 추출
    # phone이 DB에 존재하는지 여부
    p = request.data.get('phone')
    print(p)
    pw = request.data.get('password')
    print(pw)
    if(Member.objects.get(phone=p)):
        m = Member.objects.get(phone=p)
        if(pw == m.password):
            print(m.password)
            serializer = MemberSerializer(m)
            return Response(serializer.data,200)
    else:
        return Response("no",status=400)

@api_view(['POST'])
def point(request):
    num = 50
    p = request.data.get('phone')
    print(request)
    try:
        obj = Member.objects.get(phone=p)

    except ObjectDoesNotExist:
        serializer = MemberSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
        obj = Member.objects.get(phone=p)
    obj.points+=num
    obj.save()
    return Response(num, status=200)
        