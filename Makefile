# Variables
IMAGE_NAME = ontology_service_image
TEST_IMAGE_NAME = test_ontology_service_image
CONTAINER_NAME = ontology_service_container

# Display help
help:
	@echo "Available targets:"
	@echo "  containers - Build runtime and test Docker containers"
	@echo "  test       - Run tests inside the test container"
	@echo "  run        - Run the code interactively"
	@echo "  pypi       - Package the project for PyPI"
	@echo "  clean      - Tidy up this directory"

# Default target
all: container

# Build the Docker container
containers:
	docker build -t $(IMAGE_NAME) -f Dockerfile .
	docker build -t $(TEST_IMAGE_NAME) -f Dockerfile_test .

# Run the tests inside the container
test:
	docker run --rm $(TEST_IMAGE_NAME) python -m unittest discover -s tests

# Run the code in interactive form
run:
	docker run --rm -it $(IMAGE_NAME)

# Package the project for PyPI
pypi:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf dist *.egg-info build

