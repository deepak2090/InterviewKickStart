Feature: API Testing

  Scenario: Retrieve user information
    Given I have the user ID <userid>
    When I request user information for ID <userid2>
    Then the response status code should be <statuscode>
    And the response body should contain <exepected>

    Examples:
        | userid | userid2|statuscode | expected |
        | "Deepak"  | "deepakdas" |200 | 888|
        |"Meenakshi"|"Mohanty"|300| 777|
