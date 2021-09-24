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
