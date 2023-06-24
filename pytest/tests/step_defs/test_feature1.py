from multiprocessing import context

from pytest_bdd import given, when, then, scenarios,parsers, scenario
import pytest
import yaml
import os

scenarios('../features')


@given(parsers.parse('I have the user ID {userid}'))
def have_user_id(userid):
    # Perform any necessary setup without using a parameter
    #x = argparse('I have the user ID "{userid}')
    #print(x)
    print("the user id is", userid)
    context.userid = userid
    pass




@then(parsers.parse('the response status code should be {statuscode}'), converters= {'statuscode' : float})
def verify_status_code( statuscode):
    # Perform assertions on the response status code
    print(statuscode,"the user id1 is", context.userid)
    pass


@then(parsers.parse('the response body should contain {expected}'))
def verify_response_body(expected):
    # Perform assertions on the response body
    print(expected)
    pass

@then(parsers.parse('the tree structure should match the following YAML file {yaml_file}'))
def verify_tree_structure(yaml_file_path, yaml_file):
    x = yaml_file_path
    pathplaceholder = '#path#'
    if '#path#' in yaml_file:
        pathplaceholder = pathplaceholder.replace('#path#', x)
        yaml_file = yaml_file.replace('#path#/', '')
        fullpath = os.path.join(pathplaceholder, yaml_file)
    fullpath = os.path.join(yaml_file_path, yaml_file)
    with open(fullpath, 'r') as file:
        print(fullpath)
        tree_structure = yaml.load(file, Loader=yaml.Loader)
        print(tree_structure)

