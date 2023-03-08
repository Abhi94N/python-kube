from kubernetes import client, config


config.load_kube_config()
apps_api = client.AppsV1Api()


# # Deployment and Pod labels and annotations
# labels = {
#     "component": "singleuser-server"
# }
# annotations = {
#     "CapacityProvisioned" "2vCPU 4GB"
# }
# # create notebook deployment
# deployment_metadata = client.V1ObjectMeta(name="jupyter-abhi", labels=labels, annotations=annotations)
# jupyter_notebook_deployment = client.V1Deployment(api_version = "apps/v1", kind="Deployment", metadata=deployment_metadata)

# #Manfifest Type
# # jupyter_notebook_deployment.api_version = "apps/v1"


# # # Pod template container description
# ports = [client.V1ContainerPort(container_port=8888, name="notebook_port", protocol="TCP")]
# jupyter_notebook_container = client.V1Container(name = "jupyter-abhi",image_pull_policy = "Always", image="jupyter/base-notebook:latest", ports=ports)



# # Create template spec and add it to spec template for deployment
# template = client.V1PodTemplateSpec()
# template.metadata = client.V1ObjectMeta(labels=labels, annotations=annotations)
# template.spec = client.V1PodSpec(containers=[jupyter_notebook_container])


# #add pod template spec to deployment template spec
# spec = client.V1DeploymentSpec(selector=labels, replicas=1, template=template)
# jupyter_notebook_deployment.spec = spec

deployment_body = {'api_version': 'apps/v1',
 'kind': 'Deployment',
 'metadata': {'annotations': {'CapacityProvisioned': '2vCPU 4GB'}},
              'labels': {'component': 'singleuser-server'},
              'name': 'jupyter-abhi',
 'spec': {
          'replicas': 1,
          'selector': {'component': 'singleuser-server'},
          'strategy': None,
          'template': {'metadata': {'annotations': {'CapacityProvisioned2vCPU '
                                                    '4GB'},
                                    'labels': {'component': 'singleuser-server'},
                                    'name': 'jupyter-abhi',
                                },
                       'spec': {
                                'containers': [{'args': None,
                                                'command': None,
                                                'env': None,
                                                'image': 'jupyter/base-notebook:latest',
                                                'image_pull_policy': 'Always',
                                                'name': 'jupyter-abhi',
                                                'ports': [{'container_port': 8888,
                                                           'host_ip': None,
                                                           'host_port': None,
                                                           'name': 'notebook_port',
                                                           'protocol': 'TCP'}],
                                                'security_context': None,
                                                'volume_devices': None,
                                                'volume_mounts': None,
                                                'working_dir': None}],
                                'restart_policy': 'Always',
                                'security_context': None,
                                'volumes': None}}},
}
print("deployment",deployment_body)


apps_api.create_namespaced_deployment(namespace="fargate", body=deployment_body)


#print("container",jupyter_notebook_container)


