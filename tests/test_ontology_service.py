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

import unittest
from unittest.mock import patch
from ontology_service import OntologyService
import requests

class TestOntologyService(unittest.TestCase):

    @patch("ontology_service.requests.get")
    def test_fetch_ontology_details_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "config": {"title": "Example Ontology", "description": "This is a test ontology."},
            "numberOfTerms": 100,
            "status": "active",
        }

        service = OntologyService("test")
        details = service.fetch_ontology_details()

        self.assertEqual(details["Title"], "Example Ontology")
        self.assertEqual(details["Description"], "This is a test ontology.")
        self.assertEqual(details["Number of Terms"], 100)
        self.assertEqual(details["Status"], "active")

    @patch("ontology_service.requests.get")
    def test_fetch_ontology_details_404(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

        service = OntologyService("invalid")
        details = service.fetch_ontology_details()

        self.assertIn("error", details)
        self.assertIn("HTTP error occurred", details["error"])

    @patch("ontology_service.requests.get")
    def test_fetch_ontology_details_request_exception(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Connection Error")

        service = OntologyService("test")
        details = service.fetch_ontology_details()

        self.assertIn("error", details)
        self.assertIn("Request error occurred", details["error"])

    @patch("ontology_service.OntologyService.fetch_ontology_details")
    def test_format_details_success(self, mock_fetch_details):
        mock_fetch_details.return_value = {
            "Title": "Example Ontology",
            "Description": "This is a test ontology.",
            "Number of Terms": 100,
            "Status": "active",
        }

        service = OntologyService("test")
        formatted_details = service.format_details()

        self.assertIn("Ontology Title: Example Ontology", formatted_details)
        self.assertIn("Description: This is a test ontology.", formatted_details)
        self.assertIn("Number of Terms: 100", formatted_details)
        self.assertIn("Status: active", formatted_details)

    @patch("ontology_service.OntologyService.fetch_ontology_details")
    def test_format_details_error(self, mock_fetch_details):
        mock_fetch_details.return_value = {"error": "An error occurred"}

        service = OntologyService("test")
        formatted_details = service.format_details()

        self.assertEqual(formatted_details, "An error occurred")


if __name__ == "__main__":
    unittest.main()
