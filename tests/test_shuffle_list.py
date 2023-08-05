from playground import shuffle_list


def test_shuffle_list() -> None:
    shuffled_list = shuffle_list.shuffle_list([0, 1, 2, 3, 4])
    for i in shuffled_list:
        actual = i in [0, 1, 2, 3, 4]
        assert actual is True
