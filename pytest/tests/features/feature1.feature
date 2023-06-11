@featuretag
Feature: API Testing
  @scenariotag
  Scenario Outline: Retrieve user information
    Given I have the user ID <userid>
    When I request user information for ID <userid2>
    Then the response status code should be <statuscode>
    And the response body should contain <expected>

    Examples:
      | userid   | userid2    | statuscode | expected |
      | Deepak | deepakdas| 200        | 888    |
      | John   | johndoe  | 404        | User not found |
      | Meenakshi| buli   | 100        | chikimon |
