import pytest

from logic_utils import update_score


@pytest.mark.parametrize("outcome", ["Too High", "Too Low"])
@pytest.mark.parametrize("attempt_number", range(1, 21))
@pytest.mark.parametrize("current_score", [-10, 0, 100])
def test_incorrect_guesses_never_increase_score(current_score, outcome, attempt_number):
    new_score = update_score(current_score, outcome, attempt_number)

    assert new_score <= current_score
    assert new_score == current_score - 5


@pytest.mark.parametrize("attempt_number, bonus", [(1, 80), (2, 70), (8, 10), (20, 10)])
@pytest.mark.parametrize("current_score", [-10, 0, 100])
def test_winning_guess_increases_score(current_score, attempt_number, bonus):
    new_score = update_score(current_score, "Win", attempt_number)

    assert new_score > current_score
    assert new_score == current_score + bonus


def test_unknown_outcome_leaves_score_unchanged():
    assert update_score(100, "Unknown", 2) == 100
