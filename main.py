import msedgedriver_64
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time


def main():
    print('Testing MSEdgeDriver python library...')
    msedgedriver_64.install()

    edge_service = Service(executable_path='msedgedriver.exe')
    Driver = webdriver.Edge(service=edge_service)

    Driver.get("https://google.com")
    time.sleep(5)

    Driver.quit()
    print('Done.')


if __name__ == '__main__':
    main()