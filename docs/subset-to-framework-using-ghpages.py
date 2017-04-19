import json
import selenium.webdriver as webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException, UnexpectedAlertPresentException
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urlparse


raw = open("search_results.json").read().strip()[:-1]
resultsString = "{ \"res\": [" + raw + "] }"
results = json.loads(resultsString)

last_repo = ""
last_org_person = ""

if os.path.exists('not-these.txt'):
    not_these = [line.rstrip('\n') for line in open('not-these.txt')]
else:
    not_these = []

if os.path.exists('permban.csv'):
    permaban = [line.rstrip('\n') for line in open('permban.csv')]
else:
    permaban = []

browser = webdriver.Chrome()
browser.implicitly_wait(30)


def try_this():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    if "/404.html\"" not in browser.page_source \
            and "<title>Site not found &middot; GitHub Pages</title>" not in browser.page_source:
        scripts = soup.find_all("script")
        for script in scripts:
            if script.has_attr("src"):
                if framework in script["src"] and "/node_modules" not in script["src"]:

                    if "angular" in framework:
                        try:
                            ng_version = browser.execute_script('return window.angular.version.full')
                            if ng_version.startswith("1."):
                                result['framework'] = "AngularJS"
                            else:
                                result['framework'] = "Angular"
                            result['framework_version'] = ng_version
                        except WebDriverException:
                            pass

                    if not os.path.exists(results_dir):
                        os.makedirs(results_dir)

                    with open(results_dir + "/" + repo + '.indexDotHtmlAs.txt', 'a') as index_file:
                        index_file.truncate()
                        index_file.write(str(soup.prettify().encode('utf-8')))

                    if os.path.exists(image_filename):
                        os.remove(image_filename)
                    browser.save_screenshot(image_filename)
                    return True

    return False


def get_hrefs(word):

    goes = []
    goes.append(word)
    goes.append(word.lower())
    for go in goes:
        for elem in browser.find_elements_by_partial_link_text(go):
            href = elem.get_attribute("href")
            if href is None or href.startswith("..") or "javascript:" in href or href.strip() is "":
                continue
            domain_part = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(current_url))
            if not href.startswith(domain_part) and "http" in href:
                continue
            hrefs.append(href)


for result in results['res']:

    org_or_person = result['orgOrPerson']
    repo = result['repo']

    org_person_repo = org_or_person + "/" + repo
    if org_person_repo in not_these or org_person_repo in permaban:
        continue

    framework =  result['framework'].lower()

    if repo is last_repo and org_or_person is last_org_person:
        continue
    last_repo = repo
    last_org_person = org_or_person

    if repo in org_or_person + ".github.io":
        url = "http://" + org_or_person + ".github.io/index.html" # may do redirects
    else:
        url = "http://" + org_or_person + ".github.io/" + repo + "/index.html" # may do redirects

    print("processing " + url)

    results_dir = "results/" + org_or_person

    # to delete
    image_filename = results_dir + "/" + repo + '.png'
    if os.path.exists(image_filename):
        continue

    browser.get("http://www.this-page-intentionally-left-blank.org/")
    matched = False
    try:
        browser.get(url)
        time.sleep(2)

        matched = try_this()

        current_url = browser.current_url

        if not matched:
            browser.implicitly_wait(0)
            hrefs = []
            get_hrefs("Example")
            get_hrefs("Demo")
            get_hrefs("Sample")
            browser.implicitly_wait(30)

            if len(hrefs) > 0:
                for href in hrefs:
                    browser.get(href)
                    matched = try_this()
                    time.sleep(2)
                    if matched:
                        result["inChildPage"] = True
                        break

    except (TimeoutException, UnexpectedAlertPresentException) as e:
        pass

    if not matched:
        open('not-these.txt', 'a').write(org_or_person + "/" + repo + "\n")
    else:
        open(result['framework'] + '-gh-pages.txt', 'a').write(json.dumps(result) + ",\n")

browser.quit()