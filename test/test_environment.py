import os
import sys

import pytest
import toml


def test_poetry_environment():
    poetry_venv = os.environ.get("VIRTUAL_ENV")
    assert poetry_venv is not None, "Poetry environment not detected."
    assert sys.prefix.startswith(poetry_venv), "Poetry environment not active."


def get_packages_from_toml():
    with open("./pyproject.toml") as file:
        pyproject = toml.load(file)

    dependencies = pyproject["tool"]["poetry"]["dependencies"]
    return [(pkg, version) for pkg, version in dependencies.items() if pkg != "python"]


@pytest.mark.parametrize("package, version_spec", get_packages_from_toml())
def test_installed_packages(package, version_spec):
    try:
        _ = __import__(package)
    except ModuleNotFoundError:
        pytest.fail(f"Package '{package}' not found in the Poetry environment.")
