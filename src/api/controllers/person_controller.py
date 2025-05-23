from fastapi import UploadFile
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
    
    def get_manual_people(self) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.get_manual_people_operation,
            data={}
        )
        return self._data_zmq_client.send_request(request)
    
    def get_manual_people(self) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.get_manual_people_operation,
            data={}
        )
        return self._data_zmq_client.send_request(request)
    
    def create_person(self, person: Person) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.create_person_operation,
            data={ConstStrings.person_key: person}
        )
        return self._data_zmq_client.send_request(request)
    
    def import_people_from_csv(self, people: list[dict]) -> Response:
        request = Request(
            resource=ZMQConstStrings.person_resource,
            operation=ZMQConstStrings.import_people_from_csv_operation,
            data={ConstStrings.people_key: people}
        )
        print("import csv ctrl bl")
        return self._data_zmq_client.send_request(request)

    def update_person(self, person_id: str, person: Person) -> Response:
        try:
            # שליפת המשתמש הקיים
            response_get = self._data_zmq_client.send_request(Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.get_person_by_id_operation,
                data={ConstStrings.person_id_key: person_id}
            ))
            print("response_get", response_get.data)
            if response_get.status != ResponseStatus.SUCCESS:
                return response_get

            existing_person = response_get.data[ConstStrings.person_key]
            print("existing_person", existing_person)
            was_seated_and_now_not = (
                existing_person.get("is_reach_the_dinner") is True and
                person["is_reach_the_dinner"] is False and
                existing_person.get("table_number") is not None
            )
            print("was_seated_and_now_not", was_seated_and_now_not)
            # שליחת עדכון רגיל
            update_response = self._data_zmq_client.send_request(Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.update_person_operation,
                data={
                    ConstStrings.person_id_key: person_id,
                    ConstStrings.person_key: person
                }
            ))
            print("update_response", update_response.data)
            # הסרה מהשולחן
            if was_seated_and_now_not:
                table_number = existing_person["table_number"]
                response_get_table = self._data_zmq_client.send_request(Request(
                    resource=ZMQConstStrings.table_resource,
                    operation=ZMQConstStrings.get_table_by_number_operation,
                    data={ConstStrings.table_number_key: table_number}
                ))

                if response_get_table.status == ResponseStatus.SUCCESS:
                    table_id = response_get_table.data["table_id"]
                    self._data_zmq_client.send_request(Request(
                        resource=ZMQConstStrings.table_resource,
                        operation=ZMQConstStrings.remove_person_from_table_operation,
                        data={
                            ConstStrings.table_id_key: table_id,
                            ConstStrings.person_id_key: person_id
                        }
                    ))

            return update_response

        except Exception as e:
            return Response(status=ResponseStatus.ERROR, data={ZMQConstStrings.error_message: str(e)})

    def delete_person(self, person_id: str, table_number: int, is_reach_the_dinner: bool) -> Response:
        if not is_reach_the_dinner:
            # לא צריך להסיר אותו מהשולחן
            request_delete_person = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.delete_person_operation,
                data={ConstStrings.person_id_key: person_id}
            )
            return self._data_zmq_client.send_request(request_delete_person)

        # המשך מחיקה רגילה כמו קודם:
        request_get_table = Request(
            resource=ZMQConstStrings.table_resource,
            operation=ZMQConstStrings.get_table_by_number_operation,
            data={ConstStrings.table_number_key: table_number}
        )
        response_get_table = self._data_zmq_client.send_request(request_get_table)

        if response_get_table.status == ResponseStatus.SUCCESS:
            table_id = response_get_table.data["table_id"]

            request_delete_person_from_table = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.remove_person_from_table_operation,
                data={
                    ConstStrings.table_id_key: table_id,
                    ConstStrings.person_id_key: person_id
                }
            )
            response_remove = self._data_zmq_client.send_request(request_delete_person_from_table)
            if response_remove.status == ResponseStatus.SUCCESS:
                request_delete_person = Request(
                    resource=ZMQConstStrings.person_resource,
                    operation=ZMQConstStrings.delete_person_operation,
                    data={ConstStrings.person_id_key: person_id}
                )
                return self._data_zmq_client.send_request(request_delete_person)

        return Response(status=ResponseStatus.ERROR)

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
