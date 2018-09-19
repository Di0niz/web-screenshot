# Dynamic screenshots using python, selenium

import csv
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#import util
from selenium.webdriver.firefox.options import Options
from PIL import Image

from io import StringIO
import base64

"""Через selenium подключиться к snapio, 
определить место где находится картинка и скачать ее"""



# reading csv file
f = open('screenshot_details.csv')
csv_f = csv.reader(f)


options = Options()
options.add_argument( "--headless" )

# open firefox window
driver = webdriver.Firefox()

# Have a varibale for the folder name,
# so that it needs to replaced at only one place

folder_name = "screenshot_images"

# check if the directory exists, if it is just switch to it

if (os.path.isdir(folder_name)):
    os.chdir(folder_name)
else:
    # if it doesn't create that directory and switch to it

    os.mkdir(folder_name)
    os.chdir(folder_name)

for idx, (url, filename) in enumerate(csv_f):
    # skipping headers

    if idx > 0:
        # getting url

        driver.get(url)
        # getting image name and format

        driver.set_window_size(3000,3000)

        driver.save_screenshot(filename)
        
        # 1.
        # driver.get_screenshot_as_file(filename)

        # 2.
        #element=driver.find_element_by_tag_name('body')

        #print(dir(element)) 
        #element.screenshot(filename)
        #with open(filename, "wb") as file:
        #    file.write(element_png)        

        # 3. 
        #util.fullpage_screenshot(driver, filename)

        # 4.
        #driver.maximize_window()

        #driver.get_screenshot_as_file(filename)

        # 5.
        #elem = driver.find_element_by_tag_name("body")
        #print(dir(elem))

        # 6.
        #b64 = driver.get_screenshot_as_base64()
        #file = base64.decodestring(b64)

        break

# closing web driver

driver.quit()

# PEP8 checked
# ENH : optimizing images if possible, automating through batch / shell.