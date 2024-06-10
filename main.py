from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from PIL import Image
from io import BytesIO
import os
import shutil
import numpy as np

# Cleanup and create directories
if os.path.exists("./AMC/"):
    shutil.rmtree("./AMC/")
os.makedirs("./AMC/10/", exist_ok=True)

# Setup Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Setup Chrome service
service = Service(executable_path='./chromedriver.exe')

# Initialize the Chrome driver
driver = webdriver.Chrome()

for year in range(2002, 2025):
    year_path = "./AMC/10/%d/" % year
    os.makedirs(year_path, exist_ok=True)
    for exam in 'AB':
        exam_path = os.path.join(year_path, exam)
        os.makedirs(exam_path, exist_ok=True)
        for problem in range(1, 26):
            url = f"https://artofproblemsolving.com/wiki/index.php/{year}_AMC_10{exam}_Problems/Problem_{problem}"
            driver.get(url)
            wait = WebDriverWait(driver, 20)
            try:
                div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "mw-parser-output")))
                elements = div.find_elements(By.XPATH, "*")

                ims = []
                start_capture = False
                for element in elements:
                    if element.tag_name == "h2" and start_capture:
                        break
                    if start_capture:
                        location = element.location
                        size = element.size
                        png = driver.get_screenshot_as_png()
                        im = Image.open(BytesIO(png))
                        left = location['x']
                        top = location['y']
                        right = location['x'] + size['width']
                        bottom = location['y'] + size['height']
                        im = im.crop((left, top, right, bottom))
                        ims.append(im)
                    if element.tag_name == "h2":
                        start_capture = True

                if ims:
                    image = np.vstack([np.asarray(im) for im in ims])
                    image = Image.fromarray(image)
                    image.save(os.path.join(exam_path, f"{problem}.png"))
                    print("Saved "+ exam_path + f"{problem}.png")
            except Exception as e:
                print(f"ERROR: {str(e)}")
                continue

driver.quit()
