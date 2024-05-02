The following instructions are done in [Openshift Developer Sandbox](https://console.redhat.com/openshift/sandbox).
---
# Creating Environment

```bash
python -m venv ~/.virtualenvs/dagster-env
source ~/.virtualenvs/dagster-env/bin/activate
pip install poetry
poetry install
```

# Launching Dagster Locally
```bash
dagster dev
## Assuming port 3000 is not in use, openshift developer sandbox will redirect to:
## https://b349zhan-dagster-orchestration-code-redirect-3.apps.sandbox-m3.1530.p1.openshiftapps.com/runs
```

# Build Image on OCP
```bash
## clean up existing build config
oc delete bc dagster-build-config
oc process -f build-support/build-template.yaml | oc apply -f - 
oc start-build dagster-build-config --from-dir .
```


# Deploy/Teardown Postgres
```bash
oc apply -f build-support/deploy-postgres.yaml 
oc delete all,pvc -l app=postgres
```

# Deploy/Teardown Dagster
```bash
oc apply -f build-support/deploy-dagster.yaml 
oc delete all,pvc,configmap -l app=dagster
```

# Deploy/Teardown Dagster Workspace
```bash
oc apply -f build-support/deploy-workspace.yaml 
oc delete all -l app=workspace-a
```