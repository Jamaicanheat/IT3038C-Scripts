import selenium
from selenium.webdriver.chrome.options import Options

# Create a ChromeOptions object
options = Options()

# Add the path to the extension to the ChromeOptions object
options.add_extension('path/to/extension.crx')

# Create a ChromeDriver instance with the ChromeOptions object
driver = webdriver.Chrome(chrome_options=options)

# Navigate to a web page
driver.get('https://www.example.com')

# Inject JavaScript code into the web page
driver.execute_script('console.log("Hello from the extension!")')

# Close the browser
driver.quit()
