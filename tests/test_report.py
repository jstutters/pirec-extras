from plumbium_extras import report


def test_path_walk():
    expected = [
        ('foo', 0),
        ('bar', None),
        ('bob', 1)
    ]
    assert list(report.walk_path('foo[0].bar.bob[1]')) == expected


def test_get_from_dict_by_path():
    expected = 5.0
    test_case = {
        'foo': [
            {'bar': 1},
            {'bar': 2},
            {'bar': 5}
        ],
        'bob': 'wibble'
    }
    assert report.get_from_dict_by_path(test_case, 'foo[2].bar') == expected
