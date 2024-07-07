def individual_serial(todo) ->dict:
    return{
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"]
    }

def list_serial(todos)->list:
    return[individual_serial(todo) for todo in todos]


def individual_person(person) ->dict:
    return{
        "id": str(person["_id"]),
        "name": person["name"],
        "lastname": person["lastname"],
        "email": person["email"]
    }

def list_person(persons) ->list:
    return[individual_person(person) for person in persons]