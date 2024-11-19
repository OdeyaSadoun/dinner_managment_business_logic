from fastapi import HTTPException

from globals.consts.person_data_const_strings import PersonDataConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from globals.consts.consts import Consts
from infrastructures.interfaces.icontroller_managment import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.person import Person
from models.data_classes.zmq_request import Request
from models.data_classes.zmq_response import Response


class PersonController(IControllerManager):
    def __init__(self, zmq_client: IZMQClientManager) -> None:
        super().__init__()
        self._zmq_client = zmq_client

    def get_all_people(self) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.get_all_people_operation
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def get_person_by_id(self, person_id: str) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.get_person_by_id_operation,
                data={PersonDataConstStrings.person_id_key: person_id}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def create_person(self, person: Person) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.create_person_operation,
                data={PersonDataConstStrings.person_key: person}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def update_person(self, person_id: str, person: Person) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.update_person_operation,
                data={
                    PersonDataConstStrings.person_id_key: person_id,
                    PersonDataConstStrings.person_key: person
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def seat_person(self, person_id: str) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.delete_person_operation,
                data={PersonDataConstStrings.person_id_key: person_id}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))
    
    def delete_person(self, person_id: str) -> Response:
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.delete_person_operation,
                data={PersonDataConstStrings.person_id_key: person_id}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))
