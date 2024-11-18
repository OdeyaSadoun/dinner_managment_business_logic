class AuthController:
    def __init__(self, data_zmq_client):
        self._data_zmq_client = data_zmq_client