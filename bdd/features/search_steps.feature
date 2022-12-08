Feature: search flow

    Scenario: perform search
        Given we access the google website
        And We fill in the search entry
        When we click the search button
        Then We should visualize the result