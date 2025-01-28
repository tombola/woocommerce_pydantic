import os

import pytest
from dotenv import find_dotenv, load_dotenv


def pytest_configure() -> None:
    """
    Pytest hook to configure the test environment.
    """
    env_file = find_dotenv(".env.tests")
    load_dotenv(env_file)
