from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ITEM_DESCRIPTION = (By.CSS_SELECTOR, "#product_description + p")
    ITEM_DESCRIPTION_HEADER = (By.CSS_SELECTOR, "#product_description")
    ITEM_DESCRIPTION_CONTENT = (By.CSS_SELECTOR, "#product_description + p")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ITEM_NAME_IN_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ITEM_PRICE_IN_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CART_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-mini > strong")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")

    SUCCESS_ITEM_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_ITEM_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")

    ANSWER = (By.CSS_SELECTOR, "#input_value")
    INPUT_FIELD = (By.CSS_SELECTOR, "#answer")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
