from datetime import date, datetime
from pathlib import Path
from typing import Any

from openpyxl import load_workbook

from guest import Guest
from reservation import Reservation


COLUMN_MAPPING = {
    # Replace the keys with the exact SES headers used in your spreadsheet.
    "numeroReserva": "reservation_number",
    "fechaEntrada": "check_in",
    "fechaSalida": "check_out",
    "nombre": "first_name",
    "primerApellido": "first_last_name",
    "segundoApellido": "second_last_name",
    "fechaNacimiento": "date_of_birth",
    "nacionalidad": "nationality",
    "tipoDocumento": "document_type",
    "numeroDocumento": "document_number",
    "telefono": "phone_number",
    "correo": "email",
}


class ExcelReader:
    REQUIRED_COLUMNS = {
        "reservation_number",
        "check_in",
        "check_out",
        "first_name",
        "first_last_name",
        "date_of_birth",
        "nationality",
        "document_type",
        "document_number",
    }

    def read(self, filename: str) -> Reservation:
        file_path = Path(filename)

        if not file_path.exists():
            raise FileNotFoundError(f"Excel file not found: {file_path}")

        workbook = load_workbook(
            filename=file_path,
            data_only=True,
            read_only=True,
        )

        if "Guests" not in workbook.sheetnames:
            raise ValueError(
                "The workbook must contain a worksheet named 'Guests'."
            )

        worksheet = workbook["Guests"]
        rows = worksheet.iter_rows(values_only=True)

        try:
            raw_headers = next(rows)
        except StopIteration as exc:
            raise ValueError("The Guests worksheet is empty.") from exc

        headers = []

        for value in raw_headers:
            if value is None:
                headers.append("")
                continue

            original_header = str(value).strip()
            internal_header = COLUMN_MAPPING.get(
                original_header,
                original_header,
            )
            headers.append(internal_header)

        missing_columns = self.REQUIRED_COLUMNS - set(headers)

        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"Missing required columns: {missing}")

        records: list[dict[str, Any]] = []

        for row_number, values in enumerate(rows, start=2):
            record = dict(zip(headers, values))

            if all(value in (None, "") for value in record.values()):
                continue

            record["_row_number"] = row_number
            records.append(record)

        if not records:
            raise ValueError("No guest records were found.")

        first_record = records[0]

        reservation = Reservation(
            reservation_number=self._required_text(
                first_record,
                "reservation_number",
            ),
            check_in=self._to_date(
                first_record.get("check_in"),
                "check_in",
                first_record["_row_number"],
            ),
            check_out=self._to_date(
                first_record.get("check_out"),
                "check_out",
                first_record["_row_number"],
            ),
        )

        for record in records:
            guest = Guest(
                first_name=self._required_text(
                    record,
                    "first_name",
                ),
                first_last_name=self._required_text(
                    record,
                    "first_last_name",
                ),
                second_last_name=self._optional_text(
                    record.get("second_last_name")
                ),
                date_of_birth=self._to_date(
                    record.get("date_of_birth"),
                    "date_of_birth",
                    record["_row_number"],
                ),
                nationality=self._required_text(
                    record,
                    "nationality",
                ),
                document_type=self._required_text(
                    record,
                    "document_type",
                ),
                document_number=self._required_text(
                    record,
                    "document_number",
                ),
                phone_number=self._optional_text(
                    record.get("phone_number")
                ),
                email=self._optional_text(
                    record.get("email")
                ),
            )

            reservation.guests.append(guest)

        return reservation

    @staticmethod
    def _optional_text(value: Any) -> str | None:
        if value is None:
            return None

        text = str(value).strip()
        return text or None

    def _required_text(
        self,
        record: dict[str, Any],
        field_name: str,
    ) -> str:
        value = self._optional_text(record.get(field_name))

        if value is None:
            row_number = record.get("_row_number", "?")
            raise ValueError(
                f"Row {row_number}: '{field_name}' is required."
            )

        return value

    @staticmethod
    def _to_date(
        value: Any,
        field_name: str,
        row_number: int,
    ) -> date:
        if isinstance(value, datetime):
            return value.date()

        if isinstance(value, date):
            return value

        if isinstance(value, str):
            cleaned = value.strip()

            for date_format in ("%d/%m/%Y", "%Y-%m-%d"):
                try:
                    return datetime.strptime(
                        cleaned,
                        date_format,
                    ).date()
                except ValueError:
                    continue

        raise ValueError(
            f"Row {row_number}: invalid date in "
            f"'{field_name}': {value!r}"
        )
