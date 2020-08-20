import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore


class Browser:
    def __init__(self):
        self.visited_sites = deque()
        self.dir_name = sys.argv[1]

        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)

    @staticmethod
    def parsing(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        text_list = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])

        text = ""
        for item in text_list:
            text += Fore.BLUE + item.text + '\n' if '</a>' in str(item) else item.text + '\n'

        return text

    def get_content(self, url):
        if not url.startswith("https://"):
            url = "https://" + url

        try:
            with open(f"{self.dir_name}/{url[8:]}.txt", 'r') as data:
                self.visited_sites.append(url[8:])
                return data.read()
        except FileNotFoundError:
            try:
                text = Browser.parsing(url)
                with open(f"{self.dir_name}/{url[8:url.rfind('.')] if url.rfind('.') != -1 else url[8:]}.txt", 'w') as data:
                    data.write(text)
                    self.visited_sites.append(url[8:url.rindex('.')])
                    return text
            except requests.exceptions.ConnectionError:
                return "Error: Incorrect URL"

    def command_processing(self, command):
        if command == "exit":
            exit()
        elif command == "back":
            self.visited_sites.pop()
            prev_site = self.visited_sites.pop()
            with open(prev_site, 'r') as data:
                print(data.read())
        else:
            print(self.get_content(command))


browser = Browser()

while True:
    new_command = input('>')
    browser.command_processing(new_command)
