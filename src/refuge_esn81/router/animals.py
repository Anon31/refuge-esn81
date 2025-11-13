from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from refuge_esn81.database.database import get_db
from refuge_esn81 import router
from refuge_esn81.schemas.animalSchema import Animal, AnimalCreate
from refuge_esn81.services.animalService import AnimalService

animalsRouter = APIRouter(prefix="/animals", tags=["animals"])

service = AnimalService()

@animalsRouter.get("/",  response_model=list[Animal])
async def get_all_animals(db: Session = Depends(get_db)):
    return service.get_animals(db)

@animalsRouter.post("/")
async def create_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    return service.create_animal(db, animal)

# @animalsRouter.get("/{name}")
# async def find_animal(name: str):
#     return service.find(name)
#
# @animalsRouter.delete("/{name}")
# async def delete_animal(name: str):
#     return service.delete(name)