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
        'Emacs',
        'Go',
        'Microsoft Edge',
        'Microsoft Project',
        'Microsoft SQL Server',
        'MongoDB',
        'MySQL',
        'PostgreSQL',
        'Python',
        'Redis',
        'Rust',
        'Sublime Text',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(path).info()
    assert [item['name'] for item in actual] == expected

def test_info_empty_name_returns_all():
    expected = [
        'Emacs',
        'Go',
        'Microsoft Edge',
        'Microsoft Project',
        'Microsoft SQL Server',
        'MongoDB',
        'MySQL',
        'PostgreSQL',
        'Python',
        'Redis',
        'Rust',
        'Sublime Text',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(path).info(['--name', ''])
    assert [item['name'] for item in actual] == expected

def test_info_valid_name_returns_filtered():
    expected = [
        'Microsoft SQL Server',
        'MySQL',
        'PostgreSQL',
    ]
    actual = swdb(path).info(['--name', 'sql'])
    assert [item['name'] for item in actual] == expected

def test_info_invalid_name_returns_empty():
    expected = []
    actual = swdb(path).info(['--name', 'xxx'])
    assert actual == expected

def test_info_empty_tag_returns_all():
    expected = [
        'Emacs',
        'Go',
        'Microsoft Edge',
        'Microsoft Project',
        'Microsoft SQL Server',
        'MongoDB',
        'MySQL',
        'PostgreSQL',
        'Python',
        'Redis',
        'Rust',
        'Sublime Text',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(path).info(['--tag', ''])
    assert [item['name'] for item in actual] == expected

def test_info_valid_tag_returns_filtered():
    expected = [
        'Emacs',
        'Sublime Text',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(path).info(['--tag', 'text'])
    assert [item['name'] for item in actual] == expected

def test_info_invalid_tag_returns_empty():
    expected = []
    actual = swdb(path).info(['--tag', 'xxx'])
    assert actual == expected

def test_info_valid_name_and_tag_returns_filtered():
    expected = [
        'Microsoft SQL Server',
        'MongoDB',
        'PostgreSQL',
    ]
    actual = swdb(path).info(['--name', 'o', '--tag', 'data'])
    assert [item['name'] for item in actual] == expected

def test_info_invalid_name_and_tag_returns_empty():
    expected = []
    actual = swdb(path).info(['--name', 'xxx', '--tag', 'data'])
    assert actual == expected

def test_info_source_open_returns_filtered():
    expected = [
        'Emacs',
        'MongoDB',
        'MySQL',
        'PostgreSQL',
        'Redis',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(path).info(['--source', 'open'])
    assert [item['name'] for item in actual] == expected

def test_info_source_open_and_tag_returns_filtered():
    expected = [
        'Emacs',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(path).info(['--source', 'open', '--tag', 'editor'])
    assert [item['name'] for item in actual] == expected

def test_info_source_closed_and_tag_returns_filtered():
    expected = [
        'Sublime Text',
    ]
    actual = swdb(path).info(['--source', 'closed', '--tag', 'editor'])
    assert actual[0]['name'] == expected[0]

def test_info_empty_organization_returns_all():
    expected = [
        'Emacs',
        'Go',
        'Microsoft Edge',
        'Microsoft Project',
        'Microsoft SQL Server',
        'MongoDB',
        'MySQL',
        'PostgreSQL',
        'Python',
        'Redis',
        'Rust',
        'Sublime Text',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(path).info(['--organization', ''])
    assert [item['name'] for item in actual] == expected

def test_info_valid_organization_returns_filtered():
    expected = [
        'Emacs',
    ]
    actual = swdb(path).info(['--organization', 'gnu'])
    assert actual[0]['name'] == expected[0]

def test_info_invalid_organization_returns_empty():
    expected = []
    actual = swdb(path).info(['--organization', 'xxx'])
    assert actual == expected

def test_info_valid_complex_filter_returns_filtered():
    expected = [
        'Microsoft Project',
    ]
    actual = swdb(path).info(['--name', 'project',
                              '--tag', 'management',
                              '--source', 'closed',
                              '--organization', 'micro'])
    assert actual[0]['name'] == expected[0]

def test_info_invalid_complex_filter_returns_empty():
    expected = []
    actual = swdb(path).info(['--name', 'xxx',
                              '--tag', 'data',
                              '--source', 'open',
                              '--organization', 'xxx'])
    assert actual == expected

def test_cross_single_name():
    expected = [
        {'key': 'organization', 'Vim': ''},
        {'key': 'source', 'Vim': 'open'},
    ]
    actual = swdb(path).cross(['vim'])
    assert actual == expected

def test_cross_valid_names():
    expected = [
        {'key': 'organization', 'Vim': '', 'Sublime Text': '', 'Emacs': 'GNU'},
        {'key': 'source', 'Vim': 'open', 'Sublime Text': 'closed', 'Emacs': 'open'},
    ]
    actual = swdb(path).cross(['vim', 'sublime text', 'emacs'])
    assert actual == expected

def test_cross_invalid_names():
    expected = [
        {'key': 'organization', 'Vim': '', 'Emacs': 'GNU'},
        {'key': 'source', 'Vim': 'open', 'Emacs': 'open'},
    ]
    actual = swdb(path).cross(['vim', 'xxx', 'emacs'])
    assert actual == expected
