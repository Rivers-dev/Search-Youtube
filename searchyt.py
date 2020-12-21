#Written by @Rivers-dev on github
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


x = input('Enter query to search YouTube: ')
query = 'https://www.youtube.com/results?search_query=' + x.replace(' ', '+')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(firefox_options = options, executable_path=rPATH)
driver.minimize_window()
driver.get(query)
videos = driver.find_elements_by_class_name('style-scope ytd-video-renderer')
for v in range(len(videos)):
    print(str(v) + ': ' + videos[v].text + '\n')
x = input('Enter the number associated with the desired video or "q" to quit: ')
if x == 'q':
    sys.exit()
else:
    try:
        videos[int(x)].click()
        driver.maximize_window()
    except (AttributeError):
        print('Unable to access element.\n')
        sys.exit()
