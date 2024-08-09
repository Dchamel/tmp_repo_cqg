from main import string_handler, open_files


def test01_string_handler():
    assert (string_handler(
        ['a=z', 'b=y', 'c=x'],
        ['jgrebk6hnae', 'cnhjrfyjvth3nxr', 'b#sjcf_ansvo!', 'djf#aemfaaofna%'])
            ==
            ['jgreyk6hnze', 'xnhjrfyjvth3nxr', 'y#sjxf_znsvo!', 'djf#zemfzzofnz%'])


def test02_string_handler():
    assert (string_handler(['a=z', 'b=y', 'c=x'], ['abc']) == ['zyx'])


def test03_open_files():
    """Check if open file function outputs tuple with correct data types"""
    test_data = open_files('rules.cfg', 'text.txt')
    assert (type(test_data) == tuple
            and type(test_data[0]) == list
            and type(test_data[1]) == list
            and type(test_data[0][0]) == str
            and type(test_data[1][0]) == str
            )
