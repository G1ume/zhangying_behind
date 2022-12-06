from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from myApp.models import *
import json


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        # data_json = json.loads(request.body)
        # id = data_json["uid"]
        # pwd = data_json["upwd"]
        id = request.POST.get("uid")
        pwd = request.POST.get("upwd")
        # return JsonResponse({"result": 1, "message": str(id)+str(pwd)})
        if id and pwd:
            if MyUser.objects.filter(uid=id).count() == 1:
                test1 = MyUser.objects.get(uid=id)
                if test1.upwd == pwd:
                    return JsonResponse({"result": 1, "message": "登陆成功", "userInfo": {"uid": id, "un": test1.un}})
                else:
                    return JsonResponse({"result": 0, "message": "登陆失败，密码错误"})
            else:
                return JsonResponse({"result": 0, "message": "用户不存在"})
        else:
            return JsonResponse({"result": 0, "message": "登录失败，请输入完整的账号和密码信息"})
    else:
        return JsonResponse({"result": 0, "message": "Wrong Request Method: " + request.method})


def main(request):
    pass


@csrf_exempt
def register(request):
    if request.method == 'POST':
        new_uid = request.POST.get("nuid")
        new_pwd = request.POST.get("npwd")
        new_un = request.POST.get("nun")
        if new_un == '' or new_un is None:
            new_un = 'User' + str(new_uid)
        if new_uid and new_pwd:
            if len(new_pwd) > 16 or len(new_un) > 16:
                return JsonResponse({"result": 0, "message": "Password or UerName out of length!"})
            else:
                if (-2147483648 <= new_uid <= 2147483648) and MyUser.objects.filter(uid=new_uid).count() == 0:
                    MyUser(uid=new_uid, upwd=new_pwd, un=new_un).save()
                    return JsonResponse({"result": 1, "message": "注册成功！"})
                else:
                    return JsonResponse({"result": 0, "message": "UserId existed!"})
        else:
            return JsonResponse({"result": 0, "message": "UerId or Password is Empty!"})
    else:
        return JsonResponse({"result": 0, "message": "Wrong Request Method: " + request.method})


@csrf_exempt
def init(request):
    zhqy = MyUser(uid=0, upwd='woshizhqy', un='zhqy')
    zy = MyUser(uid=1, upwd='193939', un='zy')
    zhqy.save()
    zy.save()
    return JsonResponse({"message": "zhqy 和 zy 注册成功!"})
