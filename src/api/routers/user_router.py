from typing import Any

from api.routers.base_router import BaseRouter
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from models.data_classes.zmq_response import Response


class UserRouter(BaseRouter):
    def __init__(self, resource, ctrl):
        super().__init__(resource, ctrl)
        self._setup_operations()

    def _setup_operations(self):
        self._operations = {
            ZMQConstStrings.login_operation: self.login,
            ZMQConstStrings.register_operation: self.register,
            ZMQConstStrings.get_all_users_operation: self.get_all_users,
            ZMQConstStrings.get_user_by_id_operation: self.get_user_by_id,
            ZMQConstStrings.get_user_by_username_and_password_operation: self.get_user_by_username_and_password,
            ZMQConstStrings.delete_user_operation: self.delete_user,
            ZMQConstStrings.update_user_operation: self.update_user
        }

    def register(self, data: Any) -> Response:
        user = data.get(ConstStrings.user_key)
        return self._ctrl.register(user)

    def login(self, data: Any) -> Response:
        print("login router")
        user = data.get(ConstStrings.user_key)
        print(user)
        return self._ctrl.login(user)

    def get_all_users(self, data: Any) -> Response:
        return self._ctrl.get_all_users()    

    def get_user_by_id(self, data: Any) -> Response:
        user_id = data.get(ConstStrings.user_id_key)
        return self._ctrl.get_user_by_id(user_id)

    def get_user_by_username_and_password(self, data: Any) -> Response:
        username = data.get(ConstStrings.username_key)
        password = data.get(ConstStrings.password_key)
        return self._ctrl.get_user_by_username_and_password(username, password)

    def delete_user(self, data: Any) -> Response:
        user_id = data.get(ConstStrings.user_id_key)
        return self._ctrl.delete_user(user_id)

    def update_user(self, data: Any) -> Response:
        print("data in route bl", data)
        user_id = data.get(ConstStrings.user_id_key)
        updated_user_data = data.get(ConstStrings.user_key)
        return self._ctrl.update_user(user_id, updated_user_data)
