"""General Client for interacting with GoDaddy API."""

import json
import warnings

import requests


class GoDaddy:
    """Basic Class to interact with the GoDaddy Domains API.

    https://developer.godaddy.com/doc/endpoint/domains
    """

    def __init__(self, key: str, secret: str, env: str = "PROD") -> None:
        """Initialise the class.

        Key & secret are available from: https://developer.godaddy.com/keys

        Args:
            key (str): API key
            secret (str): API secret
            env (str, optional): Whether to use PROD or OTE (test).
                - Defaults to "PROD".

        Raises:
            Exception: If an invalid environment is provided you'll be notified
        """
        self.key = key
        self.secret = secret

        # Validate the GoDaddy environment name
        if env not in ["OTE", "PROD"]:
            raise Exception("Acceptable GoDaddy environments are OTE or PROD")
        else:
            self.env = env

    def check_domain_availability(
        self, domains: list, extensions: list = [".com", ".com.au"]
    ) -> dict:
        """Bulk check of domain name availability.

        Method used: https://developer.godaddy.com/doc/endpoint/domains#/v1/availableBulk

        Args:
            domains (list): Domains to check for
            extensions (list, optional): Domain extentions to consider.
                - Defaults to [".com", ".com.au"].

        Returns:
            dict: Objects informing:
                - availability
                - price
                - currency
                - domain name
        """
        if self.env == "PROD":
            url = "https://api.godaddy.com/v1/domains/available"
        else:
            url = "https://api.ote-godaddy.com/v1/domains/available"

        params = {"checkType": "FULL"}

        domains = [
            f"{domain}{extension}" for domain in domains for extension in extensions
        ]
        payload = json.dumps(domains)

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"sso-key {self.key}:{self.secret}",
        }

        response = requests.request(
            "POST", url, headers=headers, data=payload, params=params
        )

        if "domains" in response.json():
            return response.json()  # type: ignore
        else:
            warnings.warn("Unable to retrieve domains")
            warnings.warn(json.dumps(response.json()))
            return {"domains": []}
