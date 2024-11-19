#!/usr/bin/python
"""
Copyright 2024 Michael Sparks

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
#!/usr/bin/python

import requests
import logging

logging.basicConfig(level=logging.INFO)

class OntologyService:
    """A class to interact with the Ontology Lookup Service API"""

    BASE_URL = "https://www.ebi.ac.uk/ols/api/ontologies"

    def __init__(self, ontology_id):
        self.ontology_id = ontology_id

    def fetch_ontology_details(self):
        """
        Fetch ontology details from the Ontology Lookup Service.

        Returns:
            dict: A dictionary containing ontology details or error information.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/{self.ontology_id}")
            response.raise_for_status()  # Raises an HTTPError for bad HTTP responses (4xx and 5xx)

            data = response.json()
            return {
                "Title": data.get("config", {}).get("title", "No title available"),
                "Description": data.get("config", {}).get("description", "No description available"),
                "Number of Terms": data.get("numberOfTerms", "Not available"),
                "Status": data.get("status", "Unknown"),
            }
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request error occurred: {req_err}")
            return {"error": f"Request error occurred: {req_err}"}

    def format_details(self):
        """
        Format the fetched ontology details for display.

        Returns:
            str: A human-readable string representation of the ontology details.
        """
        details = self.fetch_ontology_details()

        if "error" in details:
            return details["error"]
        else:
            return (
                f"Ontology Title: {details['Title']}\n"
                f"Description: {details['Description']}\n"
                f"Number of Terms: {details['Number of Terms']}\n"
                f"Status: { details['Status']}"
            )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch details of an ontology from OLS.")
    parser.add_argument("ontology_id", nargs="?", help="The ID of the ontology to fetch (e.g., 'efo')")

    args = parser.parse_args()

    if args.ontology_id:
        # Argument provided, lookup the ontology ID directly
        ontology_service = OntologyService(args.ontology_id)
        print(ontology_service.format_details())
    else:
        # Interactive mode
        user_input = input("Please enter an ontology ID (e.g., 'efo'): ").strip()
        if user_input:
            ontology_service = OntologyService(user_input)
            print(ontology_service.format_details())
        else:
            print("No ontology ID provided. Exiting.")
