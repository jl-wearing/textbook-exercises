import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be used to test all functions."""
    question = "What programming language did you learn first?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    #function to be tested.
    language_survey.store_response("Python")
    assert 'python' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that 3 individual responses are stored properly."""

    responses = ['C', 'Java', 'python']

    #function to be tested.
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response.lower() in language_survey.responses

#A fixture helps set up a testing environment.
#Often this involves creating a resource that is used by more than one test.
#We create a fixture using a decorator.
#A decorator is a directive placed just before a function definition.