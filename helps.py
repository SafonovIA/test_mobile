from selenium.webdriver.common.by import By

# Вспомогательный файл для поиска эллементов

# Поле "Username"
username_selector = (By.ID, "user-name")

# Поле "Password"
password_selector = (By.ID, "password")

# Кнопка "Login"
submit_selector = (By.ID, "login-button")

# Добавить товар в корзину
add_selector = (By.ID, "add-to-cart-sauce-labs-backpack")

# Кнопка корзины
cart_selector = (By.CLASS_NAME, "shopping_cart_link")

# Добавленый товар
product_selector = (By.ID, "item_4_title_link")

# Кнопка "checkout"
checkout_selector = (By.ID, "checkout")

# Поле "first name"
firstname_selector = (By.ID, "first-name")

# Поле "last name"
lastname_selector = (By.ID, "last-name")

# Поле "postal code"
postalcode_selector = (By.ID, "postal-code")

# Кнопка "continue"
continue_selector = (By.ID, "continue")

# Кнопка "finish"
finish_selector = (By.ID, "finish")

# Успешное выполнение
complite_selector = (By.ID, "checkout_complete_container")
