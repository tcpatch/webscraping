from urllib.request import Request, urlopen
import re

def scrape_ispr():
    #This function scrapes the ispr website and if the word missile is in the raw HTML the url will be printed
    base_url = r'https://www.ispr.gov.pk/front/main.asp?o=t-press_release&cat=army&date='
    years = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    for year in years:
        for month in months:
            for day in days:
                try:
                    full_url = base_url + str(year) + r'/' + str(month) + r'/' + str(day)
                    req = Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
                    webpage = urlopen(req).read()
                    content = str(webpage)
                    if 'missile' in content:
                        print(full_url)
                except:
                    pass
#                if len(webpage) > 0:
#                    with open(str(year) + str(month) + str(day) + '.txt', 'a') as fp:
#                        fp.write(webpage.encode('utf-8') + '\n')


if __name__ == '__main__':
    scrape_ispr()
