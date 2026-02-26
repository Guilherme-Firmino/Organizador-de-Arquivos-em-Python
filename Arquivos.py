import os
import shutil

usuario = os.path.expanduser("~")

arquivos_downloads = os.path.join(usuario, "Downloads")

for file in os.listdir(arquivos_downloads):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    
    organizador = f"{arquivos_downloads}/{file_extension}"

    if not os.path.isdir(organizador):
        os.mkdir(organizador)

    shutil.move(f"{arquivos_downloads}/{file}", f"{organizador}/{file}")