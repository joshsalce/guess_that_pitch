import pytest
import functions as func

def test_outs_plus():
    assert isinstance(func.outs_plus([1,2,3],"Outs + 3", 2),list)
    assert len(func.outs_plus([1,2,3],"Outs + 3", 2)) == 5
    assert max(func.outs_plus([1,2,3],"Outs + 3", 2)) > 0 and max(func.outs_plus([1,2,3],"Outs + 3", 2)) < 6

def test_chase_the_func():
    assert isinstance(func.chase_the_func([2,3,1],1),list)
    assert func.chase_the_func([2,3,1],1)[-1] != 1
    assert 1 in func.chase_the_func([2,3,1],1)[:-1]

def test_edit_values():
    assert isinstance(func.edit_values([1,2,3],3),list)
    assert 1 not in func.edit_values([1,1,1,2], 1)
    assert max(func.edit_values([1,1,1,2], 1)) > 0 and max(func.edit_values([1,1,1,2], 1)) < 6
    
def test_second_sign():
    assert isinstance(func.second_sign([1,2,3,4,5], 5), list)
    assert 5 in func.second_sign([1,2,3,4,5], 5)[:-2]
    assert 5 not in func.second_sign([1,2,3,4,5], 5)[-2:]
    
def test_generate_sequence():
    assert isinstance(func.generate_sequence(),list)
    assert len(func.generate_sequence()) >= 3 and len(func.generate_sequence()) <= 5
    assert max(func.generate_sequence()) > 0 and max(func.generate_sequence()) < 6

test_outs_plus()
test_chase_the_func()    
test_edit_values()
test_second_sign()  
test_generate_sequence()



                 
    