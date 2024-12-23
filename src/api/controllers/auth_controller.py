from models.data_classes.auth import Auth
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from infrastructures.interfaces.icontroller_manager import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.zmq_response import Response
from models.data_classes.zmq_request import Request


class AuthController(IControllerManager):
    def __init__(self, data_zmq_client: IZMQClientManager):
        self._data_zmq_client = data_zmq_client

    def login(self, username: str, password: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.auth_resource,
            operation=ZMQConstStrings.login_operation,
            data={
                ConstStrings.username_key: username,
                ConstStrings.password_key: password,
            }
        )
        return self._data_zmq_client.send_request(request)    
    
    def register(self, user: Auth) -> Response:
        request = Request(
            resource=ZMQConstStrings.auth_resource,
            operation=ZMQConstStrings.register_operation,
            data={
                ConstStrings.auth_key: user
            }
        )
        print("bl", request.data)
        return self._data_zmq_client.send_request(request)
