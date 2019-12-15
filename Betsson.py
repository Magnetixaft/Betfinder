from selenium import webdriver
from selenium.webdriver.firefox.options import Options
firefox_options = Options()
team_one = ("Inter")
team_two = ("Fiorentina")


firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument('window-size=1920x1080')


driver_path = ("c:/Users/Johan/Webdrivers/geckodriver")
driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)


URL = ('https://www.betsson.com/sv/odds/')
driver.get(URL)
print(driver.title)
driver.implicitly_wait(1)
search_click = driver.find_element_by_css_selector('body > app-root > obg-m-sportsbook-layout-container > obg-m-sidenav > mat-toolbar-row > div > obg-m-sportsbook-search-input-container > obg-m-sportsbook-search-input > button > span')
search_click.click()
search_bar = driver.find_element_by_css_selector('#mat-input-0')
search_bar.send_keys(team_one)
driver.implicitly_wait(3)
search_result_first = driver.find_element_by_css_selector('#mat-option-0 > span:nth-child(1) > div:nth-child(2) > div:nth-child(2)')
search_result_first.click()
search_result_first_match = driver.find_element_by_css_selector('obg-m-sportsbook-search-result-event.obg-m-sportsbook-search-result-event:nth-child(2)')
search_result_second_match = driver.find_element_by_css_selector('obg-m-sportsbook-search-result-event.obg-m-sportsbook-search-result-event:nth-child(3)')
search_result_third_match = driver.find_element_by_css_selector('obg-m-sportsbook-search-result-event.obg-m-sportsbook-search-result-event:nth-child(4)')
driver.implicitly_wait(1)




try:
    if team_two in search_result_first_match.text:
        print("1")
        search_result_first_match.click()
        search_result_first_match_result1 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(1) > div:nth-child(1)')
        search_result_first_match_result2 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(3) > div:nth-child(1)')
        odds1 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(1) > div:nth-child(1) > obg-numeric-change:nth-child(2) > span:nth-child(1)')
        tie = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(2) > div:nth-child(1) > obg-numeric-change:nth-child(2) > span:nth-child(1)')
        odds2 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(3) > div:nth-child(1) > obg-numeric-change:nth-child(2) > span:nth-child(1)')

        if (team_one) in search_result_first_match_result1.text:
            print(team_one, ": ", odds1.text)
            print("Tie: ", tie.text)
            print(team_two, ": ", odds2.text)

        elif (team_one) in search_result_first_match_result2.text:
            print(team_two, ": ", odds1.text)
            print("Tie: ", tie.text)
            print(team_one, ": ", odds2.text)
except Exception:
    pass
try:
    if (team_two) in search_result_second_match.text:
        print("2")
        driver.implicitly_driver.implicitly_wait(1)(2)
        search_result_second_match.click()
        search_result_second_match_result1 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(1) > div:nth-child(1)')
        search_result_second_match_result2 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(3) > div:nth-child(1)')
        odds1 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(1) > div:nth-child(1) > obg-numeric-change:nth-child(2) > span:nth-child(1)')
        tie = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(2) > div:nth-child(1) > obg-numeric-change:nth-child(2) > span:nth-child(1)')
        odds2 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(3) > div:nth-child(1) > obg-numeric-change:nth-child(2) > span:nth-child(1)')
        if (team_one) in search_result_second_match_result1.text:
            print(team_one, ": ", odds1.text)
            print("Tie: ", tie.text)
            print(team_two, ": ", odds2.text)


        if (team_one) in search_result_second_match_result2.text:
            print(team_two, ": ", odds2.text)
            print("Tie: ", tie.text)
            print(team_one, ": ", odds1.text)
except Exception:
    pass
try:
    if team_two in search_result_third_match.text:
        print("3")
        search_result_third_match.click()
        search_result_third_match_result1 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(1) > div:nth-child(1)')
        search_result_third_match_result2 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(3) > div:nth-child(1)')
        odds1 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(1) > div:nth-child(1) > obg-numeric-change:nth-child(2) > span:nth-child(1)')
        tie = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(2) > div:nth-child(1) > obg-numeric-change:nth-child(2) > span:nth-child(1)')
        odds2 = driver.find_element_by_css_selector('obg-event-market-group.obg-event-market-group:nth-child(1) > obg-accordion-content:nth-child(2) > div:nth-child(1) > div:nth-child(1) > obg-selection-container:nth-child(3) > div:nth-child(1) > obg-numeric-change:nth-child(2) > span:nth-child(1)')

        if (team_one) in search_result_third_match_result1.text:
            print(team_one, ": ", odds1.text)
            print("Tie: ", tie.text)
            print(team_two, ": ", odds2.text)

        if (team_one) in search_result_third_match_result2.text:
            print(team_two, ": ", odds2.text)
            print("Tie: ", tie.text)
            print(team_one, ": ", odds1.text)
except Exception:
    pass
