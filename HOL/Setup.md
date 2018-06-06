
# Cognitive Services and Deep Learning setup

## Requirements

1.  Microsoft Azure subscription must be pay-as-you-go or MSDN

    a.  Trial subscriptions will not work

## Before the hands-on lab

Duration: 30 minutes

To maximize your lab time, the following steps which setup your environment should be performed before attending the lab.

#### Task 1: Provision the Windows Data Science Virtual Machine

1.  Navigate to the Azure Portal at <https://portal.azure.com>.

2.  Select **Create a resource**.\
    ![Screenshot of the Create a resource button.](images/Setup/image3.png "Create a resource button")

3.  Select **AI + Cognitive Services** and then select **Data Science Virtual Machine Windows 2016**.\
    ![In the New blade, both AI + Cognitive Services and Data Science Virtual Machine Windows 2016 are selected.](images/Setup/image4.png "New blade")

4.  On the **Basics** blade provide the following inputs:

    a.  **Name**: enter labvm

    b.  **VM disk type**: select HDD. This will enable you to use a GPU based machine if you choose to in the subsequent step.

    c.  **User name**: enter demouser

    d.  **Password and Confirm Password:** enter Abc!1234567890

    e.  **Subscription**: select your Azure subscription

    f.  **Resource group**: select Create new and provide the name mcw-ai-lab

    g.  **Location**: select either South Central US or East US (or any of the regions in which the NC-series VM's are currently available, see the [regions service page](https://azure.microsoft.com/en-us/global-infrastructure/services/) for an up to date listing).

    ![The Basics blade fields are set to the previously defined settings.](images/Setup/image5.png "Basics blade")

5.  Select **OK**.

6.  On the **Choose a size** blade, select **NC6 Standard** and choose **Select.**

    ![In the Choose a size blade, the NC6 Standard option is selected.](images/Setup/image6.png "Choose a size blade")

7.  Leave all values on the Settings blade at their defaults and select OK.\
    ![Fields in the settings blade are set to the default settings.](images/Setup/image7.png "Settings blade")

8.  On the Create blade, review the summary and then select Create.\
    ![Screenshot of the Create blade.](images/Setup/image8.png "Create blade")

9.  The VM should take 10-15 minutes to provision.

#### Task 2: Verify Remote Desktop access to Data Science VM

1.  When the VM is ready, you should see a notification. Select **Go to resource** to view the deployed Data Science VM in the Portal.\
    ![The Notification window has the message that Deployment succeeded.](images/Setup/image9.png "Notification window")

2.  On the blade for the VM, select **Connect**. This will download a Remote Desktop (RDP) file.

    ![Screenshot of the Connect button.](images/Setup/image10.png "Connect button")

3.  Open the downloaded RDP file.

4.  At the prompt, ensure **Clipboard** is checked and select **Continue**.\
    ![The Warning prompts you to ensure that you trust the remote computer prior to connecting. The Clipboard checkbox is selected.](images/Setup/image11.png "Warning prompt")

5.  Enter the **username** (demouser) and **password** (Abc!1234567890) and select **Connect** to login.\
    ![Screenshot of the Log in page.](images/Setup/image12.png "Log in page")

6.  Select **Connect** on the dialog that follows.\
    ![Screenshot of the Accept certificate and connect dialog box.](images/Setup/image13.png "Accept certificate and connect dialog box")

7.  Within a few moments, you should see the desktop for your new Data Science Virtual Machine.\
    ![Screenshot of the Data Science Virtual Machine Desktop.](images/Setup/image14.png "Desktop")

#### Task 3: Initialize Azure Machine Learning Workbench

Before using the Azure Machine Learning Workbench on the Data Science VM, you will need to take the one-time action of double-clicking on the AzureML Workbench Setup icon on the desktop to install your instance of the workbench.

1.  Within the RDP session to the Data Science VM, on the desktop locate the AzureML Workbench Setup.\
    ![Screenshot of the AzureML Workbench Setup desktop icon.](images/Setup/image15.png "AzureML Workbench Setup desktop icon")

2.  Double-click the icon to install the Workbench.

3.  At the **Open File -- Security Warning** dialog, select **Run**.\
    ![Screenshot of the Open File - Security Warning dialog box.](images/Setup/image16.png "Open File - Security Warning dialog box")

4.  Step through all the prompts leaving all values at their defaults to complete the Workbench installation. Installation will take about 25 minutes. Use the **X** to close the install when it is finished.

    ![The Azure Machine Learning Workbench Installer screen displays the message, Installation successful.](images/Setup/image17.png "Azure Machine Learning Workbench Installer screen")

#### Task 4: Stop the Data Science VM

If you are performing this setup the night before the hands-on lab, you can optionally Stop the VM to save on costs overnight, and resume it when you are ready to start on the lab. Follow these steps to Stop the VM:

1.  Return to the Azure Portal.

2.  Navigate to the blade of your labvm.

3.  Select the **Stop** button.\
    ![Screenshot of the Stop button.](images/Setup/image18.png "Stop button")

> **NOTE:** When you are ready to resume the VM, simply follow the previous steps and instead of selecting Stop, select **Start**. You VM will take about 5 minutes to start up, after which you can use the **Connect** button in the VM blade to RDP into the VM as before.

You should follow all steps provided *before* attending the hands-on lab.
