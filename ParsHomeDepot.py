from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path='/Users/vl/PycharmProjects/Parsing/chromedriver')
    # driver = webdriver.Chrome("/Users/vl/PycharmProjects/Parsing/chromedriver")
    qwe  = driver.get('https://www.homedepot.com/p/2-in-x-4-in-x-8-ft-Prime-Whitewood-Stud-058449/312528776')
    list = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[3]/div/div/div[6]/ul/li[1]')
    price = driver.find_element("list__item")
    print(qwe)




    # new_price = driver.find_element_b()
    # price2x4 = driver.find_element(new_price)
    # print(new_price)

if __name__ == "__main__":
    main()

#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver.get('https://www.homedepot.com/p/2-in-x-4-in-x-8-ft-Prime-Whitewood-Stud-058449/312528776')


# //*[@id="standard-price"]/div/div/span[2]
# /html/body/div[5]/div/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/div/div