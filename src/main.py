from datetime import date

from guest import Guest
from reservation import Reservation


def main() -> None:
    guest = Guest(
    first_name="Ana",
    first_surname="García",
    date_of_birth=date(1985, 4, 12),
    nationality="ES",
    document_type="DNI",
    document_number="12345678Z",
    security_code="",        
    phone_number="+34600111222",
    email="ana.garcia@example.com",
    address="Calle Mayor 10, 28013 Madrid",
    )

    reservation = Reservation(
    reservation_number="TEST-001",
    accommodation="Casa de Campo Alborada",
    check_in=date(2026, 7, 23),
    check_out=date(2026, 7, 31),
    guests=[guest]
    )

    print(reservation)


if __name__ == "__main__":
    main()
