from urllib.request import Request, urlopen


def scrape_ispr():
    #This function scrapes the ispr website and saves the raw HTML to a text file for future processing
    base_url = r'https://www.ispr.gov.pk/front/main.asp?o=t-press_release&cat=army&date='
    years = ['2008', '2009']
    months = ['1', '2']
    days = ['1', '2']
    for year in years:
        for month in months:
            for day in days:
                full_url = base_url + str(year) + r'/' + str(month) + r'/' + str(day)
                req = Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
                if len(webpage) > 0:
                    with open(str(year) + str(month) + str(day) + '.txt', 'a') as fp:
                        fp.write(webpage.encode('utf-8') + '\n')


if __name__ == '__main__':
    scrape_ispr()
