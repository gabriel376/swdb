from swdb import swdb

path = 'test/db'

def test_tags():
    expected = [
        {'tag': 'Browser', 'count': 1},
        {'tag': 'Database', 'count': 5},
        {'tag': 'Diff Viewer', 'count': 1},
        {'tag': 'Programming Language', 'count': 3},
        {'tag': 'Project Management', 'count': 1},
        {'tag': 'Text Editor', 'count': 4},
    ]
    actual = swdb(path).tags()
    assert actual == expected

def test_info():
    expected = [
        {'name': 'Emacs', 'organization': 'GNU'},
        {'name': 'Go', 'organization': ''},
        {'name': 'Microsoft Edge', 'organization': 'Microsoft'},
        {'name': 'Microsoft Project', 'organization': 'Microsoft'},
        {'name': 'Microsoft SQL Server', 'organization': 'Microsoft'},
        {'name': 'MongoDB', 'organization': ''},
        {'name': 'MySQL', 'organization': ''},
        {'name': 'PostgreSQL', 'organization': ''},
        {'name': 'Python', 'organization': ''},
        {'name': 'Redis', 'organization': ''},
        {'name': 'Rust', 'organization': ''},
        {'name': 'Sublime Text', 'organization': ''},
        {'name': 'Vim', 'organization': ''},
        {'name': 'Visual Studio Code', 'organization': 'Microsoft'},
    ]
    actual = swdb(path).info()
    assert actual == expected

def test_info_empty_name_returns_all():
    expected = [
        {'name': 'Emacs', 'organization': 'GNU'},
        {'name': 'Go', 'organization': ''},
        {'name': 'Microsoft Edge', 'organization': 'Microsoft'},
        {'name': 'Microsoft Project', 'organization': 'Microsoft'},
        {'name': 'Microsoft SQL Server', 'organization': 'Microsoft'},
        {'name': 'MongoDB', 'organization': ''},
        {'name': 'MySQL', 'organization': ''},
        {'name': 'PostgreSQL', 'organization': ''},
        {'name': 'Python', 'organization': ''},
        {'name': 'Redis', 'organization': ''},
        {'name': 'Rust', 'organization': ''},
        {'name': 'Sublime Text', 'organization': ''},
        {'name': 'Vim', 'organization': ''},
        {'name': 'Visual Studio Code', 'organization': 'Microsoft'},
    ]
    actual = swdb(path).info(['--name', ''])
    assert actual == expected

def test_info_valid_name_returns_filtered():
    expected = [
        {'name': 'Microsoft SQL Server', 'organization': 'Microsoft'},
        {'name': 'MySQL', 'organization': ''},
        {'name': 'PostgreSQL', 'organization': ''},
    ]
    actual = swdb(path).info(['--name', 'sql'])
    assert actual == expected

def test_info_invalid_name_returns_empty():
    expected = []
    actual = swdb(path).info(['--name', 'xxx'])
    assert actual == expected

def test_info_empty_tag_returns_all():
    expected = [
        {'name': 'Emacs', 'organization': 'GNU'},
        {'name': 'Go', 'organization': ''},
        {'name': 'Microsoft Edge', 'organization': 'Microsoft'},
        {'name': 'Microsoft Project', 'organization': 'Microsoft'},
        {'name': 'Microsoft SQL Server', 'organization': 'Microsoft'},
        {'name': 'MongoDB', 'organization': ''},
        {'name': 'MySQL', 'organization': ''},
        {'name': 'PostgreSQL', 'organization': ''},
        {'name': 'Python', 'organization': ''},
        {'name': 'Redis', 'organization': ''},
        {'name': 'Rust', 'organization': ''},
        {'name': 'Sublime Text', 'organization': ''},
        {'name': 'Vim', 'organization': ''},
        {'name': 'Visual Studio Code', 'organization': 'Microsoft'},
    ]
    actual = swdb(path).info(['--tag', ''])
    assert actual == expected

def test_info_valid_tag_returns_filtered():
    expected = [
        {'name': 'Emacs', 'organization': 'GNU'},
        {'name': 'Sublime Text', 'organization': ''},
        {'name': 'Vim', 'organization': ''},
        {'name': 'Visual Studio Code', 'organization': 'Microsoft'},
    ]
    actual = swdb(path).info(['--tag', 'text'])
    assert actual == expected

