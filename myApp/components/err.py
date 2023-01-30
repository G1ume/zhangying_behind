from abc import ABC, abstractmethod
from django.http import JsonResponse


class Error(ABC):
    def __init__(self, user_id: -1, position: -1):
        self.user_id = user_id
        self.position = position

    @abstractmethod
    def response(self):
        pass

    def err_info(self):
        return "at \"{}\" by user[{}]".format(self.position, self.user_id)


class RequestMethodErr(Error):
    def __init__(self, user_id, position, err_msg: None):
        super().__init__(user_id, position)
        self.err_msg = err_msg

    def response(self):
        return JsonResponse({"result": 1, "message": "Error! Wrong Request Method: " + self.err_msg})
