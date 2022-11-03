# to install the package:
# python3 -m pip install --upgrade Pillow

from PIL import Image
image = Image.open(
        "./public/img/45.jfif")
    # "C:\\Users\\seven\\Documents\\Projetos\\FURG\\AULA\\algortimo\\Urna3.0\public\\img\\13.gif")
new_image = image.resize((80, 120))
new_image.save(
    "./public/img/45.gif")
