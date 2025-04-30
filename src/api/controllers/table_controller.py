from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from globals.enums.response_status import ResponseStatus
from infrastructures.interfaces.icontroller_manager import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.table import Table
from models.data_classes.zmq_response import Response
from models.data_classes.zmq_request import Request
from models.data_classes.person import Person


class TableController(IControllerManager):
    def __init__(self, data_zmq_client: IZMQClientManager):
        self._data_zmq_client = data_zmq_client

    def get_all_tables(self) -> Response:
        request = Request(
            resource=ZMQConstStrings.table_resource,
            operation=ZMQConstStrings.get_all_tables_operation
        )
        return self._data_zmq_client.send_request(request)

    def get_table_by_id(self, table_id: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.table_resource,
            operation=ZMQConstStrings.get_table_by_id_operation,
            data={ConstStrings.table_id_key: table_id}
        )
        return self._data_zmq_client.send_request(request)

    def create_table(self, table: Table) -> Response:
        request = Request(
            resource=ZMQConstStrings.table_resource,
            operation=ZMQConstStrings.create_table_operation,
            data={ConstStrings.table_key: table}
        )
        response = self._data_zmq_client.send_request(request)
        print("response", response.data)
        return self._data_zmq_client.send_request(request)

    def update_table(self, table_id: str, table: Table) -> Response:
        request = Request(
            resource=ZMQConstStrings.table_resource,
            operation=ZMQConstStrings.update_table_operation,
            data={
                ConstStrings.table_id_key: table_id,
                ConstStrings.table_key: table
            }
        )
        return self._data_zmq_client.send_request(request)

    def update_table_position(self, table_id: str, position: dict) -> Response:
        request = Request(
            resource=ZMQConstStrings.table_resource,
            operation=ZMQConstStrings.update_table_position_operation,
            data={
                ConstStrings.table_id_key: table_id,
                ConstStrings.position_key: position
            }
        )
        return self._data_zmq_client.send_request(request)

    def delete_table(self, table_id: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.table_resource,
            operation=ZMQConstStrings.delete_table_operation,
            data={ConstStrings.table_id_key: table_id}
        )
        return self._data_zmq_client.send_request(request)

    # def add_person_to_table(self, table_id: str, person_id: str) -> Response:
    #     request = Request(
    #         resource=ZMQConstStrings.table_resource,
    #         operation=ZMQConstStrings.add_person_to_table_operation,
    #         data={
    #             ConstStrings.table_id_key: table_id,
    #             ConstStrings.person_id_key: person_id
    #         }
    #     )
    #     return self._data_zmq_client.send_request(request)
    
    # def remove_person_from_table(self, table_id: str, person_id: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.table_resource,
            operation=ZMQConstStrings.remove_person_from_table_operation,
            data={
                ConstStrings.table_id_key: table_id,
                ConstStrings.person_id_key: person_id
            }
        )
        return self._data_zmq_client.send_request(request)