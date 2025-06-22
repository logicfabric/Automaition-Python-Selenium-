from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import csv
import time


input_csv_path = '6500081466_table_data.csv'
input_csv_path_01 = '7500062485_table_data.csv'
output_csv_path = '6500081466_orders.csv'
output_csv_path_01 = '7500062485_orders.csv'

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/Achilles/AppData/Local/Google/Chrome/User Data")
options.add_argument("profile-directory=Default")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()

driver.get("https://secure.icicidirect.com/customer/login")

driver.set_window_size(1536, 816)

username = "sbiyani69" 
password = "tochange" 
# driver.find_element(By.ID, "txtu").send_keys(username)
driver.find_element(By.ID, "txtp").send_keys(password) 
driver.find_element(By.ID, "btnlogin").click()
try :
    driver.find_element(By.ID, "higootp").click()
except Exception as ex :
    print(ex)

# element_selector = "#pnlmnudsp > div:nth-child(1) > div > ul > li:nth-child(5) > a"
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_selector))).click()# Wait for the page to load
# time.sleep(2)

# driver.find_element(By.LINK_TEXT, "GTT").click()

# time.sleep(2)

# table_xpath = '/html/body/form/div[3]/div[3]/div/span/div[2]/div/div[2]/div/div/div[1]/form/div[2]/div[4]/div/div/div/div/table[2]'
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, table_xpath)))

# table = driver.find_element(By.XPATH, table_xpath)

# headers = table.find_elements(By.XPATH, './/thead/tr/th')
# header_list = [header.text for header in headers]

# rows = table.find_elements(By.XPATH, './/tbody/tr')
# row_data = []
# for row in rows:
#     columns = row.find_elements(By.XPATH, './/td')
#     row_list = [column.text for column in columns]
#     row_data.append(row_list)

# with open(input_csv_path, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(header_list) 
#     writer.writerows(row_data)   

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mrl10"))).click()

# Click on the second child element with class 'p-2' and 'fw-bold'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".p-2:nth-child(2) .fw-bold"))).click()

# # Move the mouse to the element with id 'drpAccount'
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "drpAccount")))
# ActionChains(driver).move_to_element(element).perform()

# # Click on the element with id 'drpAccount'
# element.click()

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="drpAccount"]"""))).click()

# # Click on the element with 
# # CSS class 'btn-short' and specific label attribute
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-short[label='IN303028-76957818-7500062485-NRO']"))).click()

dropdown_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "drpAccount")))
ActionChains(driver).move_to_element(dropdown_element).perform()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "drpAccount"))).click()

select = Select(dropdown_element)

select.select_by_value("IN303028-76957818-7500062485-NRO")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="pnlSelMDP"]/div[2]/input"""))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, """/html/body/form/div[3]/header/nav/div[1]/div[3]/div[1]/div/ul/li[5]/a"""))).click()# Wait for the page to load
time.sleep(2)

driver.find_element(By.LINK_TEXT, "GTT").click()

time.sleep(2)

table_xpath = '/html/body/form/div[3]/div[3]/div/span/div[2]/div/div[2]/div/div/div[1]/form/div[2]/div[4]/div/div/div/div/table[2]'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, table_xpath)))

table = driver.find_element(By.XPATH, table_xpath)

headers = table.find_elements(By.XPATH, './/thead/tr/th')
header_list = [header.text for header in headers]

rows = table.find_elements(By.XPATH, './/tbody/tr')
row_data = []
for row in rows:
    columns = row.find_elements(By.XPATH, './/td')
    row_list = [column.text for column in columns]
    row_data.append(row_list)

with open(input_csv_path_01, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header_list) 
    writer.writerows(row_data)   


driver.quit()



def clean_stock_column(value):
    cleaned_value = value.strip().replace(" ", "")
    cleaned_value = cleaned_value.replace("SINGLE", "")
    return cleaned_value
with open(input_csv_path, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    headers = next(reader)
    stock_index = headers.index('Stock')

    rows = []
    for row in reader:
        row[stock_index] = clean_stock_column(row[stock_index])

        if any(cell.strip() for cell in row):
            rows.append(row)

with open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers) 
    writer.writerows(rows)   


with open(input_csv_path_01, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    headers = next(reader)
    stock_index = headers.index('Stock')

    rows = []
    for row in reader:
        row[stock_index] = clean_stock_column(row[stock_index])

        if any(cell.strip() for cell in row):
            rows.append(row)

with open(output_csv_path_01, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers) 
    writer.writerows(rows)   

print(f"Processed CSV saved to {output_csv_path}")
