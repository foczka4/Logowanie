Feature: Policz liczbe procesorow

Scenario: Uruchom test
    Given Jestem zalogowany na komputerze
    When Sprawdzam liczbe procesorow
    Then Ilosc procesorow rowna 2
