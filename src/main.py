
from datetime import date
from excel_reader import ExcelReader
from guest import Guest
from reservation import Reservation
from xml_generator import XMLGenerator

def main() -> None:
    reader = ExcelReader()
    reservation = reader.read("examples/SESdummyData.xlsx")
    generator = XMLGenerator()
    output_path = generator.generate(
          reservation,
            "output/reservation.xml",
            )                    

    print(f"XML created: {output_path}")

    print(reservation)
    

if __name__ == "__main__":
    main()
