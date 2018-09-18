# Dynamic screenshots using python, selenium

import csv
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True


# reading csv file
f = open('screenshot_details.csv')
csv_f = csv.reader(f)

# open firefox window
driver = webdriver.Firefox(capabilities=caps)

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

for idx, row in enumerate(csv_f):
    # skipping headers

    if idx > 0:
        # getting url

        driver.get(row[0])
        # getting image name and format

        # driver.save_screenshot(row[1])

        driver.get_screenshot_as_file(row[1])

# closing web driver

driver.quit()

# PEP8 checked
# ENH : optimizing images if possible, automating through batch / shell.