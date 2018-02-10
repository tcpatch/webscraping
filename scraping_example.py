from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def open_driver():
    # driver_dir is the pointer to where the chromedriver is located
    driver_dir = 'chromedriver.exe'
    # open a new chrome webdriver to be returned
    driver = webdriver.Chrome(executable_path=driver_dir)
    return driver

def hold_up(driver, url):
    '''
    :param selenium.webdriver.chrome.webdriver.WebDriver driver: The webdriver making the GET request
    :param str url: the xpath to the unique element of the page to wait for
    :return: nothing
    '''
    # driver is not used but can be used to direct the script to handle errors if needed
    delay = 2
    try:
        myElem = WebDriverWait(browser, delay).until(ec.presence_of_element_located((By.XPATH, url)))
    except:
        # add error handling
        pass


if __name__ == '__main__':
    # This script outlines generates urls following the nomenclature of the nba website
    # (e.g. https://stats.nba.com/game/0011700014/playbyplay/) for total number of games in each season as contained in
    # the file 'year_totalgames.txt' (not provided).
    # TODO make a template with common commands for using selenium as a webscraping tool

    # base_url, preseason, and end_url variables outline the format of the url to be searched
    base_url = r'https://stats.nba.com/game/'
    preseason = '002'
    end_url = '/playbyplay/'
    # open a selenium webdriver
    driver = open_driver()
    # read the file (tab delimited) containing the year and number of NBA games played
    with open('year_totalgames.txt', 'r') as fp:
        for line in reversed(fp.readlines()):
            # each line holds first the year and the corresponding number of games played
            holder = line.split('\t')
            year = holder[0]
            total_games = holder[1]
            counter = int(total_games)
            #start at the last game and go down 1 game to make each url
            while counter > 1:
                # construct the url of the game
                current_game = str(counter)
                current_game = (5 - len(current_game))*'0' + current_game + end_url
                url = base_url + preseason + year + current_game
                # connect to the url
                driver.get(url)
                # wait until the driver has connected
                hold_up(driver, url)
                try:
                    # find the table containing the scores
                    score_table = driver.find_elements_by_tag_name('tr')
                    # write each row/cell of the table to a text file
                    # there are alternative ways of storing/parsing data, this was a simple way to write the data
                    with open('results.txt', 'a') as w:
                        w.write(url + '\n')
                        for row in score_table:
                            td = row.find_elements_by_tag_name('td')
                            for cell in td:
                                write_cell = cell.text
                                w.write(write_cell.encode('utf-8') + '\t')
                            w.write('\n')
                except:
                    # Deal with any page not loaded correctly or missing information
                    # e.g. write missed url to a separate file for later analysis or write whole web page to a text file
                    # to parse with beautiful soup later or write directly to a database etc...
                    pass
                # decrease the counter by one to get to the next game of that year
                counter -= 1
