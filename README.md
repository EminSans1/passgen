# PassGen

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

CLI password generator with entropy analysis and memorable word-based mode.

## Features

- Cryptographically secure generation using the `secrets` module
- Real-time entropy calculation in bits
- Weak password warning (entropy < 50 bits)
- Memorable mode with 100 common words
- Configurable character sets (uppercase, digits, symbols)
- Batch generation — create multiple passwords at once

## Installation

```bash
git clone https://github.com/EminSans1/passgen.git
cd passgen
```

No `pip install` needed — the tool uses only built-in modules.

## Usage

```bash
python passgen.py [OPTIONS]
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `--length N` | `16` | Password length |
| `--count N` | `1` | Number of passwords to generate |
| `--no-symbols` | — | Exclude symbols |
| `--no-digits` | — | Exclude digits |
| `--no-upper` | — | Exclude uppercase letters |
| `--memorable` | — | Generate word-based password |

### Examples

```bash
# Generate a default 16-character password
python passgen.py

# Generate 5 passwords of length 32
python passgen.py --length 32 --count 5

# Generate a memorable passphrase
python passgen.py --memorable --length 5

# Lowercase + digits only
python passgen.py --no-symbols --no-upper
```

## Sample Output

```
Password: k8#mP2$vNx@9qLw
Entropy:  95.32 bits

Password: j4R!bG7@nW3eYt
Entropy:  91.65 bits

Password: ocean-storm-flame-tiger-ember
Entropy:  46.50 bits
⚠️  WARNING: Entropy below 50 bits — weak password!
```

## How Entropy Works

Entropy measures password strength in bits. Higher is better:

| Entropy | Strength |
|---------|----------|
| < 28 bits | Very weak |
| 28–35 bits | Weak |
| 36–59 bits | Reasonable |
| 60–127 bits | Strong |
| ≥ 128 bits | Very strong |

## Project Structure

```
passgen/
├── passgen.py           # Main application
├── test_passgen.py      # Unit tests
├── README.md
└── .gitignore
```

## Testing

```bash
pytest test_passgen.py -v
```

## Contributing

1. Fork the repository
2. Create your branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License — see [LICENSE](LICENSE) for details.
