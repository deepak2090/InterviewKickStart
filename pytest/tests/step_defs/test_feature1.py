from pytest_bdd import given, when, then, scenarios,parsers

scenarios('../features')


@given(parsers.parse('I have the user ID {userid}'))
def have_user_id(userid):
    # Perform any necessary setup without using a parameter
    #x = argparse('I have the user ID "{userid}')
    #print(x)
    print("the user id is", userid)
    pass




@then(parsers.parse('the response status code should be {statuscode}'))
def verify_status_code( statuscode):
    # Perform assertions on the response status code
    print(statuscode)
    pass


@then(parsers.parse('the response body should contain {expected}'))
def verify_response_body(expected):
    # Perform assertions on the response body
    print(expected)
    pass

