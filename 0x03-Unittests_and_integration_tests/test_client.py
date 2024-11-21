#!/usr/bin/env python3
"""
Unit tests and integration tests for the client module.
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json: Mock):
        """Test GithubOrgClient.org with mocked get_json."""
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, {"login": org_name})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: Mock):
        """Test _public_repos_url property."""
        mock_org.return_value = {"repos_url": "http://some.url/repos"}
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, "http://some.url/repos")

    @patch("client.get_json")
    @patch(
        "client.GithubOrgClient._public_repos_url", new_callable=PropertyMock
    )
    def test_public_repos(self, mock_repos_url: Mock, mock_get_json: Mock):
        """Test public_repos method """
        mock_repos_url.return_value = "http://some.url/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, ["repo1", "repo2"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://some.url/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """Test has_license method."""
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [(org_payload, repos_payload, expected_repos, apache2_repos),]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up class with mocked requests.get."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,
            cls.repos_payload,
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher for requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method returns expected repos."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license argument."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
