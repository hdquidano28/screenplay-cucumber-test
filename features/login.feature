Feature: Login functionality
  As a user
  I want to login to the application
  So that I can create a contract

  Scenario: Successful login with valid credentials
    Given James is on the login page
    When he enters his credentials
      | username | password |
      | Admin     | admin123  |
    And he should see the dashboard
    Then create a contract
      | firstName |  middleName | lastName | email      | phone  | Keywords        |       notes        |
      | Helen  | Daya         |  Gonzalez     | geo@geo.com|676282  | java, js, python| QA test automation |
    Then create an interview
      |       name           | interviewer_field | date_field |
      | Puesto de trabajo QA | Maximiliano       | 2025-15-01 |


    
