from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import openpyxl
import itertools, sys

extension_path = './Captcha-Solver.crx'
excel_file_path = './addresses.xlsx'
spinner = itertools.cycle(['-', '/', '|', '\\'])

def read_address_from_excel(file_path, row):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    address_cell = sheet.cell(row=row, column=1)  # Assuming the addresses are in column A

    address = address_cell.value
    workbook.close()

    return address

counter = 0
current_row = 2  # Start from the second row in Excel

# Create Chrome options and WebDriver instance outside the loop
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension(extension_path)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

# Open the website outside the loop
driver.get('https://testnet.bnbchain.org/faucet-smart')

try:
    while True:
        # Read address from Excel file for the current row
        address = read_address_from_excel(excel_file_path, current_row)

        try:
            print("Before waiting for captcha element")
            # Wait for the captcha-solver_inner element to be visible
            captcha_element = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "captcha-solver_inner"))
            )
            print("Captcha element found")
            captcha_element.click()

            # Wait for the input element to be present
            frstInpt = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='url']"))
            )
            print("Input element found")
            frstInpt.send_keys(address)
            
            # Wait for the button element to be present
            btn = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dropdown-toggle"))
            )
            print("Button element found")
            btn.click()

            # Wait for the dropdown option to be present
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='0.3 BNBs']"))
            )
            print("Dropdown option found")
            element.click()

            # Increment the counter and move to the next row in Excel
            counter += 1
            current_row += 1
            print(f"All done! Count: {counter}")

        except TimeoutException as te:
            print(f"Timed out waiting for an element: {te}")

        except StaleElementReferenceException as se:
            print(f"Stale element reference: {se}")

        except Exception as e:
            while True:
                sys.stdout.write(next(spinner))   # write the next character
                sys.stdout.flush()                # flush stdout buffer (actual character display)
                sys.stdout.write('\b')            # erase the last written char

finally:
    # Close the browser after the loop finishes
    driver.quit()
    print(f"Closing the browser...")
