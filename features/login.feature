Feature: Login
  
  Scenario: LG001 - insert character set into username
    Given Mobile change base url
    When insert value to username by "!@#$Test"
    Then check value from username by "Test"

  Scenario: LG002 - insert number into username
    When insert value to username by "1234Test"
    Then check value from username by "1234Test"

  Scenario: LG003 - insert number into username
    When insert value to username by "1234Test"
    Then check value from username by "1234Test"