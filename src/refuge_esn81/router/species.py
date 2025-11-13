from fastapi import APIRouter, FastAPI, Depends, HTTPException
from refuge_esn81.schemas.speciesSchema import Species, SpeciesCreate
from sqlalchemy.orm import Session
from refuge_esn81.database.database import get_db
from refuge_esn81.services.specieService import SpecieService


speciesRouter = APIRouter(prefix="/api/species", tags=["species"])

@speciesRouter.get("/", response_model=list[Species])
async def get_species(db: Session = Depends(get_db)):
    """
        Récupère la liste des espèces.

        Cette route renvoie toutes les espèces enregistrées, avec une pagination
        simple via les paramètres internes `skip` et `limit` du service.

        Args:
            db (Session): Session de base de données injectée par FastAPI.

        Returns:
            list[Species]: Liste des espèces existantes.
    """
    service = SpecieService()
    return service.get_species(db)

@speciesRouter.post("/", response_model=Species)
def create_new_species(specie: SpeciesCreate, db: Session = Depends(get_db)):
    """
        Crée une nouvelle espèce.

        Cette route permet d'enregistrer une nouvelle espèce dans la base,
        à partir d'un nom fourni dans le corps de la requête.

        Args:
            specie (SpeciesCreate): Données de l'espèce à créer.
            db (Session): Session de base de données injectée par FastAPI.

        Returns:
            Species: L'espèce créée.
    """
    service = SpecieService()
    return service.create_specie(db, specie)