from api.controllers.auth_controller import AuthController
from api.controllers.table_controller import TableController
from api.controllers.person_controller import PersonController
from api.routers.auth_router import AuthRouter
from api.routers.table_router import TableRouter
from api.routers.person_router import PersonRouter
from globals.consts.consts import Consts
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from models.managers.zmq_client_manager import ZMQClientManager
from models.managers.zmq_server_manager import ZMQServerManager


class Factory:
    def create_data_zmq_client():
        return ZMQClientManager(ConstStrings.database_gateway_host, Consts.database_gateway_port)
    
    def create_auth_router(data_zmq_client):
        auth_controller = AuthController(data_zmq_client)
        return AuthRouter(ZMQConstStrings.auth_resource, auth_controller)
    
    def create_table_router(data_zmq_client):
        table_controller = TableController(data_zmq_client)
        return TableRouter(ZMQConstStrings.table_resource, table_controller)
    
    def create_person_router(data_zmq_client):
        person_controller = PersonController(data_zmq_client)
        return PersonRouter(ZMQConstStrings.person_resource, person_controller)
    
    def create_routers(data_zmq_client):
        return [
            Factory.create_auth_router(data_zmq_client),
            Factory.create_table_router(data_zmq_client),
            Factory.create_person_router(data_zmq_client)
        ]

    def create_zmq_server(routers):
        return ZMQServerManager(routers, ConstStrings.localhost, Consts.local_port)
    
    def create_all():
        data_zmq_client = Factory.create_data_zmq_client()
        algorithm_zmq_client = Factory.create_algorithm_zmq_client()
        routers = Factory.create_routers(data_zmq_client)
        Factory.create_zmq_server(routers)