from pathlib import Path
import xml.etree.ElementTree as ET

from reservation import Reservation


class XMLGenerator:
    def generate(
        self,
        reservation: Reservation,
        output_filename: str,
    ) -> Path:
        output_path = Path(output_filename)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        root = ET.Element("reservation")

        ET.SubElement(
            root,
            "reservationNumber",
        ).text = reservation.reservation_number

        ET.SubElement(
            root,
            "accommodation",
        ).text = reservation.accommodation

        ET.SubElement(
            root,
            "checkIn",
        ).text = reservation.check_in.isoformat()

        ET.SubElement(
            root,
            "checkOut",
        ).text = reservation.check_out.isoformat()

        guests_element = ET.SubElement(root, "guests")

        for guest in reservation.guests:
            guest_element = ET.SubElement(
                guests_element,
                "guest",
            )

            ET.SubElement(
                guest_element,
                "firstName",
            ).text = guest.first_name

            ET.SubElement(
                guest_element,
                "firstSurname",
            ).text = guest.first_surname

            if guest.second_surname:
                ET.SubElement(
                    guest_element,
                    "secondSurname",
                ).text = guest.second_surname

            ET.SubElement(
                guest_element,
                "dateOfBirth",
            ).text = guest.date_of_birth.isoformat()

            ET.SubElement(
                guest_element,
                "documentType",
            ).text = guest.document_type

            ET.SubElement(
                guest_element,
                "documentNumber",
            ).text = guest.document_number

            ET.SubElement(
                guest_element,
                "securityCode",
            ).text = guest.security_code

            ET.SubElement(
                guest_element,
                "nationality",
            ).text = guest.nationality

            ET.SubElement(
                guest_element,
                "phoneNumber",
            ).text = guest.phone_number

            ET.SubElement(
                guest_element,
                "email",
            ).text = guest.email

            ET.SubElement(
                guest_element,
                "address",
            ).text = guest.address

        tree = ET.ElementTree(root)

        ET.indent(tree, space="    ")

        tree.write(
            output_path,
            encoding="utf-8",
            xml_declaration=True,
        )

        return output_path
