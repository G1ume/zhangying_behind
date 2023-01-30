import sys

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myApp.components.err import RequestMethodErr
from myApp.components.chapter import MyChapter

from myApp.models import *
import json


# Create your views here.


def main(request):
    pass




def test(request):
    if request.method == 'POST':
        # request.POST.get('uid')
        selectInfo = _analyse_select_info(request.POST.get('select'))
        # print(selectInfo)
        return JsonResponse({"result": 0, "message": selectInfo})
    err = RequestMethodErr(request.POST.get("uid"), sys._getframe().f_code.co_name, request.method)
    return err.response()





def get_qlist(request):
    if request.method == 'POST':

        pass
    else:
        err = RequestMethodErr(request.POST.get("uid"), sys._getframe().f_code.co_name, request.method)
        return err.response()

