# Ontology Service User Guide

## Introduction
The Ontology Service is a Python-based tool that allows users to interact with the Ontology Lookup Service (OLS) API. It provides functionality to fetch and display details about ontologies in a user-friendly format.

## Modes of Usage
The service can be used in two modes:
1. **Interactive Mode:** Run the service as a standalone script to interact with the OLS API.
2. **Library Mode:** Use the service as a Python library in your own applications.

---

## Interactive Mode
### Running the Service
To run the service interactively:
1. Ensure you have Docker installed and set up.
2. Build the Docker container:
   ```bash
   make containers
   ```
3. Run the service in interactive mode:
   ```bash
   make run
   ```

### Usage Instructions
- If no arguments are provided, the script will prompt you to enter an ontology ID (e.g., `efo`).
- If an argument is provided, the script will directly fetch and display details about the specified ontology.

Example:
```bash
Please enter an ontology ID (e.g., 'efo'): efo
Ontology Title: Experimental Factor Ontology
Description: Ontology for experimental factors.
Number of Terms: 3000
Status: active
```

---

## Library Mode
### Using the Service as a Library
You can import and use the Ontology Service in your Python applications. Example:
```python
from ontology_service import OntologyService

# Initialise the service with an ontology ID
service = OntologyService("efo")

# Fetch ontology details
details = service.fetch_ontology_details()

# Display fetched details
print(details)
```

---

## Troubleshooting
- Ensure you have all dependencies installed by running:
  ```bash
  pip install -r requirements.txt
  ```
- For null or missing data, the service gracefully handles errors and provides meaningful feedback.

## Additional Resources
- [OLS API Documentation](https://www.ebi.ac.uk/ols/docs/)
- [GitHub Repository](https://github.com/sparkslabs/ols_example)
