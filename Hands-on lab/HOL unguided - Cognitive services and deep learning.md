![](https://github.com/Microsoft/MCW-Template-Cloud-Workshop/raw/master/Media/ms-cloud-workshop.png "Microsoft Cloud Workshops")

# Cognitive services and deep learning   
## Hands-on lab unguided    
June 2018

Information in this document, including URL and other Internet Web site references, is subject to change without notice. Unless otherwise noted, the example companies, organizations, products, domain names, e-mail addresses, logos, people, places, and events depicted herein are fictitious, and no association with any real company, organization, product, domain name, e-mail address, logo, person, place or event is intended or should be inferred. Complying with all applicable copyright laws is the responsibility of the user. Without limiting the rights under copyright, no part of this document may be reproduced, stored in or introduced into a retrieval system, or transmitted in any form or by any means (electronic, mechanical, photocopying, recording, or otherwise), or for any purpose, without the express written permission of Microsoft Corporation.

Microsoft may have patents, patent applications, trademarks, copyrights, or other intellectual property rights covering subject matter in this document. Except as expressly provided in any written license agreement from Microsoft, the furnishing of this document does not give you any license to these patents, trademarks, copyrights, or other intellectual property.

The names of manufacturers, products, or URLs are provided for informational purposes only, and Microsoft makes no representations and warranties, either expressed, implied, or statutory, regarding these manufacturers or the use of the products with any Microsoft technologies. The inclusion of a manufacturer or product does not imply endorsement of Microsoft of the manufacturer or product. Links may be provided to third-party sites. Such sites are not under the control of Microsoft and Microsoft is not responsible for the contents of any linked site or any link contained in a linked site, or any changes or updates to such sites. Microsoft is not responsible for webcasting or any other form of transmission received from any linked site. Microsoft is providing these links to you only as a convenience, and the inclusion of any link does not imply endorsement of Microsoft of the site or the products contained therein.

©  2018 Microsoft Corporation. All rights reserved.

Microsoft and the trademarks listed at <https://www.microsoft.com/en-us/legal/intellectualproperty/Trademarks/Usage/General.aspx> are trademarks of the Microsoft group of companies. All other trademarks are the property of their respective owners.

**Contents**

<!-- TOC -->

- [Cognitive services and deep learning hands-on lab unguided](#cognitive-services-and-deep-learning-hands-on-lab-unguided)
    - [Abstract and learning objectives](#abstract-and-learning-objectives)
    - [Overview](#overview)
    - [Solution architecture](#solution-architecture)
    - [Requirements](#requirements)
    - [Exercise 1: Setup Azure Machine Learning accounts](#exercise-1-setup-azure-machine-learning-accounts)
        - [Task 1: Provision Azure Machine Learning Experimentation service](#task-1-provision-azure-machine-learning-experimentation-service)
            - [Tasks to complete](#tasks-to-complete)
            - [Exit criteria](#exit-criteria)
        - [Task 2: Create the Azure Machine Learning project](#task-2-create-the-azure-machine-learning-project)
            - [Tasks to complete](#tasks-to-complete-1)
            - [Exit criteria](#exit-criteria-1)
        - [Task 3: Install dependencies](#task-3-install-dependencies)
            - [Tasks to complete](#tasks-to-complete-2)
            - [Exit criteria](#exit-criteria-2)
    - [Exercise 2: Deploy the Summarizer as a Service](#exercise-2-deploy-the-summarizer-as-a-service)
        - [Task 1: Deploy your ACS cluster](#task-1-deploy-your-acs-cluster)
            - [Tasks to complete](#tasks-to-complete-3)
            - [Exit criteria](#exit-criteria-3)
        - [Task 2: Set Visual Studio Code as the project IDE in Workbench](#task-2-set-visual-studio-code-as-the-project-ide-in-workbench)
            - [Tasks to complete](#tasks-to-complete-4)
            - [Exit criteria](#exit-criteria-4)
        - [Task 3: Create the Summarization service](#task-3-create-the-summarization-service)
            - [Tasks to complete](#tasks-to-complete-5)
            - [Exit criteria](#exit-criteria-5)
        - [Task 4: Deploy the Summarization service](#task-4-deploy-the-summarization-service)
            - [Tasks to complete](#tasks-to-complete-6)
            - [Exit criteria](#exit-criteria-6)
    - [Exercise 3: Applying TensorFlow](#exercise-3-applying-tensorflow)
        - [Task 1: Prepare TensorFlow](#task-1-prepare-tensorflow)
            - [Tasks to complete](#tasks-to-complete-7)
            - [Exit criteria](#exit-criteria-7)
        - [Task 2: Train and deploy the TensorFlow model](#task-2-train-and-deploy-the-tensorflow-model)
            - [Tasks to complete](#tasks-to-complete-8)
            - [Exit criteria](#exit-criteria-8)
    - [Exercise 4: Completing the solution](#exercise-4-completing-the-solution)
        - [Task 1: Deploy the Computer Vision API](#task-1-deploy-the-computer-vision-api)
            - [Tasks to complete](#tasks-to-complete-9)
            - [Exit criteria](#exit-criteria-9)
        - [Task 2: Deploy the Text Analytics API](#task-2-deploy-the-text-analytics-api)
            - [Tasks to complete](#tasks-to-complete-10)
            - [Exit criteria](#exit-criteria-10)
        - [Task 3: Completing the solution](#task-3-completing-the-solution)
            - [Tasks to complete](#tasks-to-complete-11)
            - [Exit criteria](#exit-criteria-11)
    - [After the hands-on lab](#after-the-hands-on-lab)
        - [Task 1: Clean up lab resources](#task-1-clean-up-lab-resources)

<!-- /TOC -->

# Cognitive Services and deep learning hands-on lab unguided 

## Abstract and learning objectives 

In this hands-on lab, you will implement and deploy a monitoring a web application to Azure IaaS. Azure security and management services will be used to manage and monitor the operational performance and security of the underlying infrastructure. Azure Application Insights will be used to monitor performance, application usage, and identify the cause of any application issues that emerge.

At the end of this hands-on lab, you will be better able to implement solutions leveraging Azure Machine Learning services and Cognitive Services.

## Overview

In this workshop you will help Contoso Ltd. Build a proof of concept that shows how they could build a solution that amplifies the claims processing capabilities of their agents.

## Solution architecture

The high-level architecture of the solution is illustrated in the diagram. The lab is performed within the context of a Jupyter Notebook running within a VM on Azure. Various notebooks are built to test the integration with the Cognitive Services listed, to train customer ML services, and to integrate the results in a simple user interface that shows the result of processing the claim with all of the AI services involved.

![The High-level architectural solution begins with a Claim, which points to Jupyter notebook. Jupyter then points to Computer Vision, Text Analytics, and Containerized Services, which includes a Classification Service and a Summary Service that both process claim text.](images/Hands-onlabunguided-CognitiveServicesanddeeplearningimages/media/image2.png "High-level architectural solution")

## Requirements

1.  Microsoft Azure subscription must be pay-as-you-go or MSDN

    a.  Trial subscriptions will not work. You will run into issues with Azure resource quota limits.

    b.  Subscriptions with access limited to a single resource group will not work. You will need the ability to deploy multiple resource groups.


## Exercise 1: Setup Azure Machine Learning accounts

Duration: 45 minutes

In this exercise, you will setup your Azure Machine Learning Experimentation and Model Management Accounts and get your project environment setup.

### Task 1: Provision Azure Machine Learning Experimentation service

#### Tasks to complete

1.  In your Azure subscription, provision an instance of the Azure Machine Learning Experimentation service in the same resource group in which you created the lab VM. Make sure to also provision an instance of the Model Management Service along with it. Choose an S1 model management pricing tier.

#### Exit criteria 

-   Navigate to your mcw-ai-lab resource group and confirm that you see an instance of Machine Learning Experimentation and Machine Learning Model Management.\
    ![Both Machine Learning Experimentation and Machine Learning Model Management are called out in the Resource group list.](images/Hands-onlabunguided-CognitiveServicesanddeeplearningimages/media/image19.png "Resource group")

### Task 2: Create the Azure Machine Learning project

#### Tasks to complete

1.  Log in to your lab VM via RDP

2.  Launch the Azure Machine Learning Workbench

3.  Create a new project using the TDSP template, with the following settings:

    -   **Project** name: mcw-ai-lab

    -   **Project directory**: C:\\HOL

    -   **Project description**: leave blank

    -   **Vistualstudio.com GIT Repository** URL: leave blank

    -   **Selected workspace:** select the ML Experimentation Workspace you created

#### Exit criteria 

-   The TDSP project dashboard appears after successfully creating the project.\
    ![Screenshot of the TDSP project dashboard.](images/Hands-onlabunguided-CognitiveServicesanddeeplearningimages/media/image20.png "TDSP project dashboard")

### Task 3: Install dependencies

The tasks that follow depend on Python libraries like nltk and gensim. The following steps ensure you have these installed in your environment.

#### Tasks to complete

1.  Open the Command Prompt from the Workbench

2.  Use the pip install command to install the gensim module

3.  Use the pip install command to install the nltk module

4.  Run the python shell and download the nltk modules by running:
    ```
    import nltk
    nltk.download('all')
    ```

5.  Download the Jupyter Notebook used in this section from: <http://bit.ly/2G4hAQz>

6.  Run the Jupyter Notebook command from within your HoL directory

7.  Upload the notebook you downloaded to the code \\ 01\_data\_acquisition\_and\_understanding folder using the Jupyer Notebook UI

8.  Open Summarize.ipynb and follow the instructions within it

#### Exit criteria 

-   You were able to execute all the cells in Summarize.ipynb and have been able to summarize long strings of text

## Exercise 2: Deploy the Summarizer as a Service

Duration: 45 minutes

In this exercise, you will create and deploy a web service that uses a pre-trained model to summarize long paragraphs of text.

### Task 1: Deploy your ACS cluster 

#### Tasks to complete

1.  Within Workbench, from the **File** menu, select **Open Command Prompt**

2.  Use the CLI to create a new cluster environment:
    ```
    az ml env setup -c -n <environment name> --location <e.g. eastus2>
    ```

3.  Check on the status of the deployment with:
    ```
    az ml env show -g <resourceGroupName> -n <clusterName>
    ```

4.  Set the context of the command line to your new environment:
    ```
    az ml env set -g <resourceGroupName> -n <clusterName>
    ```

5.  Set the model management account to be used by the command line:
    ```
    az ml account modelmanagement set -n <acctname> -g <resourcegroupname>
    ```

#### Exit criteria 

-   Your command line environment is set with a default environment and model management account, and you have an ACS cluster deployed.

### Task 2: Set Visual Studio Code as the project IDE in Workbench

#### Tasks to complete

1.  Configure the Workbench to use Visual Studio Code as the default IDE

    -   Use an Executable Path of C:\\Program Files\\Microsoft VS Code\\Code.exe

2.  Launch Visual Studio Code from the File menu of the Workbench

#### Exit criteria 

-   Visual Studio Code is open

### Task 3: Create the Summarization service

#### Tasks to complete

1.  Within Visual Studio Code, under the code\\03\_deployment folder, create a new file called "summarizer\_service.py"

2.  In that file, paste the code from <http://bit.ly/2FLJn8Y>

3.  Read through the code file to understand the structure of the service

4.  Modify the conda\_dependencies.yml file to add pip entries for gensim, tensorflow and tflearn

5.  Create an empty file named "dummy\_model.bin" in the code\\03\_deployment folder to act as a placeholder for the model file required by the CLI

#### Exit criteria 

-   You have created or modified the three aforementioned files

### Task 4: Deploy the Summarization service

#### Tasks to complete

1.  Launch an instance of the command prompt from the Workbench

2.  Deploy the summarizer service using the CLI by running the following command:
    
    az ml service create realtime -n summarizer -c ..\\..\\aml\_config\\conda\_dependencies.yml -m dummy\_model.bin -f summarizer\_service.py -r python

3.  Test the deployed service with the following command (modify the parameter values to suit your actual deployment):

    az ml service run realtime -i summarizer.**\[mcwailab-xyz.location\]** -d \"I was driving down El Camino and stopped at a red light. It was about 3pm in the afternoon. The sun was bright and shining just behind the stoplight. This made it hard to see the lights. There was a car on my left in the left turn lane. A few moments later another car, a black sedan pulled up behind me. When the left turn light changed green, the black sedan hit me thinking that the light had changed for us, but I had not moved because the light was still red. After hitting my car, the black sedan backed up and then sped past me. I did manage to catch its license plate. The license plate of the black sedan was ABC123."

4.  Verify you get a summary back

5.  In a notepad or other location take note of the full Service ID (e.g., summarizer.mcwailab-xyz.location) and the authorization key, which you will need later in the lab. To get the authorization key for your deployed service, run the following command and take note of the PrimaryKey value in the output:

    ```
    az ml service keys realtime -i summarizer.[mcwailab-xyz.location]
    ```

#### Exit criteria 

-   You were able to successfully receive a summary for the submitted claim text, similar to the following:

    ![In the Command Prompt window, the previous text displays.](images/Hands-onlabunguided-CognitiveServicesanddeeplearningimages/media/image21.png "Command Prompt window")

-   You have retrieved and noted the authorization key, similar to the following:

    ![In the Command Prompt window, the previous command and its output display. At this time, we are unable to capture all of the information in the command prompt window. Future versions of this course should address this.](images/Hands-onlabunguided-CognitiveServicesanddeeplearningimages/media/image22.png "Command Prompt window")


## Exercise 3: Applying TensorFlow

Duration: 60 minutes

In this exercise, you use TensorFlow to construct and train a simple deep neural network classification model that will classify claim text as belonging to a home insurance claim or an automobile claim. You will then deploy this trained model as a web service.

### Task 1: Prepare TensorFlow

#### Tasks to complete

1.  Within your RDP session to the lab VM, switch to the command prompt that is running the Jupyter Notebook command and press **Control + Break**. This will stop the jupyter notebook process while you update TensorFlow.

2.  Use the pip command to install tensorflow

3.  Use the pip command to install tflearn

4.  Start the Jupyter Notebook process again

#### Exit criteria 

-   Your environment now has the tensorflow and tflearn modules installed

### Task 2: Train and deploy the TensorFlow model

#### Tasks to complete

1.  Download the starter files for this task from <http://bit.ly/2pucpje>

2.  Extract this zip and copy the contents to C:\\HOL\\mcw-ai-lab\\code\\02\_modeling

3.  Open "Claim Classification.ipynb" using the Jupyter Notebook web interface

4.  Step through this notebook to read how the data is prepared and the neural network model is trained. Be sure to execute each cell as you get to it.

5.  Navigate to C:\\HOL\\mcw-ai-lab\\code\\02\_modeling and confirm you see the three new files (each beginning with claim\_classifier.tfl)

6.  Copy these three files and paste them under C:\\HOL\\mcw-ai-lab\\code\\03\_deployment\\claim\_class\_service. You are copying these over so they can be used by the predictive web service we will deploy.

7.  Download the supporting files for the claim\_class\_service from: <http://bit.ly/2u5DoGH>

8.  Extract the files and copy them into C:\\HOL\\mcw-ai-lab\\code\\03\_deployment\\claim\_class\_service

9.  Using the Jupyter Notebook interface, open claim\_class\_service.py and observe that the code it uses is like what you ran in the Claim Classification notebook, only formatted to fit the structure of an Azure Machine Learning web service (with init and run methods)

10. Switch to your command line window and navigate to C:\\HOL\\mcw-ai-lab\\code\\03\_deployment\\claim\_class\_service and run:

    ```
    az ml service create realtime -n claimclassifier -c ..\..\..\aml_config\conda_dependencies.yml -m claim_classifier.tfl.meta -f claim_class_service.py -r python -d claim_classifier.tfl.data-00000-of-00001 -d claim_classifier.tfl.index -d claims_text.txt -d textanalytics.py -d contractions.py
    ```

11. Test the deployed service by submitting to it a string like "A tornado ripped thru my home"

    ```
    az ml service run realtime -i claimclassifier.[mcwailab-xyz.location] -d "A tornado ripped thru my home"
    ```

12. Verify a class number is returned (0 or 1)

13. Acquire and note the authorization key for this service

#### Exit criteria 

-   You have deployed and successfully invoked the claims classifier service

-   You have noted the authorization key for the service

## Exercise 4: Completing the solution

Duration: 45 minutes

In this exercise, you perform the final integration with the Computer Vision API and the Text Analytics API along with the Azure Machine Learning Services you previously deployed to deliver the completed proof of concept solution

### Task 1: Deploy the Computer Vision API

#### Tasks to complete

1.  Deploy an instance of the Computer Vision API

2.  Take note of the KEY 1 and the endpoint URL

#### Exit criteria 

-   You have deployed an instance of the Computer Vision API

-   You have noted the values important to connecting to it

### Task 2: Deploy the Text Analytics API

#### Tasks to complete

3.  Deploy an instance of the Text Analytics API

4.  Take note of the KEY 1 and the endpoint URL

#### Exit criteria 

-   You have deployed an instance of the Text Analytics API

-   You have noted the values important to connecting to it

### Task 3: Completing the solution

#### Tasks to complete

1.  Download the starter files for this task from: <http://bit.ly/2puj7oL>

2.  Extract the contents of this zip file to C:\\HOL\\mcw-ai-lab\\code\\03\_deployment

3.  In the Jupyter Notebook web interface, open "Cognitive Services.ipynb"

4.  Follow the steps within the notebook to complete the lab and view the result of combining Cognitive Services with your Azure Machine Learning Services.

#### Exit criteria 

-   You are able to create a claim summary that integrates calls to all of the AI services, similar to the following:

    ![The Claim Summary results display.](images/Hands-onlabunguided-CognitiveServicesanddeeplearningimages/media/image23.png "Claim Summary results")

## After the hands-on lab 

Duration: 5 minutes

To avoid unexpected charges, it is recommended that you clean up all of your lab resources when you complete the lab.

### Task 1: Clean up lab resources

1.  Navigate to the Azure Portal and locate the Resource Groups you created for this lab

    a.  mcw-ai-lab

    b.  mcwailabenv (note there are two resources groups starting with this name, so delete both)

2.  Select **Delete resource group** from the command bar

    ![Screenshot of the Delete resource group button.](images/Hands-onlabunguided-CognitiveServicesanddeeplearningimages/media/image24.png "Delete resource group button")

3.  In the confirmation dialog that appears, enter the name of the resource group and select **Delete**

4.  Wait for the confirmation that the Resource Group has been successfully deleted. If you don't wait, and the delete fails for some reason, you may be left with resources running that were not expected. You can monitor using the Notifications dialog, accessible from the Alarm icon.

    ![The Notifications dialog box has a message stating that the resource group is being deleted.](images/Hands-onlabunguided-CognitiveServicesanddeeplearningimages/media/image25.png "Notifications dialog box")

5.  When the Notification indicates success, the cleanup is complete

    ![The Notifications dialog box has a message stating that the resource group has been deleted.](images/Hands-onlabunguided-CognitiveServicesanddeeplearningimages/media/image26.png "Notifications dialog box")

You should follow all steps provided *after* attending the Hands-on lab.

