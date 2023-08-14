from cgi import test
from pytest_bdd import scenarios, parsers, given, when
import pytest
#import pytest_html
#from pytest_html import html
import sys
import os

features_dir = os.path.dirname(os.path.abspath(__file__))
# Locate the feature files
features_dir = os.path.join(features_dir, '../tests/features')
sys.path.append(features_dir)

def pytest_html_report_title(report):
    report.title = "Deepak Report"

from pytest_metadata.plugin import metadata_key


def pytest_configure(config):
    config.stash[metadata_key]["foo"] = "bar"

import pytest
from pytest_metadata.plugin import metadata_key


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["foo"] = "bar"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["<p>foo: bar</p>"])
    
@when(parsers.parse("I request user information for ID {userid2}"))
def request_user_info(userid2):
    # Make an API request without using a parameter
    userid2 += ' XXXXX'
    print("the second user id is", userid2)
    print("1111111")
    return userid2, type(userid2)

#this code is not needed for identifying tags
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "mytag: mark tests with mytag"
    )

pathconf = os.path.dirname(os.path.abspath(__file__))
print(pathconf)
@pytest.fixture
def yaml_file_path():
    # Modify the path of testdata.yaml here
    testdata_path = os.path.join(pathconf, "tests/data/")
    print("path is ", testdata_path)
    return testdata_path
"""
@pytest.mark.optionalhook
def pytest_configure(config):
    config._metadata['Project'] = 'API Testing'
    config._metadata['Module'] = 'test_api'
    config._metadata['Tester'] = 'Your Name'
    config._metadata['Environment'] = 'Test'
    config.option.htmlpath = 'reports/report.html'  # Set the report output directory and file name

# Add a custom marker for pytest-html report
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test Data'))

def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.data.get('TestData', '')))

def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]

"""