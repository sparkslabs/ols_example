# Ontology Service

## Overview

The Ontology Service is a Python-based tool for interacting with the
Ontology Lookup Service (OLS) API. It allows users to fetch details
about ontologies and display them in a user-friendly format. The
service can be used either as an interactive script or as a library
within other Python applications.

---

## Features
- Fetch and display ontology details from the OLS API.
- Interactive and library usage modes.
- Containerised with Docker for easy deployment.
- Comprehensive testing with `unittest`.
- Ready for distribution via PyPI.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sparkslabs/ols_example.git
   cd ols_example
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Interactive Mode

Run the service as a standalone script:

```bash
python src/ontology_service.py
```

You can provide an ontology ID as an argument or enter it interactively.

### Library Mode

Use the service within your Python code:
```python
from ontology_service import OntologyService

service = OntologyService("efo")
details = service.fetch_ontology_details()
print(details)
```

---

## Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md)
file for guidelines.

---

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE)
file for details.

---

## Additional Resources
- [OLS API Documentation](https://www.ebi.ac.uk/ols/docs/)
- [GitHub Repository](https://github.com/sparkslabs/ols_example)
