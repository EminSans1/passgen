#!/usr/bin/env python3
"""Password generator with entropy analysis."""

import argparse
import math
import secrets
import string
import sys

WORDS = [
    "apple", "brave", "chair", "dream", "eagle", "flame", "grape", "house",
    "island", "jungle", "knight", "lemon", "mouse", "noble", "ocean", "piano",
    "queen", "river", "storm", "tiger", "ultra", "vivid", "whale", "xenon",
    "yacht", "zebra", "angel", "beach", "creek", "delta", "ember", "frost",
    "ghost", "haven", "ivory", "jewel", "karma", "lunar", "marsh", "ninja",
    "opera", "pearl", "quilt", "robin", "solar", "thorn", "umbra", "vapor",
    "wheat", "xray", "yield", "atlas", "blaze", "cedar", "dune", "echo",
    "flint", "grove", "honey", "index", "jade", "knot", "lance", "maple",
    "nebula", "olive", "pixel", "quest", "ridge", "sage", "trace", "unity",
    "viper", "wren", "zinc", "arrow", "badge", "coral", "drift", "elite",
    "focus", "glow", "input", "joker", "kite", "lyric", "mango",
    "nexus", "orbit", "plume", "relay", "silk", "tango", "vibe", "wander",
    "zenith", "aura", "blade", "charm", "dusk"
]


def calculate_entropy(password: str, use_symbols: bool, use_digits: bool, use_upper: bool) -> float:
    charset_size = 0
    if use_symbols:
        charset_size += len(string.punctuation)
    if use_digits:
        charset_size += len(string.digits)
    if use_upper:
        charset_size += 26
    charset_size += 26  # always lowercase

    if charset_size == 0:
        charset_size = 26

    entropy = len(password) * math.log2(charset_size)
    return entropy


def generate_password(length: int, use_symbols: bool, use_digits: bool, use_upper: bool) -> str:
    charset = string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation

    return ''.join(secrets.choice(charset) for _ in range(length))


def generate_memorable(length: int) -> str:
    words = [secrets.choice(WORDS) for _ in range(length)]
    return '-'.join(words)


def main():
    parser = argparse.ArgumentParser(description='Password generator with entropy analysis')
    parser.add_argument('--length', type=int, default=16, help='Password length (default: 16)')
    parser.add_argument('--count', type=int, default=1, help='Number of passwords (default: 1)')
    parser.add_argument('--no-symbols', action='store_true', help='Exclude symbols')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-upper', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--memorable', action='store_true', help='Generate word-based password')
    args = parser.parse_args()

    if args.length < 1:
        print("Error: Length must be at least 1", file=sys.stderr)
        sys.exit(1)

    use_symbols = not args.no_symbols
    use_digits = not args.no_digits
    use_upper = not args.no_upper

    for _ in range(args.count):
        if args.memorable:
            password = generate_memorable(args.length)
            word_count = args.length
            charset_size = len(WORDS)
            entropy = word_count * math.log2(charset_size)
        else:
            password = generate_password(args.length, use_symbols, use_digits, use_upper)
            entropy = calculate_entropy(password, use_symbols, use_digits, use_upper)

        print(f"Password: {password}")
        print(f"Entropy:  {entropy:.2f} bits")
        if entropy < 50:
            print("⚠️  WARNING: Entropy below 50 bits — weak password!")
        print()


if __name__ == "__main__":
    main()
