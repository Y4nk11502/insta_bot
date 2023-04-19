# insta_bot
Este es un programa en Python que utiliza la biblioteca Selenium para automatizar acciones en la plataforma de Instagram. En particular, este bot da "me gusta" a las fotos de un hashtag y comenta cada 3-6 fotos con un comentario aleatorio.

Configuración
Antes de utilizar el bot, es necesario configurar el archivo de Python modificando los campos correspondientes al nombre de usuario y la contraseña de Instagram.

Para hacer esto, busca las líneas de código que contienen las siguientes variables:

username = driver.find_element(By.NAME, "username")
username.send_keys("AQUI PONES TU USUARIO")

password = driver.find_element(By.NAME, "password")
password.send_keys("AQUI PONES TU CONTRASEÑA")

Reemplaza "AQUI PONES TU USUARIO" con tu nombre de usuario de Instagram, y "AQUI PONES TU CONTRASEÑA" con tu contraseña.
