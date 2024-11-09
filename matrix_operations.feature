Feature: Matrix operations

  Scenario: Adding two matrices
    Given I have matrix A
    And I have matrix B
    When I calculate the result of adding the matrices
    Then I should get the resulting matrix

  Scenario: Multiplying two matrices
    Given I have matrix A
    And I have matrix B
    When I calculate the result of multiplying the matrices
    Then I should get the resulting matrix

  Scenario: Adding two sparse matrices
    Given I have sparse matrix A
    And I have sparse matrix B
    When I calculate the result of adding the sparse matrices
    Then I should get the resulting sparse matrix


