from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import itertools
import sys
from database_connection import create_connection
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

extension_path = './Captcha-Solver.crx'
spinner = itertools.cycle(['-', '/', '|', '\\'])


def read_address_from_database(connection, current_row):
    cursor = connection.cursor()
    cursor.execute("SELECT address FROM addresses WHERE id = %s", (current_row,))
    result = cursor.fetchone()

    if result:
        address = result[0]
    else:
        address = None

    return address


def mark_address_as_activated(connection, current_row):
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE addresses SET activated = true WHERE id = %s", (current_row,))
        connection.commit()
    finally:
        if cursor:
            cursor.close()


def mark_address_as_error(connection, current_row):
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE addresses SET activated = 2 WHERE id = %s", (current_row,))
        connection.commit()
    finally:
        if cursor:
            cursor.close()


counter = 0
current_row = 338  # Assuming your database starts indexing from 1

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension(extension_path)
service_obj = Service("C:\\Users\\laimer\\Desktop\\pythonDr\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get('https://testnet.bnbchain.org/faucet-smart')

database_connection = create_connection()

try:
    while True:
        address = read_address_from_database(database_connection, current_row)

        if not address:
            # If no more addresses are available in the database, break out of the loop
            break

        try:
            try:
                captcha_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "captcha-solver_inner"))
                )
                print("Captcha element found")
                captcha_element.click()
            except TimeoutException:
                print('Captcha element not found within 15 seconds!')
                driver.execute_script("location.reload(true);")
            else:
                # Your code for when the element is found
                pass

            frstInpt = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='url']"))
            )
            print("Input element found")
            frstInpt.send_keys(address)

            btn = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-toggle"))
            )
            print("Button element found")
            btn.click()

            element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='0.3 BNBs']"))
            )
            print("Dropdown option found")
            element.click()

            noty_success = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "noty_type_success"))
            )

            if noty_success:
                mark_address_as_activated(database_connection, current_row)

                counter += 1
                current_row += 1
                print(f"All done! Count: {counter}")
                print("Success Notify")
                driver.execute_script("location.reload();")
                print("iframe detected")
            else:
                noty_error = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "noty_type_error"))
                )

                if noty_error:
                    mark_address_as_error(database_connection, current_row)

                    counter += 1
                    current_row += 1
                    print("skip...")

        except TimeoutException as te:
            print(f"Timed out waiting for an element: {te}")
        except StaleElementReferenceException as se:
            print(f"Stale element reference: {se}")
        except Exception as e:
            print(f"Unexpected error: {e}")

except Exception as ex:
    print(f"An unexpected error occurred outside the loop: {ex}")

action_chains = ActionChains(driver)
action_chains.key_down(Keys.CONTROL).send_keys("r").key_up(Keys.CONTROL).perform()

print(f"Repeating...")
