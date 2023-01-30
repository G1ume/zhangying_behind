from myApp.models import Chapter
from myApp.components.err import *
import sys


def _analyse_select_info(select_info: str):
    tmp = select_info.split(";")
    result = []
    for item in tmp:
        result.append(item.split(","))
    return result


def add_chapter(request):
    if request.method == 'POST':
        user_id = request.POST.get("uid")
        top = request.POST.get("top")
        name = request.POST.get("name")
        new_chapter_id = Chapter.objects.filter().count() + 1
        Chapter(id=str(new_chapter_id), user=user_id, top=top, name=name).save()
        return JsonResponse(
            {"result": 0, "message": "New Chapter Is Created Successfully!", "chapterId": str(new_chapter_id)})
    else:
        err = RequestMethodErr(request.POST.get("uid"), sys._getframe().f_code.co_name, request.method)
        return err.response()
