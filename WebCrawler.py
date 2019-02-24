import requests
from bs4 import BeautifulSoup


def crawler(url):
    top100 = dict()
    source_code = requests.get(url)
    str_sc = source_code.text
    soup = BeautifulSoup(str_sc, features="html.parser")

    for link in soup.findAll('div', {'class':'chart-number-one__details'}):
        top100['1'] = [link.findAll('div', {'class': 'chart-number-one__title'})[0].string.strip()]
        if len(link.findAll('div', {'class': 'chart-number-one__artist'})[0].findAll('a'))==0:
            top100['1'] += [link.findAll('div', {'class': 'chart-number-one__artist'})[0].string.strip()]
        else:
            top100['1'] += [link.findAll('div', {'class': 'chart-number-one__artist'})[0].findAll('a')[0].string.strip()]

    for link in soup.findAll('div', {'data-has-content': 'true'}):
        top100[link.get('data-rank')] = [link.get('data-title').strip(), link.get('data-artist').strip()]

    return top100


# HOT 100 CHART
with open("top_HOT.txt","w") as hot:
    hot100 = r"https://www.billboard.com/charts/hot-100"
    hot100_dict = crawler(hot100)
    for k in hot100_dict.keys():
        hot.write("%d\t%s - %s\n" % (int(k), str(hot100_dict[k][0]), str(hot100_dict[k][1])))

# TOP COUNTRY HITS
with open("top_COUNTRY.txt", "w") as country:
    country50 = r"https://www.billboard.com/charts/country-songs"
    country50_dict = crawler(country50)
    for k in country50_dict.keys():
        country.write("%d\t%s - %s\n" % (int(k), str(country50_dict[k][0]), str(country50_dict[k][1])))

# TOP ROCK HITS
with open("top_ROCK.txt","w") as rock:
    rock50 = r"https://www.billboard.com/charts/rock-songs"
    rock50_dict = crawler(rock50)
    for k in rock50_dict.keys():
        rock.write("%d\t%s - %s\n" % (int(k), str(rock50_dict[k][0]), str(rock50_dict[k][1])))

# TOP POP HITS
with open("top_POP.txt","w") as pop:
    pop50 = r"https://www.billboard.com/charts/pop-songs"
    pop50_dict = crawler(pop50)
    for k in pop50_dict.keys():
        pop.write("%d\t%s - %s\n" % (int(k), str(pop50_dict[k][0]), str(pop50_dict[k][1])))

# TOP DANCE HITS
with open("top_DANCE.txt","w") as dance:
    dance50 = r"https://www.billboard.com/charts/dance-electronic-songs"
    dance50_dict = crawler(dance50)
    for k in dance50_dict.keys():
        dance.write("%d\t%s - %s\n" % (int(k), str(dance50_dict[k][0]), str(dance50_dict[k][1])))