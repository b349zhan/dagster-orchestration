The following instructions are done in [Openshift Developer Sandbox](https://console.redhat.com/openshift/sandbox).
---
# Creating Environment

```bash
python -m venv ~/.virtualenvs/dagster-env
source ~/.virtualenvs/dagster-env/bin/activate
pip install -r requirements.txt
poetry install
```

# Launching Dagster Locally
```bash
dagster dev
## Assuming port 3000 is not in use, openshift developer sandbox will redirect to https://b349zhan-dagster-orchestration-code-redirect-3.apps.sandbox-m3.1530.p1.openshiftapps.com/runs
```