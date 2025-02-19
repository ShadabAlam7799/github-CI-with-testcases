from src.math_operations import add,sub

#Test case 1
def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

#Test case 2
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1

#Test case 3
def test_custom():
    assert add(2,3)+sub(5,3)==7