import csv
import re
import pytest


def pytest_addoption(parser):
    testplan = parser.getgroup('testplan')
    testplan.addoption("--testplan",
                       action="store",
                         default=None,
                       help="generate csv containing test metadata and exit without running test.")


def pytest_collection_modifyitems(session, config, items):
    path = config.getoption('--testplan')
    if path:
        # generate test plan CSV and exit without running tests
        with open(path, mode='w') as fd:
            writer = csv.writer(fd, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["title", "description", "markers"])
            for item in items:
                if item.cls:
                    title = f"{item.module.__name__}.py::{item.cls.__name__}::{item.name}"
                else:
                    title = f"{item.module.__name__}.py::{item.name}"
                # if not item.string is None:
                description = re.sub('\n+', '\n', item.obj.__doc__.strip())
                markers = ','.join([m.name for m in item.iter_markers()])

                writer.writerow([title, description, markers])

        pytest.exit(f"Generated test plan: {path}")
