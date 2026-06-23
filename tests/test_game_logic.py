from logic_utils import check_guess, update_score, get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_message_not_reversed():
    # FIX VERIFICATION: a too-high guess must tell the player to go LOWER
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message
    # a too-low guess must tell the player to go HIGHER
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_wrong_guess_never_adds_points():
    # FIX VERIFICATION: a wrong "Too High" guess should subtract, never add
    new_score = update_score(0, "Too High", 2)
    assert new_score < 0


def test_hard_is_harder_than_normal():
    # FIX VERIFICATION: Hard range should be wider than Normal
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high
