from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Guest:
    first_name: str
    first_last_name: str
    date_of_birth: date
    document_type: str
    document_number: str
    security_code: str
    nationality: str

    second_last_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
