from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modèles Pydantic
class Vehicule(BaseModel):
    registration: str
    owner: str
    category: str
    insurance_quotation: float

class Acc(BaseModel):
    registration: str
    owner: str
    insurance_quotation: float
    economy_gain: float
    total_amount: float


# Données de la flotte d'assurance (exemple)
fleet = [
    Vehicule(registration="AB 1234", owner="Congregation", category="Voiture", insurance_quotation=5000.0),
    Vehicule(registration="DF 4568", owner="Communauté réligieuse 1", category="Moto", insurance_quotation=2500.0),
    Vehicule(registration="GH 7899", owner="Soeur Marie Anne", category="Voiture", insurance_quotation=5000.0),
    Vehicule(registration="PK 0120", owner="Communauté réligieuse 2", category="Voiture", insurance_quotation=5000.0),
    Vehicule(registration="AG 6420", owner="Congrégation", category="moto", insurance_quotation=2500.0),
    Vehicule(registration="JK 0120", owner="Soeur Renée Martine", category="moto", insurance_quotation=2500.0),
]


# Endpoints
@app.get("/category/{category}")
def get_vehicles_by_category(category: str) -> List[Vehicule]:
    return [Vehicule for Vehicule in fleet if Vehicule.category.lower() == category.lower()]


@app.get("/owner/{owner}")
def get_vehicles_by_owner(owner: str) -> List[Vehicule]:
    return [Vehicule for Vehicule in fleet if Vehicule.owner.lower() == owner.lower()]


@app.get("/bills/{owner}")
def get_bills_for_owner(owner: str) -> List[Acc]:
    owner_Vehicule = [Vehicule for Vehicule in fleet if Vehicule.owner.lower() == owner.lower()]
    bills = []

    for Vehicule in owner_Vehicule:
        economy_gain = Vehicule.insurance_quotation * 0.2  # Majore la cotation de 20%
        total_amount = Vehicule.insurance_quotation + economy_gain
        bill = Acc(
            registration=Vehicule.registration,
            owner=Vehicule.owner,
            insurance_quotation=Vehicule.insurance_quotation,
            economy_gain=economy_gain,
            total_amount=total_amount,
        )
        bills.append(bill)

    return bills
