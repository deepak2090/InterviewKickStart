from pytest_bdd import scenarios, parsers, given, when
import pytest
import sys
import os

features_dir = os.path.dirname(os.path.abspath(__file__))
# Locate the feature files
features_dir = os.path.join(features_dir, '../tests/features')
sys.path.append(features_dir)

@when(parsers.parse("I request user information for ID {userid2}"))
def request_user_info(userid2):
    # Make an API request without using a parameter
    userid2 += ' XXXXX'
    print("the second user id is", userid2)
    print("1111111")
    return userid2, type(userid2)

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "mytag: mark tests with mytag"
    )
