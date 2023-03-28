import dataclasses
from typing import Any
from menu.models import Ingredientes
from decimal import Decimal


@dataclasses.dataclass
class IngredienteDataClass():
    nome: str
    gordura: Decimal
    proteina: Decimal
    carboidrato: Decimal
    vegetal: bool
    id: int|Any = None

    @classmethod
    def from_instance(cls, ingrediente: Ingredientes):
        return cls(
            nome=ingrediente.nome,
            gordura=ingrediente.gordura,
            proteina=ingrediente.proteina,
            carboidrato=ingrediente.carboidrato,
            vegetal=ingrediente.vegetal,
            id=ingrediente.id
        )

