## Purpose

The objective of this application is to simplify the preparation of
guest registration communications for Spain's SES.HOSPEDAJES platform.

The application is not an XML generator.

It is a domain-driven application that models reservations,
guests and official communications.

---

## Main Entities

### Accommodation

Represents the accommodation establishment.

Examples:

- Rural house
- Hotel
- Hostel
- Apartment

---

### Reservation

Represents a booking made by one or more guests.

A reservation has:

- Check-in date
- Check-out date
- Reservation number
- Accommodation
- Guests


---

### Guest

Represents a traveller staying at the accommodation.

A guest has:

- Name
- Date of birth
- Nationality
- Identity document
- Contact information

---

### Communication
Represents a communication submitted to
SES.HOSPEDAJES.

A communication contains one reservation
and all associated guests.

Its lifecycle is:

Draft
↓

Generated

↓

Submitted

↓
Cancelled (optional)

---

### Relationships

Accommodation
      ↓
Reservation
      ↓
Guest

Reservation
      ↓
Communication
      ↓
XML

### Design Principles
The application stores business information, not XML.
XML is generated only when required.
Validation occurs before XML generation.
Guest data is processed locally.
Personal data is minimized.
Temporary files are removed after use.

### Future Enhancements
Excel import
XML validation
Web interface
Multiple accommodations
Automated testing

### Why this matters
Something I learned during my years working with architects is this:

Code changes every week.

The domain changes very slowly.

If we get the domain right, everything else becomes much easier.
