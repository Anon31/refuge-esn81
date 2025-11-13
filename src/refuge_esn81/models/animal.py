from sqlalchemy import Column, Integer, String, ForeignKey
from refuge_esn81.database.database import Base
from sqlalchemy.orm import relationship

class Animal(Base):
    """
        Modèle SQLAlchemy représentant un animal du refuge.

        Attributs:
            id (int): Identifiant unique de l'animal.
            name (str): Nom de l'animal.
            photo_url (str | None): URL d'une photo de l'animal.
            species_id (int | None): Identifiant de l'espèce associée (species.id).
    """
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    description = Column(String)
    gender = Column(String)
    photo_url = Column(String(300))
    species_id = Column(Integer, ForeignKey("species.id"))

    # Relation : un animal appartient à une espèce
    species = relationship("Species", back_populates="animals")
