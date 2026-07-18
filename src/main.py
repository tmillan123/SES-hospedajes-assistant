from datetime import date

from accommodation import Accommodation
from guest import Guest
from reservation import Reservation


def main():
    accommodation = Accommodation(
        registration_number="ES12345",
        name="Casa de Campo Alborada",
        address="Lugo, Spain",
    )

    guest = Guest(
        first_name="John",
        last_name="Smith",
        date_of_birth=date(1980, 5, 12),
        nationality="GB",
    )

    reservation = Reservation(
        reservation_number="ABC123",
        check_in=date(2026, 7, 20),
        check_out=date(2026, 7, 27),
    )

    reservation.guests.append(guest)

    print(accommodation)
    print(reservation)
    print(guest)


if __name__ == "__main__":
    main()
