from sys import argv
from pyquery import PyQuery as pq
from statistics import median

def get_price(term):
  term_escaped = term.replace(" ", "-")
  html = pq("https://www.ebay.de/sch/i.html?_odkw=" + term_escaped + "&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR12.TRC2.A0.H0.TRS0&_nkw=" + term_escaped + "&_sacat=0&_udlo=30&_udhi&LH_BIN=1")
  prices = []
  for itm in html.find(".lvprice > span"):
    try:
      prices.append(float(list(itm.itertext())[2].strip().replace(",", ".")))
    except:
      pass
  try:
    return median(prices[0:5])
  except:
    return -1

if __name__ == "__main__":
  print(get_price(argv[1]))

