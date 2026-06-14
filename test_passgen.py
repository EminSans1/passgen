"""Tests for passgen."""

import math
import secrets
import string
from unittest.mock import patch

import pytest

from passgen import (
    WORDS,
    calculate_entropy,
    generate_memorable,
    generate_password,
)


def test_default_length():
    password = generate_password(16, True, True, True)
    assert len(password) == 16


def test_custom_length():
    password = generate_password(32, True, True, True)
    assert len(password) == 32


def test_minimum_length_enforcement():
    password = generate_password(1, True, True, True)
    assert len(password) == 1


def test_no_symbols():
    password = generate_password(100, False, True, True)
    assert not any(c in string.punctuation for c in password)


def test_no_digits():
    password = generate_password(100, True, False, True)
    assert not any(c in string.digits for c in password)


def test_no_upper():
    password = generate_password(100, True, True, False)
    assert not any(c in string.ascii_uppercase for c in password)


def test_only_lowercase():
    password = generate_password(100, False, False, False)
    assert all(c in string.ascii_lowercase for c in password)


def test_all_features_enabled():
    password = generate_password(100, True, True, True)
    has_symbol = any(c in string.punctuation for c in password)
    has_digit = any(c in string.digits for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    assert has_symbol and has_digit and has_upper and has_lower


def test_entropy_calculation_full_charset():
    password = "a" * 16
    entropy = calculate_entropy(password, True, True, True)
    expected = 16 * math.log2(
        len(string.ascii_lowercase) + len(string.ascii_uppercase)
        + len(string.digits) + len(string.punctuation)
    )
    assert abs(entropy - expected) < 0.01


def test_entropy_calculation_no_symbols():
    password = "a" * 16
    entropy = calculate_entropy(password, False, True, True)
    expected = 16 * math.log2(
        len(string.ascii_lowercase) + len(string.ascii_uppercase) + len(string.digits)
    )
    assert abs(entropy - expected) < 0.01


def test_entropy_calculation_no_digits():
    password = "a" * 16
    entropy = calculate_entropy(password, True, False, True)
    expected = 16 * math.log2(
        len(string.ascii_lowercase) + len(string.ascii_uppercase) + len(string.punctuation)
    )
    assert abs(entropy - expected) < 0.01


def test_entropy_calculation_no_upper():
    password = "a" * 16
    entropy = calculate_entropy(password, True, True, False)
    expected = 16 * math.log2(
        len(string.ascii_lowercase) + len(string.digits) + len(string.punctuation)
    )
    assert abs(entropy - expected) < 0.01


def test_entropy_calculation_only_lowercase():
    password = "a" * 16
    entropy = calculate_entropy(password, False, False, False)
    expected = 16 * math.log2(len(string.ascii_lowercase))
    assert abs(entropy - expected) < 0.01


def test_entropy_increases_with_length():
    short = generate_password(8, True, True, True)
    long = generate_password(32, True, True, True)
    entropy_short = calculate_entropy(short, True, True, True)
    entropy_long = calculate_entropy(long, True, True, True)
    assert entropy_long > entropy_short


def test_uses_secrets_not_random():
    with patch('secrets.choice') as mock_choice:
        mock_choice.return_value = 'a'
        password = generate_password(10, True, True, True)
        assert password == 'a' * 10
        assert mock_choice.called


def test_memorable_length():
    password = generate_memorable(5)
    words = password.split('-')
    assert len(words) == 5


def test_memorable_uses_valid_words():
    password = generate_memorable(10)
    words = password.split('-')
    for word in words:
        assert word in WORDS


def test_wordlist_size():
    assert len(WORDS) == 100


def test_memorable_entropy():
    word_count = 10
    password = generate_memorable(word_count)
    entropy = word_count * math.log2(len(WORDS))
    assert entropy > 50


def test_entropy_below_50_warning():
    password = "abc"
    entropy = calculate_entropy(password, False, False, False)
    assert entropy < 50
