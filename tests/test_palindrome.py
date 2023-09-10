from playground import palindrome


def test_palindrome() -> None:
    actual = palindrome.palindrome("いろしろい")
    assert actual is True


def test_palindrome_false() -> None:
    actual = palindrome.palindrome("あいうえお")
    assert actual is False


def test_palindrome_not_str() -> None:
    actual = palindrome.palindrome(100)  # type: ignore
    assert actual is False
