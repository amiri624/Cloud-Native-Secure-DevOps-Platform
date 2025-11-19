
# Cloud-Native-Secure-DevOps-Platform

```bas
cloud-native-secure-devops-platform/
│
├── src/
│   └── app/
│       ├── main.py
│       ├── requirements.txt
│       ├── Dockerfile
│       ├── tests/
│       │   └── test_health.py
│       └── Makefile
│
├── k8s/
│   ├── base/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── configmap.yaml
│   │   ├── hpa.yaml
│   │   ├── pdb.yaml
│   │   ├── networkpolicy.yaml
│   │   ├── secret.yaml
│   │   └── serviceaccount.yaml
│   │
│   ├── istio/
│   │   ├── gateway.yaml
│   │   ├── virtualservice.yaml
│   │   └── destinationrule.yaml
│   │
│   ├── security/
│   │   ├── rbac.yaml
│   │   ├── vault-secretproviderclass.yaml
│   │   └── policies/
│   │       ├── no-privileged.yaml
│   │       ├── require-labels.yaml
│   │       ├── block-latest-image.yaml
│   │       └── enforce-https.yaml
│   │
│   └── monitoring/
│       ├── prometheus.yaml
│       ├── loki.yaml
│       ├── tempo.yaml
│       ├── alerts.yaml
│       └── grafana-dashboards/
│           ├── app-metrics.json
│           └── system-overview.json
│
├── gitops/
│   ├── root-app.yaml
│   ├── app-of-apps.yaml
│   └── apps/
│       ├── app.yaml
│       ├── monitoring.yaml
│       ├── istio.yaml
│       └── security.yaml
│
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
│
├── infrastructure/
│   ├── k3d/
│   │   ├── cluster.yaml
│   │   └── registry.yaml
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── eks/
│           ├── cluster.tf
│           ├── vpc.tf
│           └── nodegroup.tf
│
├── scripts/
│   ├── bootstrap.sh
│   ├── deploy.sh
│   └── destroy.sh
│
├── docs/
│   ├── architecture.svg
│   ├── threat-model.md
│   └── api-spec.yaml
│
└── README.md

```
