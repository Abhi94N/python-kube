"""
Creates a deployment using AppsV1Api from file jupyter-deployment.yaml.
"""

from os import path

import yaml

from kubernetes import client, config
from kubernetes.config import ConfigException

def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    try:
        # try to load the cluster credentials
        # Configs can be set in Configuration class directly or using helper utility
        config.load_incluster_config()
    except ConfigException:
        # next method uses the KUBECONFIG env var by default
        config.load_kube_config()

    with open(path.join(path.dirname(__file__), "jupyter-abhi.yaml")) as f:
        dep = yaml.safe_load(f)
        
        k8s_apps = client.CoreV1Api()
        resp = k8s_apps.create_namespaced_pod(
            body=dep, namespace="fargate")
        print("Deployment created. status='%s'" % resp.metadata.name)


if __name__ == '__main__':
    main()