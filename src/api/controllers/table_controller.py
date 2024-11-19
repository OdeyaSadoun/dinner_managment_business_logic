from fastapi import HTTPException

from globals.consts.table_data_const_strings import TableDataConstStrings
from globals.consts.person_data_const_strings import PersonDataConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from globals.consts.consts import Consts
from infrastructures.interfaces.icontroller_managment import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.person import Person
from models.data_classes.table import Table
from models.data_classes.zmq_request import Request
from models.data_classes.zmq_response import Response


class TableController(IControllerManager):
    def __init__(self, zmq_client: IZMQClientManager) -> None:
        super().__init__()
        self._zmq_client = zmq_client

    def get_all_tables(self) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.get_all_tables_operation
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def get_table_by_id(self, table_id: str) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.get_table_by_id_operation,
                data={TableDataConstStrings.table_id_key: table_id}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def create_table(self, table: Table) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.create_table_operation,
                data={TableDataConstStrings.table_key: table}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def update_table(self, table_id: str, table: Table) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.update_table_operation,
                data={
                    TableDataConstStrings.table_id_key: table_id,
                    TableDataConstStrings.table_key: table
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def delete_table(self, table_id: str) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.delete_table_operation,
                data={TableDataConstStrings.table_id_key: table_id}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def add_person_to_table(self, table_id: str, person: Person) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.add_person_to_table_operation,
                data={
                    TableDataConstStrings.table_id_key: table_id,
                    PersonDataConstStrings.person_key: person
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))
