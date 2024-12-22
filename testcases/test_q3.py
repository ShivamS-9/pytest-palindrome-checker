import sys
sys.path.append("../Code")
import pytest
from palindrome import check_pali_day, pali_day_iterate

def test_check_pali_day_palindrome():
    assert check_pali_day(22, 2, 2022) == True


def test_check_pali_day_not_palindrome():
    assert check_pali_day(23, 5, 2021) == False


def test_check_pali_day_palindrome_5digyear():
    assert check_pali_day(12, 12, 72121) == True


def test_check_pali_day_palindrome_3digyear():
    assert check_pali_day(20, 12, 102) == True


def test_pali_day_iterate_invalid_year_neg():
    with pytest.raises(ValueError) as e:
        pali_day_iterate(-10)
    assert str(e.value) == "Year must be a positive integer greater than 0"


def test_pali_day_iterate_invalid_year_0():
    with pytest.raises(ValueError) as e:
        pali_day_iterate(0)
    assert str(e.value) == "Year must be a positive integer greater than 0"


def test_pali_day_iterate_valid_year_no_palindromes():
    pali_day_iterate(2000) == []


def test_pali_day_iterate_valid_year_1_palindrome():
    assert pali_day_iterate(2001) == ["10-02-2001"]


def test_pali_day_iterate_invalid_year_as_str():
    with pytest.raises(ValueError) as e:
        pali_day_iterate("yyy")
    assert str(e.value) == "Year must be a positive integer greater than 0"
