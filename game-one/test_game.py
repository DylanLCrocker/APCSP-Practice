import pytest
import game

# Replace this template with at least three tests per game function:
# def test_describe_the_case():
#     assert game.your_function(chosen_input) == expected_result

def test_is_equal_distrabution():
    counts = [0, 0, 0]
    for i in range(0, 10000, 1):
        result = game.random_move()
        counts[result] += 1
    assert counts == pytest.approx([3333, 3333, 3333], rel=0.05)

def test_string_conversion() :
    assert game.convert_move_to_string(0) == "Rock"
    assert game.convert_move_to_string(1) == "Paper"
    assert game.convert_move_to_string(2) == "Scissors"

def test_find_winner() :
    assert game.find_winner("Scissors", "Scissors") == "Scissors = Scissors, It's a Tie"

def test_new_test() :
    pass

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
