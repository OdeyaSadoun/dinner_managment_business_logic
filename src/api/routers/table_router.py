from typing import Any

from api.routers.base_router import BaseRouter
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from infrastructures.interfaces.icontroller_manager import IControllerManager
from models.data_classes.zmq_response import Response


class TableRouter(BaseRouter):
    def __init__(self, resource: str, ctrl: IControllerManager):
        super().__init__(resource, ctrl)
        self._setup_operations()

    def _setup_operations(self):
        self._operations = {
            ZMQConstStrings.get_all_tables_operation: self.get_all_tables,
            ZMQConstStrings.get_table_by_id_operation: self.get_table_by_id,
            ZMQConstStrings.create_table_operation: self.create_table,
            ZMQConstStrings.update_table_operation: self.update_table,
            ZMQConstStrings.update_table_position_operation: self.update_table_position,
            ZMQConstStrings.delete_table_operation: self.delete_table,
            ZMQConstStrings.import_tables_from_csv_operation: self.import_tables_from_csv,
        }
        
    def import_tables_from_csv(self, data: Any) -> Response:
        tables = data.get(ConstStrings.tables_key)
        return self._ctrl.import_tables_from_csv(tables)
    
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

    def update_table_position(self, data: Any) -> Response:
        table_id = data.get(ConstStrings.table_id_key)
        position = data.get(ConstStrings.position_key)
        return self._ctrl.update_table_position(table_id, position)

    def delete_table(self, data: Any) -> Response:
        table_id = data.get(ConstStrings.table_id_key)
        return self._ctrl.delete_table(table_id)