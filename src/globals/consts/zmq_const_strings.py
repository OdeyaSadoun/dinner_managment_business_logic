class ZMQConstStrings:
    # ? Request format identifiers
    resource_identifier = "resource"
    operation_identifier = "operation"
    data_identifier = "data"
    status_identifier = "status"

    # ? Resources
    auth_resource = "auth"
    person_resource = "person"
    table_resource = "table"
    
    # ? Error messages
    error_message = 'ERROR: '
    unknown_resource_error_message = "Unknown resource"
    unknown_operation_error_message = "Unknown operation"


    # ? Operations
    login_operation = "login"
    register_operation = "register"

    get_all_people_operation = "get_all_people"
    get_person_by_id_operation = "get_person_by_id"
    create_person_operation = "create_person"
    update_person_operation = "update_person"
    seat_person_operation = "seat_person"
    delete_person_operation = "delete_person"

    get_all_tables_operation = "get_all_tables"
    get_table_by_id_operation = "get_table_by_id"
    create_table_operation = "create_table"
    update_table_operation = "update_table"
    delete_table_operation = "delete_table"
    add_person_to_table_operation = "add_person_to_table"