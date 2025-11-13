from sqlalchemy.orm import Session
from refuge_esn81.schemas.speciesSchema import SpeciesCreate
from refuge_esn81.models.species import Species

class SpecieService:
    """Service de gestion des espèces (création, lecture, etc.)."""
    def create_specie(self, db: Session, specie: SpeciesCreate):
        """
                Crée une nouvelle espèce en base de données.

                Args:
                    db (Session): Session SQLAlchemy utilisée pour la transaction.
                    specie (SpeciesCreate): Données de l'espèce à créer (nom).

                Returns:
                    Species: L'espèce créée, avec son identifiant généré.
        """
        db_specie = Species(name=specie.name)
        db.add(db_specie)
        db.commit()
        db.refresh(db_specie)
        return db_specie

    def get_species(self, db: Session, skip: int = 0, limit: int = 100):
        """
                Récupère une liste paginée d'espèces.

                Args:
                    db (Session): Session SQLAlchemy.
                    skip (int): Nombre d'éléments à ignorer (offset).
                    limit (int): Nombre maximum d'espèces à retourner.

                Returns:
                    list[Species]: Liste des espèces trouvées.
        """
        return db.query(Species).offset(skip).limit(limit)