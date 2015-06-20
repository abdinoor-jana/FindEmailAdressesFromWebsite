from selenium import webdriver
from selenium.webdriver.common.by import By
from sets import Set
import lepl.apps.rfc3696
import sys
import urllib2
####################################################################################################
# Functions Definition:
def findEmailAdress(url):
    driver.get(url)
    print 'Checking URL:' + url + ', Domain: ' + domain

    # 1. Check hyperlink: Find a tag that has the same domain with typed url
    checkHyperlinks(driver.find_elements_by_tag_name('a'))

    # 2. Check clickable: Find every tag that has ng-click attribute. //*[@class="menu"]
    checkNgClickables(driver.find_elements(By.XPATH, '//*[string(@ng-click)]'))

    # 3. Check clickable: Find every tag that has ng-click attribute. //*[@class="menu"]
    checkClickables(driver.find_elements(By.XPATH, '//*[string(@click)]'))

def checkHyperlinks(hyperlinks):
    for hyperlink in hyperlinks:
        try:
            redirectUrl = hyperlink.get_attribute('href')
            # Redirect if the link that has the same domain and prevent duplicate redirection
            if (redirectUrl is not None) and (redirectUrl not in redirectUrlSet):
                if hyperlink.is_displayed():
                    redirectUrlSet.add(redirectUrl)
                    isRedirect(redirectUrl)
            # Check if it is an email address
            isEmail(hyperlink.text)
        except:
            # print "Unexpected error:", sys.exc_info()[0]
            return

def isEmail(string):
    email_validator = lepl.apps.rfc3696.Email()
    if email_validator(string):
        global emailCounts
        emailCounts += 1
        emailSet.add(string)
        print "Email Found: " + string

def checkNgClickables(clickableLinks):
    for clickableLink in clickableLinks:
        try:
            ngClick = clickableLink.get_attribute('ng-click')
            if (ngClick is not None) and (ngClick not in clickableTagSet):
                if clickableLink.is_displayed():
                    clickableTagSet.add(ngClick)
                    clickableLink.click()
                    print 'Clicked:' + ngClick
                    # Check hyperlink
                    checkHyperlinks(driver.find_elements_by_tag_name('a'))
            # print 'Clickable:' + ngClick
        except:
            # print "Unexpected error:", sys.exc_info()[0]
            return

def checkClickables(clickableLinks):
    for clickableLink in clickableLinks:
        try:
            ngClick = clickableLink.get_attribute('click')
            if (ngClick is not None) and (ngClick not in clickableTagSet):
                if clickableLink.is_displayed():
                    clickableTagSet.add(ngClick)
                    clickableLink.click()
                    print 'Clicked:' + ngClick
                    # Check hyperlink
                    checkHyperlinks(driver.find_elements_by_tag_name('a'))
        except:
            # print "Unexpected error:", sys.exc_info()[0]
            return

def isRedirect(url):
    # redirect the link if it is under the same domain
    if domain == getDomain(url):
        print 'Redirecting URL with the same domain:' + url
        driver.get(url)
        findEmailAdress(url)

def getDomain(url):
    #  check if http or https
    if len(url) > 8:
        if url[:7] == 'http://':
            url = url[7:]
        if url[:8] == 'https://':
            url = url[8:]
    domain = url.split('/')[0];
    return domain
####################################################################################################
domain = ""
emailCounts = 0
redirectUrlSet = Set([])
clickableTagSet = Set([])
emailSet = Set([])
driver = webdriver.Firefox()
url = "http://jana.com"

# check if the typed url is valid
if len(sys.argv) > 1:
    try:
        if len(sys.argv[1]) > 8:
            if sys.argv[1][:7] == 'http://':
                url = sys.argv[1]
            elif sys.argv[1][:8] == 'https://':
                print sys.argv[1][:8]
                url = sys.argv[1]
            else:
                url = 'http://'+sys.argv[1]
        urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print(e.code)
        exit(1)
    except urllib2.URLError, e:
        print(e.args)
        exit(1)
    domain = getDomain(url)
    findEmailAdress(url)
    print emailCounts, ' email address found:'
    for email in emailSet:
        print email
else:
    print 'Arguments are not valid. Example: python find_email_addresses.py jana.com'

driver.close()