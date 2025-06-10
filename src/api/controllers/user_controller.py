from models.data_classes.login_user import LoginUser
from models.data_classes.user import User
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from infrastructures.interfaces.icontroller_manager import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.zmq_response import Response
from models.data_classes.zmq_request import Request


class UserController(IControllerManager):
    def __init__(self, data_zmq_client: IZMQClientManager):
        self._data_zmq_client = data_zmq_client

    def login(self, user: LoginUser) -> Response:
        request = Request(
            resource=ZMQConstStrings.auth_resource,
            operation=ZMQConstStrings.login_operation,
            data={
                ConstStrings.user_key: user
            }
        )
        print("before send")
        return self._data_zmq_client.send_request(request)

    def register(self, user: User) -> Response:
        request = Request(
            resource=ZMQConstStrings.auth_resource,
            operation=ZMQConstStrings.register_operation,
            data={
                ConstStrings.user_key: user
            }
        )
        return self._data_zmq_client.send_request(request)

    def get_all_users(self) -> Response:
        request = Request(
            resource=ZMQConstStrings.auth_resource,
            operation=ZMQConstStrings.get_all_users_operation,
            data={}
        )
        return self._data_zmq_client.send_request(request)

    def get_user_by_id(self, user_id: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.auth_resource,
            operation=ZMQConstStrings.get_user_by_id_operation,
            data={
                ConstStrings.user_id_key: user_id
            }
        )
        return self._data_zmq_client.send_request(request)

    def get_user_by_username_and_password(self, username: str, password: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.auth_resource,
            operation=ZMQConstStrings.get_user_by_username_and_password_operation,
            data={
                ConstStrings.username_key: username,
                ConstStrings.password_key: password
            }
        )
        return self._data_zmq_client.send_request(request)

    def delete_user(self, user_id: str) -> Response:
        print("user_id bl", user_id)
        request = Request(
            resource=ZMQConstStrings.auth_resource,
            operation=ZMQConstStrings.delete_user_operation,
            data={
                ConstStrings.user_id_key: user_id
            }
        )
        return self._data_zmq_client.send_request(request)

    def update_user(self, user_id: str, updated_user_data: dict) -> Response:
        print("updated_user_data", updated_user_data)
        request = Request(
            resource=ZMQConstStrings.auth_resource,
            operation=ZMQConstStrings.update_user_operation,
            data={
                ConstStrings.user_id_key: user_id,
                ConstStrings.user_key: updated_user_data
            }
        )
        return self._data_zmq_client.send_request(request)
