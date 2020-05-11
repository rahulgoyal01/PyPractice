from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

# this object reprsent introduction element on the page.
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
elem.click()

#to search in a search field
searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()

#control browser action
browser.back()
browser.forward()
browser.refresh()
browser.quit()
