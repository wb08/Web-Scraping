from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string
import csv

data=[]

class Avito:
    def __init__(self):
        with open('AUTO_HREF.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)

        new_list = []
        for sub_list in your_list:
            for el in sub_list:
                new_list.append(el)
        self.drifer=webdriver.Firefox()
        self.navidate(new_list)

    def take_sckrenshot(self):
        self.drifer.save_screenshot('avito.png')

    def rasposnavanie(self):
        image=Image.open('tel.gif')
        data.append(image_to_string(image))


    def write_csv(self,data):
        with open('list_to_csv.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for item in data:
                csv_writer.writerow([item])

    def crop(self,location,size):
        image=Image.open('avito.png')
        x=location['x']
        y=location['y']
        widht=size['width']
        height=size['height']
        image.crop((x,y,x+widht,y+height)).save('tel.gif')
        self.rasposnavanie()


    def navidate(self,new_list):
        dlina_url=len(new_list)
        dlina = 0
        while dlina<dlina_url:

            self.drifer.get(new_list[dlina])
            mashina_click = self.drifer.find_elements_by_xpath('//a[@class="js-item-slider item-slider"]')
            dlina_mashin_na_str = len(mashina_click)
            i = 0
            while i < dlina_mashin_na_str-1:
                self.drifer.execute_script("window.scrollTo(0, 120)")
                try:
                    mashina_click = self.drifer.find_elements_by_xpath('//a[@class="js-item-slider item-slider"]')[i]
                    mashina_click.click()
                except IndexError:
                    self.drifer.refresh()
                sleep(2)
                try:
                    button = self.drifer.find_element_by_xpath(
                        '//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
                    button.click()

                    sleep(3)

                    self.take_sckrenshot()
                    image = self.drifer.find_element_by_xpath(
                        '//div[@class="item-popup-content js-item-phone-popup-content"]//*')
                    location = image.location
                    size = image.size
                    self.crop(location, size)
                    self.write_csv(data)
                    self.drifer.back()
                    sleep(3)
                except:
                    self.drifer.back()

                if i == dlina_mashin_na_str-1:
                    i = 0
                    continue

                i += 1
            dlina+=1




def main():
    b=Avito()


if __name__=='__main__':
    main()
