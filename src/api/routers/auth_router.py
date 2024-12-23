from typing import Any

from api.routers.base_router import BaseRouter
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from models.data_classes.zmq_response import Response


class AuthRouter(BaseRouter):
    def __init__(self, resource, ctrl):
        super().__init__(resource, ctrl)
        self._setup_operations()

    def _setup_operations(self):
        self._operations = {
            ZMQConstStrings.login_operation: self.login,
            ZMQConstStrings.register_operation: self.register
        }

    def register(self, data: Any) -> Response:
        print("in register route")
        user = data.get(ConstStrings.auth_key)
        return self._ctrl.register(user)
    
    def login(self, data: Any) -> Response:
        username = data.get(ConstStrings.username_key)
        password = data.get(ConstStrings.password_key)
        return self._ctrl.login(username, password)
    

