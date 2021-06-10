"""Main module."""
import logging
from typing import Any, Dict, List

import requests

logger = logging.getLogger(__name__)
BASE_URL = "https://api.fasten-project.eu/api/"


class FastenPackage:
    def __init__(self, url: str, forge: str, pkg_name: str, pkg_version: str):
        self.url = url
        self.forge = forge
        self.pkg_name = pkg_name
        self.pkg_version = pkg_version

    def get_pkg_metadata(self) -> Any:
        """
        Requests the package metadata from FASTEN's RESTAPI

        Args:
            forge (str): Forge of the package - Default: pypi
            pkg_name (str): Package name
            pkg_version (str): Package version
        """
        if self.pkg_version is None:
            self.pkg_version = self.get_pkg_version(self.forge, self.pkg_name)
            logger.debug("package version: %s", self.pkg_version)

        logger.info(
            "Retrieving metadata for: %s/%s/%s...", self.forge, self.pkg_name, self.pkg_version
        )
        url = f"{self.url}/{self.forge}/packages/{self.pkg_name}/{self.pkg_version}"
        print(url)
        logger.debug(url)

        res = requests.get(url)

        if res.ok:
            logger.debug("Request status code: %s", res.status_code)
            return res.json()
        # TODO: raise exception for errors like 404 - req.ok(true/false)
        return res.text

    def get_pkg_version(self, forge: str, pkg_name: str) -> str:
        """
        Get the latest know version of a given package

        Args:
            forge (str): Package forge
            pkg_name (str): Package name
        """
        version = "1.1"
        # TODO: implement a way to get the latest version of a package from the RESTAPI
        return version

    def get_pkglist_metadata(self, pkgs_list) -> List[Dict[str, str]]:
        # get a list from requirements.txt
        pkgs_list = [
            {
                "name": "test_pkg1",
                "version": "version_test_pkg1",
                "forge": "test_pkg_forge1",
            },
            {
                "name": "test_pkg2",
                "version": "version_test_pkg2",
                "forge": "test_pkg_forge2",
            },
        ]
        logger.info("Retrieving metadata for the packages: %s", pkgs_list)

        result = []
        # for each pkg, run check and return its metadata.
        for pkg in pkgs_list:
            result.append(
                self.get_pkg_metadata(pkg["forge"], pkg["name"], pkg["version"])
            )

        return result
