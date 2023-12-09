Feature: login on the site

  Scenario: sucessfully login

    Given that the user is on the login site
    When he types login data
    Then will see the dashboard page
