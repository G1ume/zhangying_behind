import sys

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from myApp.components.err import RequestMethodErr
from myApp.models import User


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
            if User.objects.filter(id=id).count() == 1:
                test1 = User.objects.get(id=id)
                if test1.upwd == pwd:
                    return JsonResponse({"result": 0, "message": "登陆成功", "userInfo": {"uid": id, "un": test1.un}})
                else:
                    return JsonResponse({"result": 1, "message": "登陆失败，密码错误"})
            else:
                return JsonResponse({"result": 1, "message": "用户不存在"})
        else:
            return JsonResponse({"result": 1, "message": "登录失败，请输入完整的账号和密码信息"})
    else:
        err = RequestMethodErr(request.POST.get("uid"), sys._getframe().f_code.co_name, request.method)
        return err.response()


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
                return JsonResponse({"result": 2, "message": "Password or UerName out of length!"})
            else:
                if (-2147483648 <= int(new_uid) <= 2147483648) and User.objects.filter(uid=new_uid).count() == 0:
                    User(id=new_uid, password=new_pwd, name=new_un, avatar=None).save()
                    return JsonResponse({"result": 0, "message": "注册成功！"})
                else:
                    return JsonResponse({"result": 2, "message": "User existed!"})
        else:
            return JsonResponse({"result": 2, "message": "UerId or Password is Empty!"})
    else:
        err = RequestMethodErr(request.POST.get("uid"), sys._getframe().f_code.co_name, request.method)
        return err.response()
