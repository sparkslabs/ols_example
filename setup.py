from setuptools import setup, find_packages

setup(
    name="ontology_service",
    version="0.1.0",
    author="Michael Sparks",
    author_email="sparks.m@gmail.com",
    description="A Python service to interact with the Ontology Lookup Service (OLS) API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sparkslabs/ols_example",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "ontology-service=ontology_service:main",
        ],
    },
)
