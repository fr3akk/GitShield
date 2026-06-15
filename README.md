# GitShield

A Python-based DevSecOps security tool that detects hardcoded secrets and exposed credentials before they are committed to a Git repository.

GitShield combines regex-based secret detection, entropy analysis, automated reporting, and Git pre-commit hook integration to prevent accidental credential leaks during development.

---

## Features

* Regex-based secret detection
* Entropy-based secret detection
* Severity classification (Critical / High / Medium)
* JSON report generation
* HTML security report generation
* Git pre-commit hook integration
* Automatic commit blocking
* Staged file scanning using Git index
* Configurable detection rules
* Directory and file exclusion support

---

## Security Impact

GitShield helps prevent exposure of:

* AWS Access Keys
* GitHub Tokens
* OpenAI API Keys
* Hardcoded Passwords
* API Keys
* High-Entropy Secrets

By detecting these secrets before they are committed, GitShield reduces the risk of credential leakage and repository compromise.

---

## Architecture

```text
git add file.py
        ↓
Git Staging Area
        ↓
GitShield Pre-Commit Hook
        ↓
Retrieve Staged Files
        ↓
Regex Detection
        +
Entropy Detection
        ↓
Findings Generated
        ↓
Allow Commit / Block Commit
```

---

## Commit Protection Workflow

GitShield integrates directly with Git pre-commit hooks and scans only staged files before a commit is created.

When secrets are detected:

```text
[!] GITSHIELD BLOCKED COMMIT

Detected 2 potential secrets:

[Critical] GitHub Token -> secret.py
[Medium] High Entropy String -> secret.py
```

The commit is automatically blocked until the detected secrets are removed.

When no secrets are found:

```text
[+] GitShield Scan Passed
```

The commit proceeds normally.

---

## Staged File Scanning

GitShield scans only files currently staged for commit.

Workflow:

```text
git add secret.py
        ↓
git diff --cached --name-only
        ↓
GitShield
        ↓
Scan Staged Files Only
        ↓
Allow / Block Commit
```

Benefits:

* Faster scans
* Reduced false positives
* Better developer experience
* Real-world DevSecOps workflow integration

---

## Supported Secret Types

| Secret Type          | Severity |
| -------------------- | -------- |
| AWS Access Key       | Critical |
| GitHub Token         | Critical |
| OpenAI API Key       | Critical |
| Password Assignment  | High     |
| API Key Assignment   | High     |
| High Entropy Strings | Medium   |

---

## Detection Techniques

### Regex-Based Detection

GitShield uses predefined patterns to identify known credential formats:

* AWS Access Keys
* GitHub Tokens
* OpenAI API Keys
* Password Assignments
* API Key Assignments

Example:

```python
aws_key = "AWS_ACCESS_KEY"
```

### Entropy-Based Detection

GitShield uses Shannon Entropy analysis to identify randomly generated secrets that may not match predefined patterns.

Example:

```python
token = "HIGH_ENTROPY_SECRET"
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/fr3akk/GitShield.git
cd GitShield
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```powershell
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Run Repository Scan

```bash
python main.py
```

### Run Pre-Commit Protection

```bash
git commit -m "your commit message"
```

GitShield will automatically scan staged files and block commits containing exposed secrets.

---

## Reporting

### JSON Report

Machine-readable findings for automation and integration.

### HTML Report

Interactive dashboard containing:

* Severity statistics
* Findings table
* Security summary

---

## Excluded Directories

GitShield automatically ignores:

```text
.git
venv
__pycache__
node_modules
build
dist
output
examples
```

This improves performance and reduces false positives.

---

## Technologies Used

* Python
* Regex
* Shannon Entropy Analysis
* Jinja2
* GitPython
* Git Hooks

---

## Releases

* v1.0 – Core Secret Scanner
* v1.1 – Commit Protection
* v2.0 – Staged File Scanning

---

## Future Roadmap

### v3.0

* GitHub Actions Integration
* CI/CD Secret Scanning
* Enhanced HTML Dashboard
* Finding Deduplication

### v4.0

* SARIF Export Support
* Custom Detection Rules
* Enterprise Policy Enforcement
* Multi-Repository Scanning

---

## Author

Ayush (fr3akk)

GitHub: https://github.com/fr3akk
