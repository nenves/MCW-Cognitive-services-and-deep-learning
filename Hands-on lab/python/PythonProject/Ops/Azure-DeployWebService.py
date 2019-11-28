# In[1]: Workspace creation
subscription_id = ""
resource_group = ""
workspace_name = ""
workspace_region = ""

working_directory = "C:\\Users\\veselne\\source\\repos\\nenves\\MCW-Cognitive-services-and-deep-learning\\Hands-on lab\\python\\PythonProject\\Ops"

import azureml.core
print("version is {0}".format(azureml.core.VERSION))


from azureml.core import Workspace

ws = Workspace.create(name=workspace_name, 
                      subscription_id=subscription_id, 
                      resource_group=resource_group, 
                      create_resource_group=False,
                      location=workspace_region)

print('Workspace configuration completed')

# In[2]: Web service and container deployment configuration
from azureml.core.conda_dependencies import CondaDependencies 
import os

os.chdir(working_directory)

myacienv = CondaDependencies.create(pip_packages=['gensim','nltk','numpy','inference_schema'])

with open("mydeployenv.yml","w") as f:
    f.write(myacienv.serialize_to_string())

# ## Deployment
from azureml.core.webservice import AciWebservice, Webservice

# Deployment configuration for the container web service
aci_config = AciWebservice.deploy_configuration(
    cpu_cores = 1,
    memory_gb = 1,
    tags = {"name":"Summarization"},
    description = "Summarizes text")

# Container image configuration
service_name = "summarization1"
runtime = "python"
driver_file = "summarizer_service1.py"
conda_file = "mydeployenv.yml"

from azureml.core.image import ContainerImage

image_config = ContainerImage.image_configuration(execution_script=driver_file, 
                                                  runtime = runtime, 
                                                  conda_file=conda_file)

# In[3]: Deploy service in container
deployedService = Webservice.deploy(workspace = ws,
                               name = service_name,
                               model_paths = [],
                               image_config = image_config,
                               deployment_config = aci_config)

deployedService.wait_for_deployment(show_output = True)

# In[4]: Test deployed service
uri = deployedService.scoring_uri


example_document = """On november 9th 1989, as the Berlin Wall tumbled, 
Hans-Joachim Binder was on night shift at the potash mine in Bischofferode, 
a village in the communist-ruled German Democratic Republic. 
Mr Binder, a maintenance worker who had toiled in the mine for 17 years, had no idea of the momentous events unfolding 240km (150 miles) to the east. 
The first sign something was up was when most of his colleagues disappeared to investigate what was happening at the border with West Germany, 
just ten minutes drive away. Only three returned to complete their shift. Less than a year later Germany was reunited, 
capping one of the most extraordinary stories in modern history. 
Not only had a communist dictatorship collapsed, releasing 16m people from the fear of the Stasi (secret police) and the stultification of censorship. 
Unlike any other country ever freed from tyranny, the entire population of East Germany was given citizenship of a big, 
rich democracy. As a grand, if ill-fated, gesture of welcome the West German chancellor, 
Helmut Kohl, converted some of their worthless savings into hard currency at the preposterously generous exchange rate of one Deutschmark to one Ostmark."""

import json
result = deployedService.run(input_data = json.dumps({"text" : example_document, "count" : "None", "ratio" : "0.5"}))
print(result)

