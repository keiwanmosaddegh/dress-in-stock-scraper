import os
from selenium import webdriver

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=op)
driver.get("https://www.stories.com/en_sek/clothing/dresses/mini-dresses/product.sheer-leopard-jacquard-mini-dress-black.0793274001.html")

sizes = driver.find_element_by_id('sizes')

size_options = sizes.find_elements_by_class_name('size-options')

for size_option in size_options:
    if (size_option.get_attribute('data-value') == '34'):
        print("Size 34 found!")
        if 'is-sold-out' in size_option.get_attribute('class'):
            print("Size 34 is sold out!")
        else:
            print("Size 34 is in stock!")

driver.close()
