import os
from typing import List

from api.controllers.user_controller import UserController
from api.controllers.table_controller import TableController
from api.controllers.person_controller import PersonController
from api.routers.user_router import UserRouter
from api.routers.table_router import TableRouter
from api.routers.person_router import PersonRouter
from api.routers.base_router import BaseRouter
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from infrastructures.interfaces.izmq_server_manager import IZMQServerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.managers.zmq_client_manager import ZMQClientManager
from models.managers.zmq_server_manager import ZMQServerManager


class Factory:
    def create_data_zmq_client() -> IZMQClientManager:
        host = os.getenv(ConstStrings.database_gateway_host_env_key)        
        port = os.getenv(ConstStrings.database_gateway_port_env_key)
        return ZMQClientManager(host, port)
    
    def create_user_router(data_zmq_client: IZMQClientManager) -> BaseRouter:
        user_controller = UserController(data_zmq_client)
        return UserRouter(ZMQConstStrings.auth_resource, user_controller)
    
    def create_person_router(data_zmq_client: IZMQClientManager) -> BaseRouter:
        person_controller = PersonController(data_zmq_client)
        return PersonRouter(ZMQConstStrings.person_resource, person_controller)
    
    def create_table_router(data_zmq_client: IZMQClientManager) -> BaseRouter:
        table_controller = TableController(data_zmq_client)
        return TableRouter(ZMQConstStrings.table_resource, table_controller)
    
    def create_routers(data_zmq_client: IZMQClientManager) -> List[BaseRouter]:
        return [
            Factory.create_user_router(data_zmq_client),
            Factory.create_person_router(data_zmq_client),
            Factory.create_table_router(data_zmq_client)
        ]

    def create_zmq_server(routers: List[BaseRouter]) -> IZMQServerManager:
        host = os.getenv(ConstStrings.localhost_env_key)        
        port = os.getenv(ConstStrings.local_port_env_key)
        return ZMQServerManager(routers, host, port)
    
    def create_all() -> None:
        data_zmq_client = Factory.create_data_zmq_client()
        routers = Factory.create_routers(data_zmq_client)
        Factory.create_zmq_server(routers)