from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from globals.enums.response_status import ResponseStatus
from infrastructures.interfaces.icontroller_manager import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.zmq_response import Response
from models.data_classes.zmq_request import Request
from models.data_classes.person import Person


class PersonController(IControllerManager):
    def __init__(self, data_zmq_client: IZMQClientManager):
        self._data_zmq_client = data_zmq_client
        
    def get_all_people(self) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.get_all_people_operation
        )
        return self._data_zmq_client.send_request(request)
    
    def get_person_by_id(self, person_id: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.get_person_by_id_operation,
            data={ConstStrings.person_id_key: person_id}
        )
        return self._data_zmq_client.send_request(request)

    def create_person(self, person: Person) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.create_person_operation,
            data={ConstStrings.person_key: person}
        )
        return self._data_zmq_client.send_request(request)

    def update_person(self, person_id: str, person: Person) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.update_person_operation,
            data={
                ConstStrings.person_id_key: person_id,
                ConstStrings.person_key: person
            }
        )
        return self._data_zmq_client.send_request(request)
    
    def delete_person(self, person_id: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.delete_person_operation,
            data={ConstStrings.person_id_key: person_id}
        )
        return self._data_zmq_client.send_request(request)

    def seat_and_add_person_to_table(self, person_id: str, table_id: str) -> Response:
        try:
            seat_request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.seat_person_operation,
                data={ConstStrings.person_id_key: person_id}
            )
            seat_response = self._data_zmq_client.send_request(seat_request)
            
            print(seat_response.status)
            if seat_response.status != ResponseStatus.SUCCESS:
                return seat_response

            print("add inbl")
            add_request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.add_person_to_table_operation,
                data={
                    ConstStrings.table_id_key: table_id,
                    ConstStrings.person_id_key: person_id
                }
            )
            add_response = self._data_zmq_client.send_request(add_request)
            print(add_response.data)
            if add_response.status != ResponseStatus.SUCCESS:
                return add_response  

            return Response(status=ResponseStatus.SUCCESS)

        except Exception as e:
            return Response(
                status=ResponseStatus.ERROR,
                data={ZMQConstStrings.error_message: str(e)}
            )

    def unseat_and_remove_person_from_table(self, person_id: str, table_id: str) -> Response:
        try:
            unseat_request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.unseat_person_operation,
                data={ConstStrings.person_id_key: person_id}
            )
            unseat_response = self._data_zmq_client.send_request(unseat_request)
            if unseat_response.status != ResponseStatus.SUCCESS:
                return unseat_response

            remove_request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.remove_person_from_table_operation,
                data={
                    ConstStrings.table_id_key: table_id,
                    ConstStrings.person_id_key: person_id
                }
            )
            remove_response = self._data_zmq_client.send_request(remove_request)
            if remove_response.status != ResponseStatus.SUCCESS:
                return remove_response  

            return Response(status=ResponseStatus.SUCCESS)

        except Exception as e:
            return Response(
                status=ResponseStatus.ERROR,
                data={ZMQConstStrings.error_message: str(e)}
            )
