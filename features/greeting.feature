Feature: Greeting

  @id:greeting
  Scenario: Greeting
    Given user is on card page
    When user views the greeting
    Then user should see "Hi, my name is wclaytor!"
  

