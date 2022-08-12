import contextlib
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# function that takes a list of strings and adds an extension to each string
def add_extension(lst, ext):
    return [item + ext for item in lst]


def profile_search(
    name,
    remote_url="http://54.36.177.119:4450",
    credentials={"email": "interndata@mailfence.com", "password": "AbdoAbdo123@"},
):
    try:
        results_users = []
        results_descriptions = []
        users = []
        descriptions = []

        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)

        driver.get("https://www.tumblr.com/login")
        time.sleep(5)

        username = driver.find_element_by_name("email")
        username.send_keys(credentials["email"])

        password = driver.find_element_by_name("password")
        password.send_keys(credentials["password"])

        driver.find_element_by_class_name("EvhBA").click()
        time.sleep(3)

        url = f"https://www.tumblr.com/search/{name}?v=blog"
        driver.get(url)

        for _ in range(4):
            with contextlib.suppress(Exception):
                # Appending the results of the search to the list `results_users` and then it is extending the list `users` with the text of the results.
                results_users.append(driver.find_elements_by_class_name("UulOO"))
                users.extend(user.text for user in results_users[-1])

                # Appending the results of the search to the list `results_descriptions` and then it is extending the list `descriptions` with the text of the results.
                results_descriptions.append(driver.find_elements_by_class_name("fTJAC"))
                descriptions.extend(
                    description.text for description in results_descriptions[-1]
                )

                # Clicking on the "Afficher plus de blogs" button.
                driver.find_element_by_xpath(
                    "//span[normalize-space()='Afficher plus de blogs']"
                ).click()
                time.sleep(1)

            urls = add_extension(users, ".tumblr.com")
            keys = [f"profile {str(index+1)}" for index, _ in enumerate(urls)]
            values = [
                [user, description, url]
                for user, description, url in zip(users, descriptions, urls)
            ]

        driver.quit()

        # build a dictionary from the list of keys and values
        return dict(zip(keys, values))

    except Exception as e:
        print(f"An error has occurred {e}")
        if driver:
            driver.quit()


