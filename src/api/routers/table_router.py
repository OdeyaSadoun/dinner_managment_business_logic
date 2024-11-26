from typing import Any

from api.routers.base_router import BaseRouter
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from dinner_managment_business_logic.src.infrastructures.interfaces.icontroller_manager import IControllerManager
from models.data_classes.zmq_response import Response


class TableRouter(BaseRouter):
    def __init__(self, resource: str, ctrl: IControllerManager):
        super().__init__(resource, ctrl)
        self._setup_operations()

    def _setup_operations(self):
        self._operations = {
            ZMQConstStrings.get_all_tables_operation: self.get_all_tables,
            ZMQConstStrings.get_person_by_id_operation: self.get_person_by_id,
            ZMQConstStrings.create_person_operation: self.create_person,
            ZMQConstStrings.update_person_operation: self.update_person,
            ZMQConstStrings.delete_person_operation: self.delete_person,
            ZMQConstStrings.seat_person_operation: self.seat_person,
        }

    def get_all_tables(self, data: Any=None) -> Response:
        return self._ctrl.get_all_tables()

    def get_table_by_id(self, data: Any) -> Response:
        table_id = data.get(ConstStrings.table_id_key)
        return self._ctrl.get_table_by_id(table_id)

    def create_table(self, data: Any) -> Response:
        table = data.get(ConstStrings.table_key)
        return self._ctrl.create_table(table)

    def update_table(self, data: Any) -> Response:
        table_id = data.get(ConstStrings.table_id_key)
        table = data.get(ConstStrings.table_key)
        return self._ctrl.update_table(table_id, table)

    def delete_table(self, data: Any) -> Response:
        table_id = data.get(ConstStrings.table_id_key)
        return self._ctrl.delete_table(table_id)
    
    def add_person_to_table(self, data: Any) -> Response:
        table_id = data.get(ConstStrings.table_id_key)
        person = data.get(ConstStrings.person_key)
        return self._ctrl.update_table(table_id, person)   
