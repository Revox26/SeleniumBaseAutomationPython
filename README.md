# Welcome to Automation Project

Hello, I am Jeremy Marcos the creator of this project

This repository contains an automation framework that allows you to streamline various tasks with ease. Follow the steps
below to get started and make your life easier through automation.

# User Manual for QA-Team Automation Test Runner

## Table of Contents
1. Introduction
2. Set up and installation
3. Getting started
4. Test Configuration
5. Test Execution
6. Troubleshooting

# 1. Introduction

The QA-Team Automation Test Runner is a Python application designed to facilitate the execution of automated test
scripts using the selenium python framework. This user manual will guide you through the installation, configuration,
and usage
of the application. The application allows you to select a specific test, configure testing options, and execute the
tests with ease.

### Requirements

- Python 3.11.5
- Seleniumbase
- selenium
- pytest

# 2. Set up and installation

Follow these simple steps to set up and run the automation project:
1. Clone the Repository:
- Clone this repository to your local machine using the following command: <code> git
  clone https://github.com/Jeremy-QA/SeleniumBaseAutomationPython.git </code>

2. Provide Important Data:
- Contact the project owner or maintainer to obtain the necessary data such as URL, username, and password.
  Paste the file of important data into configuration_files.

3. Navigate to the Project Directory:
- Open your command-line interface (e.g., Command Prompt or Terminal).
  Navigate to the project directory using the cd command: <code> cd path/to/automation-project </code>

4. Create a Virtual Environment:
- Create a Python virtual environment for your project using the following command: <code> python -m venv yourEnvironmentName </code>

5. Activate the Virtual Environment:
- Activate the virtual environment by running the appropriate command for your operating system: 
  <code> yourEnvironmentName\Scripts\activate </code>

6. Install Project Dependencies:
- Install the required Python packages from the requirements.txt file using pip: <code> pip install -r requirements.txt </code>

7. Navigate to the Test Directory:
- Move to the tests directory using the following command: <code> cd test_runner </code>

8. Run the Automation Test Runner GUI App:
- Start the automation framework by running the main application script: <code> python app.py </code>

Now you're all set! You can enjoy the automation framework and streamline your tasks efficiently.

![img.png](img.png)

# 3. Getting started
Once you have installed the required software, follow these steps to start using the QA-Team Automation Test Runner:

# 4. Test Configuration
1. ### Select a Test
- Use the "Select a Test" dropdown to choose the specific test you want to run.

2. ### Select Staging Environment
- Use the "Select Staging Environment" dropdown to choose the testing environment for your test.

3. ### Select Browser
- Use the "Select Browser" dropdown to specify the browser you want to use for testing.

3. ### Additional Options
- Use the "Additional Options" text box to provide any additional command-line options for your pytest tests.

4. ### Test Options
- Test Options
You can enable or disable various test options using checkboxes, such as "Demo Mode," "Slow Mode," "Generate Report," "Save Screenshot," "Incognito Mode," and "Start Maximized." Each checkbox has a tooltip with an explanation of its purpose.

# 5. Test Execution 
After configuring your test, you can execute it:
1. Click the "Run" button to start the test.
2. The selected pytest test command will be generated based on your configuration.
3. The test will execute, and the test output will be displayed in the command prompt or terminal window.


# Video Demonstration
![sample_automation.gif](..%2FUsers%2FJeremy%20Marco%2FDownloads%2Fsample_automation.gif)

# 6. Troubleshooting
If you encounter any issues while using the QA-Team Automation Test Runner, consider the following troubleshooting steps:
- Check Python Installation: Ensure you have Python 3.x installed and the required packages.
- Syntax Errors: Check the code for any syntax errors, and ensure you have the correct code file.
- Test Selection: Make sure you select a valid test from the dropdown.
- Configuration: Verify that your test configuration is correct, including staging environment and browser selection.
- Check Test Output: Review the test output in the terminal for any error messages.

# Contribute
If you'd like to contribute to this project or report issues, please open a pull request or create an issue in the
GitHub repository. Your contributions and feedback are highly appreciated.

# License
This project is open-source and available under the MIT License. Feel free to use and modify it according to your needs.
Happy automating! 🤖✨
