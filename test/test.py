from swdb import swdb

PATH = 'db/test.yaml'

def test_tags():
    expected = [
        {'tag': 'Browser', 'count': 1},
        {'tag': 'Database', 'count': 5},
        {'tag': 'Diff Viewer', 'count': 1},
        {'tag': 'Programming Language', 'count': 3},
        {'tag': 'Project Management', 'count': 1},
        {'tag': 'Text Editor', 'count': 4},
    ]
    actual = swdb(PATH).tags()
    assert actual == expected

def test_list():
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
    actual = swdb(PATH).list()
    assert [item['name'] for item in actual] == expected

def test_list_empty_name():
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
    actual = swdb(PATH).list(['--name', ''])
    assert [item['name'] for item in actual] == expected

def test_list_valid_name():
    expected = [
        'Microsoft SQL Server',
        'MySQL',
        'PostgreSQL',
    ]
    actual = swdb(PATH).list(['--name', 'sql'])
    assert [item['name'] for item in actual] == expected

def test_list_invalid_name():
    expected = []
    actual = swdb(PATH).list(['--name', 'xxx'])
    assert actual == expected

def test_list_empty_tag():
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
    actual = swdb(PATH).list(['--tag', ''])
    assert [item['name'] for item in actual] == expected

def test_list_valid_tag():
    expected = [
        'Emacs',
        'Sublime Text',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(PATH).list(['--tag', 'text'])
    assert [item['name'] for item in actual] == expected

def test_list_invalid_tag():
    expected = []
    actual = swdb(PATH).list(['--tag', 'xxx'])
    assert actual == expected

def test_list_valid_name_and_tag():
    expected = [
        'Microsoft SQL Server',
        'MongoDB',
        'PostgreSQL',
    ]
    actual = swdb(PATH).list(['--name', 'o', '--tag', 'data'])
    assert [item['name'] for item in actual] == expected

def test_list_invalid_name_and_tag():
    expected = []
    actual = swdb(PATH).list(['--name', 'xxx', '--tag', 'data'])
    assert actual == expected

def test_list_source_open():
    expected = [
        'Emacs',
        'MongoDB',
        'MySQL',
        'PostgreSQL',
        'Redis',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(PATH).list(['--source', 'open'])
    assert [item['name'] for item in actual] == expected

def test_list_source_open_and_tag():
    expected = [
        'Emacs',
        'Vim',
        'Visual Studio Code',
    ]
    actual = swdb(PATH).list(['--source', 'open', '--tag', 'editor'])
    assert [item['name'] for item in actual] == expected

def test_list_source_closed_and_tag():
    expected = [
        'Sublime Text',
    ]
    actual = swdb(PATH).list(['--source', 'closed', '--tag', 'editor'])
    assert actual[0]['name'] == expected[0]

def test_list_empty_organization():
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
    actual = swdb(PATH).list(['--organization', ''])
    assert [item['name'] for item in actual] == expected

def test_list_valid_organization():
    expected = [
        'Emacs',
    ]
    actual = swdb(PATH).list(['--organization', 'gnu'])
    assert actual[0]['name'] == expected[0]

def test_list_invalid_organization():
    expected = []
    actual = swdb(PATH).list(['--organization', 'xxx'])
    assert actual == expected

def test_list_valid_complex_filter():
    expected = [
        'Microsoft Project',
    ]
    actual = swdb(PATH).list(['--name', 'project',
                              '--tag', 'management',
                              '--source', 'closed',
                              '--organization', 'micro'])
    assert actual[0]['name'] == expected[0]

def test_list_invalid_complex_filter():
    expected = []
    actual = swdb(PATH).list(['--name', 'xxx',
                              '--tag', 'data',
                              '--source', 'open',
                              '--organization', 'xxx'])
    assert actual == expected

def test_info_empty_name():
    expected = None
    actual = swdb(PATH).info([''])
    assert actual == expected

def test_info_invalid_name():
    expected = None
    actual = swdb(PATH).info(['xxx'])
    assert actual == expected

def test_info_partial_name():
    expected = None
    actual = swdb(PATH).info(['emac'])
    assert actual == expected

def test_info_valid_name():
    expected = {
        'name': 'Emacs',
        'organization': 'GNU',
        'source': 'open',
    }
    actual = swdb(PATH).info(['emacs'])
    assert all(actual[key] == expected[key] for key in expected)

def test_cross_empty_name():
    expected = []
    actual = swdb(PATH).cross([])
    assert actual == expected

def test_cross_single_name():
    expected = [
        {'key': 'organization', 'Vim': ''},
        {'key': 'source', 'Vim': 'open'},
    ]
    actual = swdb(PATH).cross(['--name', 'vim'])
    assert actual == expected

def test_cross_valid_names():
    expected = [
        {'key': 'organization', 'Emacs': 'GNU', 'Sublime Text': '', 'Vim': ''},
        {'key': 'source', 'Emacs': 'open', 'Sublime Text': 'closed', 'Vim': 'open'},
    ]
    actual = swdb(PATH).cross(['--name', 'vim', 'sublime text', 'emacs'])
    assert actual == expected

def test_cross_invalid_names():
    expected = [
        {'key': 'organization', 'Vim': '', 'Emacs': 'GNU'},
        {'key': 'source', 'Vim': 'open', 'Emacs': 'open'},
    ]
    actual = swdb(PATH).cross(['--name', 'vim', 'xxx', 'emacs'])
    assert actual == expected
