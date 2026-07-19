from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Guest:
    first_name: str
    first_surname: str
    date_of_birth: date
    document_type: str
    document_number: str
    security_code: str
    nationality: str
    phone_number:str
    email: str
    address: str

    second_surname: Optional[str] = None
