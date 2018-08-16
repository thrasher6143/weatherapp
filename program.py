import requests


def main():
    print_the_header()

    code = input('What zipcode are you in? (e. g. 90210) ')

    get_html_from_web(code)

    # parse the html
    # display for the forecast


def print_the_header():
    print('==============================')
    print('       WEATHER APP   ')
    print('==============================')
    print()


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    print(response.status_code)



if __name__ == '__main__':
    main()