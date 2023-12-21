Feature: login on the site

  Scenario Outline: sucessfully login

    Given that the user is on the login site
    When he types login data "<user>" "<password>"
    Then will see the "<text>" page
    Examples:
      | user | password | text      |
      | admin    | serenity | Dashboard |
