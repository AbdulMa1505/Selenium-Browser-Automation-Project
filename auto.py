from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def AutoWeb():
    # Path to ChromeDriver
    driver_path = "C:\\Users\\Abdul Malik\\chromedriver.exe"  

    # Options for Brave browser
    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    # Initialize the driver using Service object
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Automating YouTube Search
    print("Opening YouTube...")
    driver.get("https://www.youtube.com")
    time.sleep(3)

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Python tutorials")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    # Automating Gmail Login Attempt (enter your email)
    print("Opening Gmail...")
    driver.get("https://www.gmail.com")
    time.sleep(3)

    email_input = driver.find_element(By.ID, "identifierId")
    email_input.send_keys("yourmail@gmail.com")
    next_button = driver.find_element(By.ID, "identifierNext")
    next_button.click()
    time.sleep(3)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("123456")  # Input your password
    next_button = driver.find_element(By.ID, "passwordNext")  # Locate "Next" button for password
    next_button.click()  # Click Next to attempt login
    time.sleep(5)

    # Close the browser after automation
    driver.quit()

AutoWeb()
