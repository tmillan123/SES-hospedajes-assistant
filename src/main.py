from datetime import date

from guest import Guest


def main() -> None:
    guest = Guest(
        first_name="Ana",
        last_name="García",
        date_of_birth=date(1985, 4, 12),
        document_type="DNI",
        document_number="12345678Z",
        nationality="ES",
        phone_number="+34600111222",
        email="ana.garcia@example.com",
    )

    print(guest)


if __name__ == "__main__":
    main()
