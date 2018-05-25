from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
from selenium import webdriver
from BeautifulSoup import BeautifulSoup as soup
import sys
import requests
def main(urls):
    validIPS = []
    path = r"[{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$]"
    for i in urls:
        driver = webdriver.Chrome('/Users/nick/Downloads/chromedriver')
        driver.get(i)
        x = driver.page_source
        #x = requests.get(i).text
        print(type(x))
        
        y = re.search(path,x)
        if(y):
            validIPS.append(y.group())
        #except:
         #   print("Error with {}".format(i))
          #  continue
    with open('validIPS.csv','w+') as file:
        for i in validIPS:
       	    file.write(str(i)+'\n')
    print(len(validIPS))
if __name__ == "__main__":
    URLS = sys.argv[1:]
    main(URLS)
