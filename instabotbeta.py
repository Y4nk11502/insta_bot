#Bot de instagram que da like a las fotos de un hashtag 
# y comenta cada 3 - 6 fotos con un comentario aleatorio

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

#Configuracion del driver
driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(10)

# Establecer el tamaño de la ventana
driver.set_window_size(800, 600)  # Ancho: 800px, Alto: 600px

#Pagina de inicio de sesion
sleep(1)
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
sleep(2)

#Aceptar cookies
"""
sleep(1)
option = 'button[class="_a9-- _a9_1"]'
button_cookies = driver.find_element(By.CSS_SELECTOR, option).click()
sleep(2)
"""

#Iniciar sesion
username = driver.find_element(By.NAME, "username")
username.send_keys("AQUI PONES TU USUARIO")
sleep(1)

password = driver.find_element(By.NAME, "password")
password.send_keys("AQUI PONES TU CONTRASEÑA")
sleep(1)

password.send_keys(Keys.ENTER)
sleep(5)
print("Inicio de sesion exitoso")

driver.implicitly_wait(10)
#Hashtag a buscar
# ...
hashtag_list = ['cuban', 'cubano', 'gymbro', 'like4like','likeforlike', 'followforfollow', 'follow4follow', 'followme', 'followback', 'follow', 'follo']

for hashtag in hashtag_list:
    driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    print("Hashtag: " + hashtag + " cargado")
    sleep(10)

    #Abrir la primera foto
    first_photo_css = 'div[class="_aagu"]'
    wait = WebDriverWait(driver, 10)
    first_photo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, first_photo_css)))
    first_photo.click()
    print("Primera foto abierta")
    sleep(5)

    #Iterar a través de 16 fotos y dar "me gusta"
    for i in range(70):
        like_button_xpath = '//button[./div[1]/*[name()="svg" and @aria-label="Me gusta"]]'
        wait = WebDriverWait(driver, 20)
        like_button = wait.until(EC.element_to_be_clickable((By.XPATH, like_button_xpath)))
        like_button.click()
        print("Foto " + str(i + 1) + " le gusta")
        sleep(4)

        # Si no estamos en la última foto, pasar a la siguiente
        if i < 69:
            next_button_xpath = '//div[@class=" _aaqg _aaqh"]/button'
            next_button = driver.find_element(By.XPATH, next_button_xpath)
            next_button.click()
            sleep(random.randint(4, 15))
            print("Siguiente foto")

    sleep(5)
# ...
