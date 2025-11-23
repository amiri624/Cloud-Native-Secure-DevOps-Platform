{{- define "devsecops-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "devsecops-app.fullname" -}}
{{ printf "%s" (include "devsecops-app.name" .) -}}
{{- end -}}
