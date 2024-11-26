from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from globals.enums.response_status import ResponseStatus
from dinner_managment_business_logic.src.infrastructures.interfaces.icontroller_manager import IControllerManager
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

    def seat_person(self, person_id: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.seat_person_operation,
            data={ConstStrings.person_id_key: person_id}
        )
        return self._data_zmq_client.send_request(request)
    
    def delete_person(self, person_id: str) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.delete_person_operation,
            data={ConstStrings.person_id_key: person_id}
        )
        return self._data_zmq_client.send_request(request)