def test_info_invalid_tag_returns_empty():
    expected = []
    actual = swdb(path).info(['--tag', 'xxx'])
    assert actual == expected

def test_info_valid_name_and_tag_returns_filtered():
    expected = [
        {'name': 'Microsoft SQL Server', 'organization': 'Microsoft'},
        {'name': 'MongoDB', 'organization': ''},
        {'name': 'PostgreSQL', 'organization': ''},
    ]
    actual = swdb(path).info(['--name', 'o', '--tag', 'data'])
    assert actual == expected

def test_info_invalid_name_and_tag_returns_empty():
    expected = []
    actual = swdb(path).info(['--name', 'xxx', '--tag', 'data'])
    assert actual == expected

def test_info_source_open_returns_filtered():
    expected = [
        {'name': 'Emacs', 'organization': 'GNU'},
        {'name': 'MongoDB', 'organization': ''},
        {'name': 'MySQL', 'organization': ''},
        {'name': 'PostgreSQL', 'organization': ''},
        {'name': 'Redis', 'organization': ''},
        {'name': 'Vim', 'organization': ''},
        {'name': 'Visual Studio Code', 'organization': 'Microsoft'},
    ]
    actual = swdb(path).info(['--source', 'open'])
    assert actual == expected

def test_info_source_open_and_tag_returns_filtered():
    expected = [
        {'name': 'Emacs', 'organization': 'GNU'},
        {'name': 'Vim', 'organization': ''},
        {'name': 'Visual Studio Code', 'organization': 'Microsoft'},
    ]
    actual = swdb(path).info(['--source', 'open', '--tag', 'editor'])
    assert actual == expected

def test_info_source_closed_and_tag_returns_filtered():
    expected = [
        {'name': 'Sublime Text', 'organization': ''},
    ]
    actual = swdb(path).info(['--source', 'closed', '--tag', 'editor'])
    assert actual[0]['name'] == expected[0]['name']

def test_info_empty_organization_returns_all():
    expected = [
        {'name': 'Emacs', 'organization': 'GNU'},
        {'name': 'Go', 'organization': ''},
        {'name': 'Microsoft Edge', 'organization': 'Microsoft'},
        {'name': 'Microsoft Project', 'organization': 'Microsoft'},
        {'name': 'Microsoft SQL Server', 'organization': 'Microsoft'},
        {'name': 'MongoDB', 'organization': ''},
        {'name': 'MySQL', 'organization': ''},
        {'name': 'PostgreSQL', 'organization': ''},
        {'name': 'Python', 'organization': ''},
        {'name': 'Redis', 'organization': ''},
        {'name': 'Rust', 'organization': ''},
        {'name': 'Sublime Text', 'organization': ''},
        {'name': 'Vim', 'organization': ''},
        {'name': 'Visual Studio Code', 'organization': 'Microsoft'},
    ]
    actual = swdb(path).info(['--organization', ''])
    assert actual == expected

def test_info_valid_organization_returns_filtered():
    expected = [
        {'name': 'Emacs', 'organization': 'GNU'},
    ]
    actual = swdb(path).info(['--organization', 'gnu'])
    assert actual[0]['name'] == expected[0]['name']

def test_info_invalid_organization_returns_empty():
    expected = []
    actual = swdb(path).info(['--organization', 'xxx'])
    assert actual == expected

def test_info_valid_complex_filter_returns_filtered():
    expected = [
        {'name': 'Microsoft Project', 'organization': 'Microsoft'},
    ]
    actual = swdb(path).info(['--name', 'project',
                              '--tag', 'management',
                              '--source', 'closed',
                              '--organization', 'micro'])
    assert actual[0]['name'] == expected[0]['name']

def test_info_invalid_complex_filter_returns_empty():
    expected = []
    actual = swdb(path).info(['--name', 'xxx',
                              '--tag', 'data',
                              '--source', 'open',
                              '--organization', 'xxx'])
    assert actual == expected
