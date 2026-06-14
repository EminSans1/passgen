# passgen

CLI password generator with entropy analysis and memorable mode.

## Usage

```bash
python passgen.py [OPTIONS]
```

### Options

- `--length LENGTH` - Password length (default: 16)
- `--count COUNT` - Number of passwords (default: 1)
- `--no-symbols` - Exclude symbols from password
- `--no-digits` - Exclude digits from password
- `--no-upper` - Exclude uppercase letters
- `--memorable` - Generate word-based password

### Examples

```bash
# Generate default 16-char password
python passgen.py

# Generate 5 passwords of length 32
python passgen.py --length 32 --count 5

# Generate memorable password (word-based)
python passgen.py --memorable --length 5

# Generate password with only lowercase letters and digits
python passgen.py --no-symbols --no-upper
```

## Features

- Cryptographically secure using `secrets` module
- Entropy calculation in bits
- Warning for weak passwords (entropy < 50 bits)
- Memorable mode with 100 common words
- Configurable character sets

## Testing

```bash
pytest test_passgen.py -v
```
