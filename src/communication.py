from dataclasses import dataclass

from reservation import Reservation


@dataclass
class Communication:
    reservation: Reservation
    status: str = "Draft"

Again...
