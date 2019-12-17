from selenium import webdriver
from selenium.webdriver.firefox.options import Options
firefox_options = Options()
team_one = ("Everton")
team_two = ("Arsenal")


firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument('window-size=1920x1080')


driver_path = ("c:/Users/Johan/Webdrivers/geckodriver")
driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)

def Bet365_main():
    global Bet365Odds1
    global Bet365OddsX
    global Bet365Odds2

    URL = ('https://www.bet365.com/#/HO/')
    driver.get(URL)

    driver.implicitly_wait(3)
    select_search = driver.find_element_by_css_selector('.sml-SearchTextInput')
    select_search.click()
    select_search.send_keys(team_one+" "+team_two)
    search_result = driver.find_element_by_css_selector('div.ssm-SiteSearchTextHeaderMarketGroup:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    odds1 = driver.find_element_by_css_selector('div.ssm-SiteSearchTextHeaderMarketGroup:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)')
    tie = driver.find_element_by_css_selector('div.ssm-SiteSearchTextHeaderMarketGroup:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > span:nth-child(2)')
    odds2 = driver.find_element_by_css_selector('div.ssm-SiteSearchTextHeaderMarketGroup:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > span:nth-child(2)')
    if (team_one + " ") in search_result.text:

        Bet365Odds1 = (team_one, odds1.text)
        Bet365OddsX = ("Tie", tie.text)
        Bet365Odds2 = (team_two, odds2.text)

    elif(" " + team_one) in search_result.text:

        Bet365Odds1 = (team_one, odds2.text)
        Bet365OddsX = ("Tie", tie.text)
        Bet365Odds2 = (team_two, odds1.text)
    print("Bet365:")
    print("".join(str(Bet365Odds1).replace("'", "").strip("([])").replace(",", "")))
    print("".join(str(Bet365OddsX).replace("'", "").strip("([])").replace(",", "")))
    print("".join(str(Bet365Odds2).replace("'", "").strip("([])").replace(",", "")))



