from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver (use your preferred WebDriver, e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to your page
driver.get("https://uat-destibrom-staging.itdev.app/")

# Wait for the page to load, adjust time as necessary
time.sleep(15)

# Locate the canvas element using XPath
# Locate the canvas element by XPath
canvas_element = driver.find_element(By.XPATH, '//*[@id="bar-chart"]')

# Use JavaScript to get the data URL (Base64 PNG representation of the canvas)
destination_elements = driver.find_elements("//ul/li")

# Iterate over each element and print its text
for element in destination_elements:
    print(element.text)

# Close the browser when done
driver.quit()
