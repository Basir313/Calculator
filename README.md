# 🧮 Simple Python Calculator

A beginner-friendly Python project used to **practice CI/CD** with GitHub Actions.

## 📁 Project Structure

```
Calculator/
├── calculator.py         # Core calculator functions
├── test_calculator.py    # Unit tests (pytest)
└── .github/
    └── workflows/
        └── ci.yml        # CI/CD pipeline
```

## ⚙️ Features

| Function   | Description              |
|------------|--------------------------|
| `add`      | Addition                 |
| `subtract` | Subtraction              |
| `multiply` | Multiplication           |
| `divide`   | Division (zero-safe)     |

## 🚀 Run Locally

```bash
python calculator.py
```

## 🧪 Run Tests

```bash
pip install pytest pytest-cov
pytest test_calculator.py -v --cov=calculator
```

## 🔄 CI/CD Pipeline

Powered by **GitHub Actions** — triggered on every push or pull request to `main`:

1. **CI — Test job**: installs `pytest`, runs all tests with coverage report.
2. **CD — Deploy job**: runs only after tests pass; executes the application (simulated deploy).

> The deploy step simulates a real deployment. In a real project you'd push to a server, Docker registry, or cloud provider here.
