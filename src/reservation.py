from dataclasses import dataclass, field
from datetime import date
from typing import List

from accommodation import Accommodation
from guest import Guest


@dataclass
class Reservation:
    reservation_number: str
    accommodation: Accommodation
    check_in: date
    check_out: date
    guests: List[Guest] = field(default_factory=list)
