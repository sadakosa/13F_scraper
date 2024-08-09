from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up the WebDriver options (optional, depending on your setup)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode, i.e., without a browser window

# Set up the WebDriver (make sure the path to your chromedriver is correct)
service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the target page
target_url = "https://www.sec.gov/Archives/edgar/data/1067983/000095015000000118/0000950150-00-000118.txt"
driver.get(target_url)

# Find the <pre> tag with the specified style and extract the text
pre_element = driver.find_element(By.CSS_SELECTOR, "pre[style='word-wrap: break-word; white-space: pre-wrap;']")
pre_text = pre_element.text

# Output the extracted text
print("Extracted text:")
print(pre_text)

# Close the browser
driver.quit()
