
import pick

def test_check_guess_correct():
    correct_answer = pick.check_guess(1,1)
    assert correct_answer == 0    

def test_check_guess_too_low():
    incorrect_answer = pick.check_guess(1,2)
    assert incorrect_answer == 1

def test_check_guess_too_high():
    incorrect_answer = pick.check_guess(2,1)
    assert incorrect_answer == 1




