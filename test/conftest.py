import pytest
import os


@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, "test.csv"), "w+") as c:
        yield "csv file!"

def pytest_addoption(parser):
    parser.addoption("--os-name", default="linux", help="os name")


