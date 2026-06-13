# GitShield

GitShield is a Python-based DevSecOps security tool that detects hardcoded secrets and exposed credentials within source code repositories.

## Features

- Regex-based secret detection
- Entropy-based secret detection
- Repository scanning
- Severity classification
- JSON reporting
- HTML reporting

## Supported Detections

- AWS Access Keys
- GitHub Tokens
- OpenAI API Keys
- Password Assignments
- API Key Assignments
- High Entropy Strings

## Tech Stack

- Python
- Regex
- Jinja2
- GitPython

## Usage

```bash
python main.py
```

## Future Roadmap

- Git Pre-Commit Protection
- GitHub Actions Integration
- Finding Deduplication
- Enhanced HTML Dashboard