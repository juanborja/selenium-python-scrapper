from selenium.webdriver import Chrome
import pandas as pd

webdriver = "/home/juan/Proyectos/scrapping/71/chromedriver"

driver = Chrome(webdriver)
url = "https://www.clarin.com/sociedad/"
driver.get(url)
items = len(driver.find_elements_by_tag_name("article"))

total = []
for item in range(items):
    quotes = driver.find_elements_by_tag_name("article")
    for quote in quotes:
        #quote_text = quote.find_element_by_class_name('summary').text
        quote_text = "casa"
        author = driver.find_elements_by_class_name("fecha")[0].text
        new = ((quote_text,author))
        total.append(new)
    df = pd.DataFrame(total,columns=['quote','author'])
    df.to_csv('resumen.csv')
driver.close()