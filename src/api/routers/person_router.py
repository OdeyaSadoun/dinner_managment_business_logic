from typing import Any

from api.routers.base_router import BaseRouter
from globals.consts.const_strings import ConstStrings
from models.data_classes.zmq_response import Response
from infrastructures.interfaces.icontroller_manager import IControllerManager
from globals.consts.zmq_const_strings import ZMQConstStrings


class PersonRouter(BaseRouter):
    def __init__(self, resource: str, ctrl: IControllerManager):
        super().__init__(resource, ctrl)
        self._setup_operations()

    def _setup_operations(self):
        self._operations = {
            ZMQConstStrings.get_all_people_operation: self.get_all_people,
            ZMQConstStrings.get_person_by_id_operation: self.get_person_by_id,
            ZMQConstStrings.create_person_operation: self.create_person,
            ZMQConstStrings.update_person_operation: self.update_person,
            ZMQConstStrings.delete_person_operation: self.delete_person,
            ZMQConstStrings.seat_person_operation: self.seat_person,
        }

    def get_all_people(self, data: Any=None) -> Response:
        return self._ctrl.get_all_people()

    def get_person_by_id(self, data: Any) -> Response:
        person_id = data.get(ConstStrings.person_id_key)
        return self._ctrl.get_person_by_id(person_id)

    def create_person(self, data: Any) -> Response:
        person = data.get(ConstStrings.person_key)
        return self._ctrl.create_person(person)

    def update_person(self, data: Any) -> Response:
        person_id = data.get(ConstStrings.person_id_key)
        person = data.get(ConstStrings.person_key)
        return self._ctrl.update_person(person_id, person)

    def seat_person(self, data: Any) -> Response:
        person_id = data.get(ConstStrings.person_id_key)
        return self._ctrl.seat_person(person_id)

    def delete_person(self, data: Any) -> Response:
        person_id = data.get(ConstStrings.person_id_key)
        return self._ctrl.delete_person(person_id)
