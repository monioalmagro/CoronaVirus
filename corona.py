from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path = "/home/almagro/Escritorio/Selenium/chromedriver")
driver.get("https://google.com/covid19-map/?hl=es-419")
time.sleep(5)


rows = len(driver.find_elements_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody/tr"))
col = len(driver.find_elements_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td"))

print(rows)
print(col)



for n in range(2 ,rows+1):
    for b in range(1,col+1):
        dato = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
        print(dato)
        print("esto es n:",n)
        print("esto es b:",b)
       

    print()
    
