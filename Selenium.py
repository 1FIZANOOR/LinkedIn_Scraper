from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize the webdriver
driver = webdriver.Chrome()

# Login credentials
email = "**********"
password = "*******"

# Navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Wait for the email and password fields to be loaded
try:
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
except TimeoutException:
    print("Timeout waiting for login fields to load.")
    driver.quit()
    exit()

# Fill in the login credentials
email_field.send_keys(email)
password_field.send_keys(password)

# Submit the login form
password_field.submit()

# Wait for the user to manually complete the login process if necessary
# This is usually not required if the login fields are present

# Navigate to the profile page
profile_url = "************"
driver.get(profile_url)

# Wait for the company name element to be loaded
try:
    # Update the XPath to match the current LinkedIn layout
    company_name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='text-body-small inline t-black--light break-words']"))
    )
    print("Company Name:", company_name_element.text)
except TimeoutException:
    print("Timeout waiting for company name element to load.")
try:
    person_name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'text-heading-xlarge')]"))
    )
    print("Person's Name:", person_name_element.text)
except TimeoutException:
    print("Timeout waiting for person's name element to load.")
try:
    email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'pv-contact-info__contact-type')]//a[starts-with(@href, 'mailto:')]"))
    )
    email_address = email_element.get_attribute('href').split(':')[1]
    print("Email Address:", email_address)
except TimeoutException:
    print("Timeout waiting for email element to load.")

# Close the driver
driver.quit()