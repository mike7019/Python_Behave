Feature: testing the serenity demo page

  Background:

  Scenario Outline:

    Given that the user is on the login site
    When he types login data "<username>" "<password>"
      | browser   | url   | user   | password   |
      | <browser> | <url> | <user> | <password> |
    Examples:
      | browser | url                                                   | user  | password |
      | chrome  | https://demo.serenity.is/Account/Login/?ReturnUrl=%2F | admin | serenity |

  Scenario: actor wants to create an unit business

    When actor creates a new unit bussiness
    Then actor will see the unit created

