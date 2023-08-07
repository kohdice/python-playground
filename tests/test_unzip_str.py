import pytest

from playground import unzip_str


def test_unzip_str() -> None:
    actual = unzip_str.unzip_str("a1b2c3")

    assert actual == "abbccc"


def test_unzip_str_none() -> None:
    with pytest.raises(TypeError):
        unzip_str.unzip_str("")


def test_unzip_str_int() -> None:
    with pytest.raises(TypeError):
        unzip_str.unzip_str(12345)  # type: ignore
