# Ontology Service Developer Guide

## Introduction
This guide is intended for developers who wish to contribute to or extend the Ontology Service. It covers the project structure, testing, build processes, and CI/CD integration.

---

## Project Structure
```
/app
├── src/
│   └── ontology_service.py   # Core service implementation
├── tests/                    # Unit tests
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions workflow for CI/CD
├── Dockerfile                # Main runtime Dockerfile
├── Dockerfile_test           # Dockerfile for running tests
├── requirements.txt          # Dependencies
├── Makefile                  # Build and test commands
├── setup.py                  # PyPI package configuration
└── README.md                 # Project overview and usage
```

---

## Development Workflow

### Setting Up the Development Environment

First of all create a fork of this project. The URL below assumes your URL
not the project's URL

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url/ols_example.git
   cd ols_example
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Service Locally
To run the service locally, execute:
```bash
python src/ontology_service.py
```

---

## Testing
### Running Tests Locally
Run tests using `unittest`:
```bash
python -m unittest discover -s tests
```

### Running Tests in Docker
1. Build the test container:
   ```bash
   make containers
   ```
2. Execute tests inside the container:
   ```bash
   make test
   ```

---

## Continuous Integration and Deployment (CI/CD)

### Overview of GitHub Actions

The project uses GitHub Actions for CI/CD, configured in `.github/workflows/ci.yml`. Key stages:

1. **Test Stage:**
   - Runs all tests using `unittest` to ensure code quality.

2. **Packaging Stage:**
   - Builds distribution artifacts (`sdist` and `bdist_wheel`) for PyPI.

### Viewing Results

1. Navigate to the "Actions" tab in the GitHub repository.

2. Select the latest workflow run to view test results and packaging details.

### Accessing Distribution Artifacts

1. After a successful packaging stage, artifacts are uploaded to the workflow run.

2. Download them directly from the "Artifacts" section of the GitHub Actions interface. (NOTE: This is TBD)

---

## Packaging and Deployment

### Creating a PyPI Package Locally

1. Build the distribution files:
   ```bash
   make pypi
   ```

2. Upload the package to PyPI:
   ```bash
   twine upload dist/*
   ```

### Docker Deployment

To deploy the service as a Docker container:

1. Build the container:
   ```bash
   make container
   ```

2. Run interactively:
   ```bash
   make run
   ```

---

## Contribution Guidelines

1. Fork the repository and create a feature branch:
   ```bash
   git checkout -b feature/my-new-feature
   ```

2. Submit pull requests with clear commit messages.

3. Ensure all tests pass locally and in CI before submission.

---

## Additional Resources
- [OLS API Documentation](https://www.ebi.ac.uk/ols/docs/)
- [GitHub Repository](https://github.com/sparkslabs/ols_example)
