from swdb import swdb

path = 'test/db'

def test_tags():
    expected = [
        {'tag': 'Database', 'count': 4},
        {'tag': 'Diff Viewer', 'count': 1},
        {'tag': 'Programming Language', 'count': 3},
        {'tag': 'Text Editor', 'count': 2},
    ]
    actual = swdb(path).tags()
    assert actual == expected

def test_info():
    expected = [
        {'name': 'Emacs'},
        {'name': 'Go'},
        {'name': 'MongoDB'},
        {'name': 'MySQL'},
        {'name': 'PostgreSQL'},
        {'name': 'Python'},
        {'name': 'Redis'},
        {'name': 'Rust'},
        {'name': 'Vim'},
    ]
    actual = swdb(path).info()
    assert actual == expected

def test_info_empty_name_returns_all():
    expected = [
        {'name': 'Emacs'},
        {'name': 'Go'},
        {'name': 'MongoDB'},
        {'name': 'MySQL'},
        {'name': 'PostgreSQL'},
        {'name': 'Python'},
        {'name': 'Redis'},
        {'name': 'Rust'},
        {'name': 'Vim'},
    ]
    actual = swdb(path).info(['--name', ''])
    assert actual == expected

def test_info_valid_name_returns_filtered():
    expected = [
        {'name': 'MySQL'},
        {'name': 'PostgreSQL'},
    ]
    actual = swdb(path).info(['--name', 'sql'])
    assert actual == expected

def test_info_invalid_name_returns_empty():
    expected = []
    actual = swdb(path).info(['--name', 'xxx'])
    assert actual == expected

def test_info_empty_tag_returns_all():
    expected = [
        {'name': 'Emacs'},
        {'name': 'Go'},
        {'name': 'MongoDB'},
        {'name': 'MySQL'},
        {'name': 'PostgreSQL'},
        {'name': 'Python'},
        {'name': 'Redis'},
        {'name': 'Rust'},
        {'name': 'Vim'},
    ]
    actual = swdb(path).info(['--tag', ''])
    assert actual == expected

def test_info_valid_tag_returns_filtered():
    expected = [
        {'name': 'Emacs'},
        {'name': 'Vim'},
    ]
    actual = swdb(path).info(['--tag', 'text'])
    assert actual == expected

def test_info_invalid_tag_returns_empty():
    expected = []
    actual = swdb(path).info(['--tag', 'xxx'])
    assert actual == expected

def test_info_valid_name_and_tag_returns_filtered():
    expected = [
        {'name': 'MongoDB'},
        {'name': 'PostgreSQL'},
    ]
    actual = swdb(path).info(['--name', 'o', '--tag', 'data'])
    assert actual == expected

def test_info_invalid_name_and_tag_returns_empty():
    expected = []
    actual = swdb(path).info(['--name', 'xxx', '--tag', 'data'])
    assert actual == expected
