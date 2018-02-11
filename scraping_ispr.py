from urllib.request import Request, urlopen


def scrape_ispr():
    base_url = r'https://www.ispr.gov.pk/front/main.asp?o=t-press_release&id='
    end_url = '&cat=army'
    index = 4010
    for index in range(1000, 4999):
        full_url = base_url + str(index) + end_url
        req = Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        print(webpage)


if __name__ == '__main__':
    scrape_ispr()
