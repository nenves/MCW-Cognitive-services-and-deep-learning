#!/usr/bin/env python
# coding: utf-8

# # Azure Machine Learning Setup
# To begin, you will need to provide the following information about your Azure Subscription.
# 
# **If you are using your own Azure subscription, please provide names for subscription_id, resource_group, workspace_name and workspace_region to use.** Note that the workspace needs to be of type [Machine Learning Workspace](https://docs.microsoft.com/en-us/azure/machine-learning/service/setup-create-workspace).
# 
# **If an enviorment is provided to you be sure to replace XXXXX in the values below with your unique identifier.**
# 
# In the following cell, be sure to set the values for `subscription_id`, `resource_group`, `workspace_name` and `workspace_region` as directed by the comments (*these values can be acquired from the Azure Portal*).
# 
# To get these values, do the following:
# 1. Navigate to the Azure Portal and login with the credentials provided.
# 2. From the left hand menu, under Favorites, select `Resource Groups`.
# 3. In the list, select the resource group with the name similar to `XXXXX`.
# 4. From the Overview tab, capture the desired values.
# 
# Execute the following cell by selecting the `&gt;|Run` button in the command bar above.

# In[2]:


#Provide the Subscription ID of your existing Azure subscription
subscription_id = "<your-azure-subscription-id>"

#Provide a name for the Resource Group that will contain Azure ML related services 
resource_group = "<your-subscription-group-name>"

# Provide the name and region for the Azure Machine Learning Workspace that will be created
workspace_name = ""
workspace_region = "" # eastus2, eastus, westcentralus, southeastasia, australiaeast, westeurope


# ## Create and connect to an Azure Machine Learning Workspace
# 
# The Azure Machine Learning Python SDK is required for leveraging the experimentation, model management and model deployment capabilities of Azure Machine Learning services. Run the following cell to create a new Azure Machine Learning **Workspace** and save the configuration to disk. The configuration file named `config.json` is saved in a folder named `.azureml`. 
# 
# **Important Note**: You will be prompted to login in the text that is output below the cell. Be sure to navigate to the URL displayed and enter the code that is provided. Once you have entered the code, return to this notebook and wait for the output to read `Workspace configuration succeeded`.

# In[3]:

import azureml.core
print('azureml.core.VERSION: ', azureml.core.VERSION)

# import the Workspace class and check the azureml SDK version
from azureml.core import Workspace

ws = Workspace.create(
    name = workspace_name,
    subscription_id = subscription_id,
    resource_group = resource_group, 
    location = workspace_region, 
    exist_ok = True)

#ws.write_config()
print('Workspace configuration succeeded')


# Take a look at the contents of the generated configuration file by running the following cell:

# In[5]:

#get_ipython().system(u'cat .azureml/config.json')


# # Deploy model to Azure Container Instance (ACI)
# 
# In this section, you will deploy a web service that uses Gensim as shown in `01 Summarize` to summarize text. The web service will be hosted in Azure Container Service.

# ## Create the scoring web service
# 
# When deploying models for scoring with Azure Machine Learning services, you need to define the code for a simple web service that will load your model and use it for scoring. By convention this service has two methods init which loads the model and run which scores data using the loaded model.
# 
# This scoring service code will later be deployed inside of a specially prepared Docker container.

# In[7]:


get_ipython().run_cell_magic(u'writefile', u'summarizer_service.py', u'\nimport re\nimport nltk\nimport unicodedata\nfrom gensim.summarization import summarize, keywords\n\ndef clean_and_parse_document(document):\n    if isinstance(document, str):\n        document = document\n    elif isinstance(document, unicode):\n        return unicodedata.normalize(\'NFKD\', document).encode(\'ascii\', \'ignore\')\n    else:\n        raise ValueError("Document is not string or unicode.")\n    document = document.strip()\n    sentences = nltk.sent_tokenize(document)\n    sentences = [sentence.strip() for sentence in sentences]\n    return sentences\n\ndef summarize_text(text, summary_ratio=None, word_count=30):\n    sentences = clean_and_parse_document(text)\n    cleaned_text = \' \'.join(sentences)\n    summary = summarize(cleaned_text, split=True, ratio=summary_ratio, word_count=word_count)\n    return summary \n\ndef init():  \n    nltk.download(\'all\')\n    return\n\ndef run(input_str):\n    try:\n        return summarize_text(input_str)\n    except Exception as e:\n        return (str(e))')


# ## Create a Conda dependencies environment file
# 
# Your web service can have dependencies installed by using a Conda environment file. Items listed in this file will be conda or pip installed within the Docker container that is created and thus be available to your scoring web service logic.

# In[8]:


from azureml.core.conda_dependencies import CondaDependencies 

myacienv = CondaDependencies.create(pip_packages=['gensim','nltk'])

with open("C:\\Users\\veselne\\source\\repos\\nenves\\MCW-Cognitive-services-and-deep-learning\\Hands-on lab\\python\\PythonCode\\mydeployenv.yml","w") as f:
    f.write(myacienv.serialize_to_string())


# ## Deployment
# 
# In the following cells you will use the Azure Machine Learning SDK to package the model and scoring script in a container, and deploy that container to an Azure Container Instance.
# 
# Run the following cells.

# In[9]:


from azureml.core.webservice import AciWebservice, Webservice

aci_config = AciWebservice.deploy_configuration(
    cpu_cores = 1, 
    memory_gb = 1, 
    tags = {'name':'Summarization'}, 
    description = 'Summarizes text.')


# Next, build up a container image configuration that names the scoring service script, the runtime, and provides the conda file.

# In[10]:


service_name = "summarizer"
runtime = "python"
driver_file = "summarizer_service.py"
conda_file = "mydeployenv.yml"

from azureml.core.image import ContainerImage

image_config = ContainerImage.image_configuration(execution_script = driver_file,
                                                  runtime = runtime,
                                                  conda_file = conda_file)


# Now you are ready to begin your deployment to the Azure Container Instance.
# 
# Run the following cell. This may take between 5-15 minutes to complete.
# 
# You will see output similar to the following when your web service is ready: `SucceededACI service creation operation finished, operation "Succeeded"`

# In[11]:


webservice = Webservice.deploy(
  workspace=ws, 
  name=service_name, 
  model_paths=[],
  deployment_config=aci_config,
  image_config=image_config, 
  )

webservice.wait_for_deployment(show_output=True)


# ## Test the deployed service
# 
# Now you are ready to test scoring using the deployed web service. The following cell invokes the web service.
# 
# Run the following cells to test scoring using a single input row against the deployed web service.

# In[12]:


example_document = """
I was driving down El Camino and stopped at a red light.
It was about 3pm in the afternoon.  
The sun was bright and shining just behind the stoplight.
This made it hard to see the lights.
There was a car on my left in the left turn lane.
A few moments later another car, a black sedan pulled up behind me. 
When the left turn light changed green, the black sedan hit me thinking 
that the light had changed for us, but I had not moved because the light 
was still red.
After hitting my car, the black sedan backed up and then sped past me.
I did manage to catch its license plate. 
The license plate of the black sedan was ABC123. 
"""


# In[13]:


result = webservice.run(input_data = example_document)
print(result)


# ## Capture the scoring URI
# 
# In order to call the service from a REST client, you need to acquire the scoring URI. Run the following cell to retrieve the scoring URI and take note of this value, you will need it in the last notebook.

# In[14]:


webservice.scoring_uri


# The default settings used in deploying this service result in a service that does not require authentication, so the scoring URI is the only value you need to call this service.

# In[ ]:





