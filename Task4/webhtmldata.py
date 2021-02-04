from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/kamini/Desktop/Niyuj-Assign-new/drivers/chromedriver_linux64/chromedriver")

driver.get("file:///home/kamini/Desktop/Niyuj-Assign-new/Task4/Table.html")
driver.maximize_window()
driver.implicitly_wait(10)

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr")) #count no of rows

cols= len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/td"))

print(rows)
print(cols)
print("****************")
for r in range(1,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='   ')
    print()

driver.quit()
