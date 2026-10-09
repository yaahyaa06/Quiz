from project import check_answer , calculate_score, get_result

def test_check_answer():
    assert check_answer(1, 1) ==True
    assert check_answer(1, 2) == False

def test_calculate_score():
    assert calculate_score(0, True) ==1
    assert calculate_score(1, False)==1   

def test_get_result():
    assert get_result(10,10)=="Excellent!"
    assert get_result(8,10)=="Good!"
    assert get_result(3,10)=="Keep practicing"
