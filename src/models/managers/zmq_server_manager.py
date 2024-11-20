from typing import Any
import zmq

from globals.consts.zmq_const_strings import ZMQConstStrings
from infrastructures.interfaces.izmq_server_manager import IZMQServerManager
from globals.enums.response_status import ResponseStatus
from models.data_classes.zmq_response import Response
from models.data_classes.zmq_request import Request


class ZMQServerManager(IZMQServerManager):
    def __init__(self, routers: Any, host: str, port: str) -> None:
        self._connect(host, port)
        self.routers = {}
        self._include_routers(routers)
        self._start_receiving_requests()

    def _include_routers(self, routers: Any) -> None:
        for router in routers:
            self.routers[router.resource] = router

    def _connect(self, host: str, port: str) -> None:
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REP)
        self._socket.bind(f"{ZMQConstStrings.base_tcp_connection_strings}{host}:{port}")

    def _start_receiving_requests(self) -> None:
        self._handle_incoming_requests()

    def _handle_incoming_requests(self) -> None:
        while True:
            request_json = self._socket.recv_json()
            request = Request.from_json(request_json)
            response = self._route_request(request)
            self._socket.send_json(response.to_json())

    def _route_request(self, request: Request) -> Any:
        resource = request.resource
        operation = request.operation
        data = request.data
        if resource in self.routers:
            route = self.routers[resource]
            return route.handle_operation(operation, data)
        else:
            return Response(
                status=ResponseStatus.ERROR, 
                data={ZMQConstStrings.error_message: ZMQConstStrings.unknown_resource_error_message}
                )