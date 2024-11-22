
with open('/Users/lilibethpuchaicela/Desktop/Tesis/Algoritmos/newFolder/ESTUDIANTE_PERIODO_LAB1_31102024_v5_.csv', 'r') as file:
    contenido = file.read()

contenido = contenido.replace(',', '.').replace('Pueblos indígenas de la Sierra\t|', '|').replace('\n|', '|').replace('\t', ' ').replace('Visual\nVisual|', 'Visual|').replace('UNIDAD EDUCATIVA MUNICIPAL \nJACINTO GORDILLO|', 'UNIDAD EDUCATIVA MUNICIPAL JACINTO GORDILLO|')

ruta_salida = '/Users/lilibethpuchaicela/Desktop/Tesis/Algoritmos/newFolder/ArchivoCorregidoData5.csv'
with open(ruta_salida, 'w') as file:
    file.write(contenido)

# Leer el nuevo archivo con pandas utilizando la ruta completa
# df = pd.read_csv(ruta_salida, sep=';')

# Mostrar las primeras filas para verificar que se ha leído correctamente
# print(df.head())
