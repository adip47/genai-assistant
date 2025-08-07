def get_pod_logs(namespace: str, pod_name: str):
    # Connect to Kubernetes API and fetch logs
    return f"Logs for pod '{pod_name}' in namespace '{namespace}'"

def get_cluster_status():
    return "Kubernetes cluster is healthy with 12 nodes."
