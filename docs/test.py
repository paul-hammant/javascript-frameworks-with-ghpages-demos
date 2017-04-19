import selenium.webdriver as webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(30)

browser.get("https://paulhammant.com/2016/12/11/permissions-for-composite-in-house-webapps/")
elems = browser.find_elements_by_partial_link_text("example")
for elem in elems:
    print(elem.get_attribute("href"))