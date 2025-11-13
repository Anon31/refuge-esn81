from sqlalchemy.orm import Session
from refuge_esn81.schemas.animalSchema import AnimalCreate
from refuge_esn81.models.animal import Animal

class AnimalService:
    """Service de gestion des animaux du refuge (création, lecture, etc.)."""

    def create_animal(self, db: Session, animal: AnimalCreate):
        """
                Crée un nouvel animal en base de données.

                Args:
                    db (Session): Session SQLAlchemy à utiliser pour la transaction.
                    animal (AnimalCreate): Données de l'animal à créer (nom, photo_url, species_id).

                Returns:
                    Animal: L'animal créé, avec son identifiant généré.
         """
        db_animal = Animal(
            name=animal.name,
            age=animal.age,
            description=animal.description,
            gender=animal.gender,
            photo_url=animal.photo_url,
            species_id=animal.species_id
        )
        db.add(db_animal)
        db.commit()
        db.refresh(db_animal)
        return db_animal

    def get_animals(self, db: Session, skip: int = 0, limit: int = 100):
        """
                Retourne une liste paginée d’animaux.

                Args:
                    db (Session): Session SQLAlchemy.
                    skip (int): Nombre d’éléments à ignorer (offset).
                    limit (int): Nombre maximum d’animaux à retourner.

                Returns:
                    list[Animal]: Liste d’animaux récupérés.
        """
        return db.query(Animal).offset(skip).limit(limit).all()