# playwright-test-project

Test project for learning Playwright

## Run locally

Install the Python dependencies and Playwright browser once, then run pytest:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -q
```

## Run in GitHub Actions

The workflow in `.github/workflows/playwright-tests.yml` runs the suite on every push and pull request. It:

- sets up Python 3.13
- installs `requirements.txt`
- installs Playwright Chromium and required Linux OS packages
- runs `python -m pytest -q`
