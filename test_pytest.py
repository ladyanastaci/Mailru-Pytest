import pytest


def test_concat():
    assert '.'.join(['asd', 'asd']) == 'asd.asd'
    assert ''.join(['asd', 'asd']) == 'asdasd'
    assert ''.join([]) == ''


def test_isalpha():
    assert '123'.isalpha() == False
    assert 'asd'.isalpha() == True
    assert ''.isalpha() == False


def test_startsWith():
    assert 'asddsa'.startswith('asd') == True
    assert 'asdsa'.startswith('dsa') == False
    assert 'asd'.startswith('') == True


def test_setPop():
    assert {1, 2, 3}.pop() == 1

    set_data = {1, 2, 3}
    set_data.pop()
    assert set_data == {2, 3}
    with pytest.raises(TypeError):
        {}.pop()


def test_intersection():
    assert {1, 2, 3}.intersection({2}) == {2}
    assert set().intersection({2}) == set()
    assert {1, 2, 3}.intersection(set()) == set()
    assert set().intersection(set()) == set()


def asd():
    assert {1, 2, 3} - {2, 3} == {1}
    assert set() - {2, 3} == set()
    with pytest.raises(TypeError):
        a = set() * set()