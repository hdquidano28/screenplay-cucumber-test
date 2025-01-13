Feature: Recruitment functionality
  As a user
  I want to access recruitment
  So that I can create an interview

    Background:
    Given James is on the login page

  Scenario: Create a contract and interview
    Given create a contract
      | firstName |  middleName | lastName | email      | phone  | Keywords        |       notes        |
      | Helen  | Daya         |  Gonzalez     | geo@geo.com|676282  | java, js, python| QA test automation |
    When create an interview
      | name                 | interviewer_field | date_field |
      | Puesto de trabajo QA | Maximiliano       | 2025-01-15 |
    Then the interview is schedule Successful
    And offers a job 
    And hired the user


    