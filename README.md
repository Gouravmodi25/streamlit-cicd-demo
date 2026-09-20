# Streamlit CI/CD Demo

A simple Streamlit app used to demonstrate a complete CI/CD workflow:

Local → GitHub → Pull Request → CI (GitHub Actions) → Merge → CD → Render → Live app

## Run locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Project structure

- `streamlit_app.py`: the application
- `requirements.txt`: dependencies
- `.github/workflows/ci.yaml`: CI checks on pull requests
- `.github/workflows/deploy.yaml`: deployment after merge to main
