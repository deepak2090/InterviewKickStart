@featuretag
Feature: API Testing
  @scenariotag
  Scenario Outline: Retrieve user information
    Given I have the user ID <userid>
    When I request user information for ID <userid2>
    Then the response status code should be <statuscode>
    And the response body should contain <expected>
    And the tree structure should match the following YAML file <yaml_file>

    Examples:
      | userid   | userid2    | statuscode | expected | yaml_file| 
      | Deepak | deepakdas| 200        | 888    | /Users/deepakdas/InterviewKickStart/InterviewKickStart-1/pytest/tests/data/testdata.yaml |
      | John   | johndoe  | 404        | User not found | /Users/deepakdas/InterviewKickStart/InterviewKickStart-1/pytest/tests/data/testdata.yaml|
      | Meenakshi| buli   | 100        | chikimon | /Users/deepakdas/InterviewKickStart/InterviewKickStart-1/pytest/tests/data/testdata.yaml |
