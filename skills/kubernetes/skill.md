# Kubernetes

You operate Kubernetes workloads declaratively: small focused resources, explicit limits, and verification after every change.

## Manifests

- Keep resources small and focused: one Deployment, one Service, one ConfigMap per concern.
- Use `kubectl apply -f` with versioned manifest files; never use `kubectl run` or `kubectl create` for production objects.
- Pin `apiVersion` for your cluster's Kubernetes version; check with `kubectl version`.
- Label everything for selection and ownership: `app`, `tier`, `environment`, `version`.
- Use a single source of truth (Helm, Kustomize) for environments instead of copy-pasted YAML.

## Deployments and rollouts

- Set `replicas` explicitly, never 0 by accident, and use `replicas` for capacity, not HA alone.
- Use `strategy` with `maxUnavailable: 0` and `maxSurge` for zero-downtime rolling updates.
- Define `readinessProbe` and `livenessProbe` with realistic paths, periods, and failure thresholds.
- Separate readiness from liveness: readiness gates traffic, liveness restarts.
- Pin image tags to the build (`:sha-<hash>`); avoid mutable `latest` tags.
- Prefer rolling updates over delete-recreate; verify rollout with `kubectl rollout status`.

## Resources and scheduling

- Always set `resources.requests` and `resources.limits` for CPU and memory.
- Keep limits close to requests to avoid throttling surprises; document headroom.
- Set `securityContext` (non-root, read-only root filesystem) and use `runAsNonRoot: true`.
- Use `nodeSelector`/`affinity` only when there is a real constraint; tolerations with `NoSchedule` deliberately.
- Prefer `HorizontalPodAutoscaler` over static scaling when load is variable; give it correct metrics.

## Configuration and secrets

- Put environment-specific values in ConfigMaps; never hard-code them in the image.
- Store secrets as Kubernetes Secrets, mounted or injected, never in plain YAML or env vars in manifests.
- Prefer immutable ConfigMaps/Secrets for rollout-triggered restarts; version them.
- Reference config by name; check `kubectl get configmap` before deploying new manifests.

## Networking

- Use Services with explicit `selector` and `port`/`targetPort`; verify endpoints with `kubectl get endpoints`.
- Prefer an Ingress for HTTP routing; terminate TLS there, not in every pod.
- Use NetworkPolicies to restrict traffic by default; never rely on default-allow.
- Name ports in the manifest so YAML reads clearly: `ports: [{ name: http, containerPort: 8080 }]`.

## Observability and troubleshooting

- Debug order: `kubectl get events`, `describe pod`, `logs -f --previous`, then `exec` into the pod.
- Check status everywhere: `kubectl get pods,svc,ingress -A | grep -v Running`.
- Read logs with `--previous` after a crash to see the pre-restart output.
- Use `kubectl port-forward` for local debugging only; never expose services to the internet casually.
- Prefer `kubectl drain` and cordon over deleting nodes or pods manually.
- Collect metrics and logs from the cluster (Prometheus, Loki or equivalents); do not SSH into nodes as routine.
- Make every change one object at a time and confirm with `kubectl diff` before applying.
