import os
import shutil

ruta_destino='E:\series y peliculas\por ordenar'

ruta=input()

os.chdir(ruta)

main_ruta=ruta

print(main_ruta)

archivos=os.listdir(main_ruta)

def busca_mkv(archivos, ruta):
	os.chdir(ruta)
	for archivo in archivos:
		nombre_archivo, extencion_archivo=os.path.splitext(archivo)
		if (extencion_archivo==".MKV" or extencion_archivo==".mkv"):
			print('nice')
			shutil.move(archivo, ruta_destino)
			print(os.getcwd())
		else:
			pass


busca_mkv(archivos,main_ruta)

carpetas=list(filter(os.path.isdir, archivos))

for carpeta in carpetas:
	sub_ruta=main_ruta+carpeta
	archivos_2=os.listdir(sub_ruta)
	busca_mkv(archivos_2, sub_ruta)
	
