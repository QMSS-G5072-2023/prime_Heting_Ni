from prime_hn2401 import prime_hn2401
import pytest
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
@pytest.mark.parametrize("number, expected_result", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (1, False),
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
])
def test_is_prime_param(number, expected_result):
    assert is_prime(number) == expected_result
