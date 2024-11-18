class ZMQConstStrings:    
    base_tcp_connection_strings = "tcp://"

    # ? Request format identifiers
    resource_identifier = "resource"
    operation_identifier = "operation"
    data_identifier = "data"

    # ? Response format indentifiers
    status_identifier = "status"
    data_identifier = "data"

    # ? Resources 
    person_resource = "person"
    pakash_resource = "pakash"
    guard_resource = "guard"
    
    # ? Operations
    get_pakash_by_dates_operation = "get_pakash_by_dates"
    get_person_by_id_operation = "get_person_by_id"
    get_all_people_operation = "get_all_people"
    get_all_guards_operation = "get_all_guards"
    execute_pakash_algorithm_operation = "execute_pakash_algorithm"
    create_guards_operation = "create_guards"
    update_guard_operation = "update_guard"
    check_pakash_validation_operation = "check_pakash_validation"
    get_guards_by_person_id_operation = "get_guards_by_person_id"
    get_person_by_personal_number_operation = "get_person_by_personal_number"
    create_person_operation = "create_person"
    update_person_operation = "update_person"
    delete_person_operation = "delete_person"
    get_guards_between_dates_operation = "get_guards_between_dates"
    shuffle_pakash_operation = "shuffle_pakash"
    update_pakash_operation = "update_pakash"

    # ? Response statuses
    success_status = "success"
    error_status = "error"

    # ? Error messages
    unknown_resource_error_message = "Unknown resource"
    unknown_operation_error_message = "Unknown operation"
    error_message = "Error"
    pakash_generation_error_message = "Cannot scheduele pakash"
    pakash_generation_dates_error_message = "Missing dates between last guard and new pakash start date"