# libraries
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from multiprocessing.pool import ThreadPool
import threading

# variables
url = "https://eldorado.ua/"
directory = os.path.dirname(os.path.realpath(__file__))
print('test directory ', directory)
env_path = directory + "\chromedriver"
chromedriver_path = env_path + "\chromedriver.exe"
UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 " \
            "Safari/537.36 "
dict1 = {"Смартфоны и телефоны": "https://eldorado.ua/node/c1038944/",
         "Телевизоры и аудиотехника": "https://eldorado.ua/node/c1038957/",
         "Ноутбуки, ПК и Планшеты": "https://eldorado.ua/node/c1038958/",
         "Техника для кухни": "https://eldorado.ua/node/c1088594/",
         "Техника для дома": "https://eldorado.ua/node/c1088603/",
         "Игровая зона": "https://eldorado.ua/node/c1285101/",
         "Гаджеты и аксесуары": "https://eldorado.ua/node/c1215257/",
         "Посуда": "https://eldorado.ua/node/c1039055/",
         "Фото и видео": "https://eldorado.ua/node/c1038960/",
         "Красота и здоровье": "https://eldorado.ua/node/c1178596/",
         "Авто и инструменты": "https://eldorado.ua/node/c1284654/",
         "Спорт и туризм": "https://eldorado.ua/node/c1218544/",
         "Товары для дома и сада": "https://eldorado.ua/node/c1285161/",
         "Товары для детей": "https://eldorado.ua/node/c1085100/"}
count = 0
threaded_data = threading.local()  # Создаёт хранилище (класс) для потоков, чтобы не вызывать webdriver при каждой итерации
os.environ['PATH'] += env_path  # Добавляет chromedriver в PATH


class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_argument(f'--user-agent={UserAgent}')
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    def __del__(self):
        self.driver.quit()  # driver.quit(), когда переменная больше не используется (при окончании выполнения потока)
        print('The driver has been quited.')


def create_driver():
    the_driver = getattr(threaded_data, 'the_driver', None)
    if the_driver is None:
        the_driver = Driver()
        setattr(threaded_data, 'the_driver', the_driver)
    return the_driver.driver


def processing_brand_pages(name):
    with open(f"{directory}\section_pages\\{name}.html", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "lxml")
    links = soup.find_all("div", class_="title")
    driver = create_driver()
    for n in links:
        ref = url + n.find('a').get('href')
        global count
        print(n.text, count)
        count += 1
        driver.get(ref)
        try:
            with open(f"{directory}\\brand_pages\\{name}\\{n.text}.html", "w", encoding="utf-8") as file:
                file.write(driver.page_source)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    #ThreadPool(processes=6).map(processing_brand_pages, dict1.keys())
    
    with ThreadPool(processes=6) as pool:
        pool.map(processing_brand_pages, dict1.keys())
    del threaded_data  # Quit all the Selenium drivers
    import gc
    gc.collect()
    
    # https://stackoverflow.com/questions/70025698/when-i-use-threadpool-the-program-waits-after-completion-before-closing