#"File" and "UploadFile" are use for Request Files
#Form use for login endpoint
#HTTPException return HTTP responses with errors to the client you use 
from fastapi import APIRouter ,Form , File, UploadFile, HTTPException
from models.todos import Todo , Person
from config.database import collection_name
from schema.schemas import list_serial, list_person
from bson import ObjectId

from typing import Annotated #use for Forms 

router = APIRouter()

#GET Request Method
@router.get("/")
async def get_todo():
    todos = list_serial(collection_name.find())
    todos2= list_person(collection_name.find())
    return todos2

#POST Request Method
@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))

#PUT Request Method
@router.put("/{id}}")
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId()}, {"$set": dict(todo)})

#DELETE Request Method
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})

#FORM 
@router.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

#------------------------------------------------------------------------------
#Request FILES
@router.post("/files/")
async def create_file(file: Annotated[bytes,File()]): # expects to receive the file as a sequence of bytes
    return {"file_size": len(file)}


#The UploadFile object is used to access file information, such as its name, and is returned in the response.
@router.post("/files")
async def create_upload_file(file: UploadFile):
    return{"filename": file.filename}

#Form Method 

@router.post("/Username")
async def register_user(name: Annotated[str, Form()], lastname: Annotated[str, Form()], email: Annotated[str, Form()]):
    user_data ={
        "name": name,
        "lastname": lastname,
        "email": email
    }

    collection_name.insert_one(user_data)

#-------------------------------------------------------------------------------

#Hanligs Errors https://developer.mozilla.org/es/docs/Web/HTTP/Status
#ERRORS HTTP

@router.get("/search/") 
async def read(name: str):
    todos= list_serial(collection_name.find({"name": name})) #search with names
    if len(todos) == 0: # len() is used to determine if the variable "todos" has information.
        raise HTTPException(status_code=404, detail="Name not found")
    else:
        return todos
