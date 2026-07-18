# SES-hospedajes-assistant
A privacy-conscious Python tool for validating guest registration data and generating XML communications compatible with Spain’s SES.Hospedajes platform.

🚧**Status:** Early development (v0.1)

 The project currently supports:
 - Reading reservation data from Excel
 - Domain modelling
 - XML generation (work in progress)
 - Validation engine (in progress)

---

## Overview

The Spanish **SES.HOSPEDAJES** platform requires accommodation providers to submit guest registration data in a specific XML format.

While the platform performs validation during submission, it does not provide a draft workflow for progressively preparing reservations. As a result, errors are often discovered only after uploading the XML, leaving accommodation providers to correct them under time pressure, sometimes just before guest check-in.

This project was inspired by the practical challenges faced by rural accommodation providers using the SES.HOSPEDAJES platform. It aims to reduce last-minute validation errors by allowing reservations to be prepared and verified locally before submission.

The application is intentionally designed following **privacy-by-design** principles and processes guest information locally.

---

## Objectives

- Simplify the preparation of guest registration data
- Detect errors before submission
- Generate SES-compatible XML files
- Reduce manual work and repeated submissions
- Follow GDPR data minimization principles
- Provide a clean, maintainable and extensible architecture

---

## Who is this for?

The intended audience for this solution are: 

- Rural accommodation providers
- Holiday rental managers
- Software developers integrating with SES.HOSPEDAJES
- Python developers interested in XML automation
---


## Features

- Read reservation and guest data from Excel
- Validate mandatory fields before XML generation
- Detect incomplete or inconsistent guest information
- Validate reservation dates
- Generate XML using the official SES structure
- Produce human-readable validation reports
- Process all data locally
- Use fictional sample data only

---

## Installation

```bash
git clone https://github.com/tmillan123/SES-hospedajes-assistant.git

cd SES-hospedajes-assistant

pip install -r requirements.txt

---

## Project Workflow

```
Excel Reservation Data
          │
          ▼
 Data Validation
          │
          ▼
 Validation Report
          │
          ▼
 XML Generation
          │
          ▼
 Manual Upload to SES.HOSPEDAJES

---

## Project Structure

ses-hospedajes-assistant/
│
├── docs/
├── examples/
├── output/
├── src/
├── templates/
├── tests/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Architecture

src/
│
├── excel_reader.py
│      Reads reservation data
│
├── validator.py
│      Validates business rules
│
├── models.py
│      Domain objects
│
├── xml_generator.py
│      Generates SES XML
│
├── config.py
│      Configuration
│
└── main.py
       Coordinates the workflow

---


## Validation

Examples of validation rules include:

- Missing mandatory fields
- Invalid email addresses
- Invalid phone numbers
- Missing identity document information
- Invalid reservation dates
- Inconsistent guest counts
- XML structure validation

### Validation failed

Guest 4:
- Missing phone number

Guest 7:
- Invalid email address

Reservation:
- Check-out date must be later than check-in date

Guest count mismatch:
Declared: 14
Found: 13
```
### 5. Add Running Tests

Later:

```markdown
## Running tests

pytest

---

## Why this project?

Many software projects demonstrate programming skills.

This project demonstrates something different:

- understanding of a regulated business process
- requirements analysis
- secure software design
- privacy-by-design principles
- domain modelling
- maintainable architecture

The objective is not simply to generate XML, but to design software that solves a real operational problem faced by accommodation providers while reducing the likelihood of errors during guest registration.



---

## Why Python?

Python was chosen because of its mature XML libraries, excellent data-processing ecosystem, and suitability for automation tasks involving structured business data.


## Privacy by Design

This project has been designed with privacy as a primary objective.

Key principles include:

- Local processing only
- No transmission of guest information to third-party services
- No storage of document images
- Data minimization
- Fictional sample data only
- No production establishment identifiers included in the repository

This repository intentionally contains **no personal data**.

---

## Technologies

- Python
- openpyxl
- xml.etree.ElementTree
- pytest

Future versions may include:

- Streamlit
- Docker
- GitHub Actions
- XML Schema validation
- Automated testing


---

## Example Usage

```bash
python src/main.py examples/sample_reservation.xlsx

Output:

Reservation validated successfully.

Guests processed: 13

XML generated:
output/guest_communication.xml

---

## Roadmap

### Version 0.1

- Read Excel reservations
- Generate SES XML
- Documentation
- Sample data

### Version 0.2

- Complete validation engine
- Unit tests
- Improved error reporting

### Version 0.3

- Configuration files
- Multiple accommodation support
- XML schema validation

### Version 1.0

- Web interface
- Docker deployment
- GitHub Actions CI
- Complete documentation

---

## Disclaimer

This is an independent technical project created for educational and software engineering purposes.

It is **not affiliated with**, endorsed by, or maintained by the Spanish Ministry of the Interior or the SES.HOSPEDAJES platform.

Users remain responsible for reviewing generated communications before submission.

---

## What This Project Demonstrates

Beyond XML generation, this project showcases:

- Requirements analysis
- Business process automation
- Software architecture
- Secure-by-design thinking
- Privacy-by-design principles
- Data validation
- XML processing
- Clean Python architecture
- Technical documentation
- Testable software design

The focus is not simply generating XML files, but designing a reliable, maintainable solution that improves a real-world regulated workflow while respecting privacy requirements.
