import zmq

from globals.consts.const_strings import ConstStrings
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.zmq_response import Response
from models.data_classes.zmq_request import Request


class ZMQClientManager(IZMQClientManager):
    def __init__(self, host: str, port: str) -> None:
        self._connect(host, port)

    def send_request(self, request: Request) -> Response:
        self._socket.send_json(request.to_json())
        response = self._socket.recv_json()
        return Response.from_json(response)

    def _connect(self, host: str, port: str) -> None:
        self.context = zmq.Context()
        self._socket = self.context.socket(zmq.REQ)
        self._socket.connect(f"{ConstStrings.base_tcp_connection_strings}{host}:{port}")