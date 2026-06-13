# GitShield

A Python-based DevSecOps security tool that detects hardcoded secrets and exposed credentials before they are committed to a Git repository.

GitShield combines regex-based detection, entropy analysis, reporting capabilities, and Git pre-commit hook integration to help developers prevent accidental credential leaks.

---

## Features

* Regex-based secret detection
* Entropy-based secret detection
* Recursive repository scanning
* Severity classification (Critical / High / Medium)
* JSON report generation
* HTML security report generation
* Git pre-commit hook integration
* Automatic commit blocking on secret detection
* Configurable detection rules
* Directory and file exclusion support

---

## Security Impact

GitShield helps identify and prevent exposure of:

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
Git Commit
    ↓
Git Pre-Commit Hook
    ↓
GitShield Scanner
    ↓
Regex Detection
    +
Entropy Detection
    ↓
Findings
    ↓
Commit Allowed / Blocked
```

---

## Project Structure

```text
GitShield
│
├── hooks
│   └── pre_commit.py
│
├── scanner
│   ├── entropy_detector.py
│   ├── file_scanner.py
│   ├── gitshield_scanner.py
│   ├── regex_detector.py
│   ├── repository_scanner.py
│   └── rule_loader.py
│
├── reports
│   ├── dashboard.py
│   ├── html_report.py
│   ├── json_report.py
│   └── report_template.html
│
├── rules
│   └── patterns.json
│
├── examples
│   ├── config.py
│   ├── databse.py
│   ├── random_secret.py
│   └── src
│       └── auth.py
│
├── output
│
├── README.md
├── requirements.txt
└── main.py
```

---

## Detection Techniques

### Regex-Based Detection

GitShield uses predefined patterns to detect known secret formats such as:

* AWS Access Keys
* GitHub Tokens
* OpenAI API Keys
* Password Assignments
* API Key Assignments

Example:

```python
aws_key = "AKIA1234567890123456"
```

---

### Entropy-Based Detection

GitShield identifies randomly generated strings with high entropy that may represent:

* Tokens
* API Keys
* Session Secrets
* Authentication Credentials

Example:

```python
token = "A7kP9mX2QvL8sRt4ZnY6"
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

### Activate Virtual Environment

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

GitShield will:

* Scan the target repository
* Detect secrets
* Generate findings
* Create JSON and HTML reports

---

## Example Output

```text
===== GITSHIELD SUMMARY =====

Critical: 2
High: 4
Medium: 3

Total Findings: 9
```

---

## Git Pre-Commit Protection

GitShield can be integrated with Git pre-commit hooks.

When secrets are detected:

```text
[!] GITSHIELD BLOCKED COMMIT

Detected 3 potential secrets:

[Critical] AWS Access Key -> config.py
[High] Password Assignment -> database.py
```

The commit is automatically blocked.

When no secrets are found:

```text
[+] GitShield Scan Passed
```

The commit proceeds normally.

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

## Reporting

### JSON Report

Machine-readable findings:

```json
{
  "type": "AWS Access Key",
  "severity": "Critical",
  "file": "config.py"
}
```

### HTML Report

Human-readable dashboard containing:

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

This reduces false positives and improves scanning performance.

---

## Technologies Used

* Python
* Regex
* Shannon Entropy Analysis
* Jinja2
* Git Hooks
* GitPython

---

## Future Roadmap

### v2.0

* Scan only staged Git files
* Finding deduplication
* Improved entropy detection
* Enhanced HTML dashboard

### v3.0

* GitHub Actions integration
* SARIF export support
* CI/CD security scanning
* Custom rule creation

---

## Learning Outcomes

This project demonstrates:

* Secure Coding Practices
* DevSecOps Fundamentals
* Git Hook Development
* Secret Detection Techniques
* Security Automation
* Python Development
* Vulnerability Prevention

---

## Author

Ayush (fr3akk)

GitHub: https://github.com/fr3akk
