## Insta_bot 
Este es un programa en Python que utiliza la biblioteca Selenium para automatizar acciones en la plataforma de Instagram. En particular, este bot da "me gusta" a las fotos de un hashtag y comenta cada 3-6 fotos con un comentario aleatorio.

Configuración
Antes de utilizar el bot, es necesario configurar el archivo de Python modificando los campos correspondientes al nombre de usuario y la contraseña de Instagram.

Para hacer esto, busca las líneas de código que contienen las siguientes variables:
```python
username = driver.find_element(By.NAME, "username")
username.send_keys("AQUI PONES TU USUARIO")
```
```python
password = driver.find_element(By.NAME, "password")
password.send_keys("AQUI PONES TU CONTRASEÑA")
```
Reemplaza **"AQUI PONES TU USUARIO"** con tu nombre de usuario de Instagram, y **"AQUI PONES TU CONTRASEÑA"** con tu contraseña.

## Uso
Para usar el bot, asegúrate de tener instalado Python y la biblioteca Selenium. Luego, ejecuta el archivo de Python en tu terminal con el comando:
> python bot-instagram.py

El bot abrirá una ventana del navegador Chrome y accederá a la página de inicio de sesión de Instagram. Después de iniciar sesión, el bot buscará fotos relacionadas
con los hashtags indicados y dará "me gusta" a un máximo de 70 fotos por hashtag

Puedes agregar o modificar los hashtags que quieras buscar cambiando la lista de hashtags en el código:
```python
hashtag_list = ['animales', 'perros', 'gymbro', 'like4like','likeforlike', 'followforfollow', 'follow4follow', 'followme', 'followback', 'follow', 'follo']
```
