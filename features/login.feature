Feature: Login
  
  Scenario: TC0007 - login
    Given Mobile change base url
      And Mobile login as "USER1"
    #   And wait until loader finish
    #   And click finger skip