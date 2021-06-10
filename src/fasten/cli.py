"""Console script for fasten."""
import logging

import click

from fasten.fasten import FastenPackage

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s:: %(message)s", level=logging.DEBUG
)
logger = logging.getLogger(__name__)
FastenPkg = FastenPackage()


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-f",
    "--forge",
    default="pypi",
    type=str,
    help="Forge of the package (pypi, mvn or debian)",
)
@click.option(
    "-v",
    "--version",
    default=None,
    type=str,
    help="Version of the package. By default it looks for the latest version on PyPI.",
)
@click.argument("pkg_name")
def check(forge, version, pkg_name):
    """
    Given a package name, FASTEN will return all metadata.

    Args:
        forge (str): Forge of the package (pypi, mvn or debian) - Default: pypi
        version (str): Package version - Default: latest known version
        pkg_name (str): Package name
    """
    logger.debug("Forge: %s, pkg name: %s, version: %s", forge, pkg_name, version)
    result = FastenPkg.get_pkg_metadata(forge, pkg_name, version)
    click.echo(f"Result:\n {result}\n")


@cli.command()
def check_all():
    """
    Given the output of `requirements.txt`, FASTEN will return all metadata for
    each package.
    """
    result = FastenPkg.get_pkglist_metadata
    click.echo(f"Results: \n{result}\n")
