import os
import arcpy
import time
from datetime import datetime

# Caminho do projeto ArcGIS Pro (.aprx)
arquivo_aprx = arcpy.GetParameter(0)

# Diretório onde os arquivos JPEG serão salvos
pasta_jpeg = arcpy.GetParameterAsText(1)

# Nomeia o cliente
cliente = arcpy.GetParameterAsText(2)

# Nomeia tipo de Estudo
estudo = arcpy.GetParameterAsText(3)

# Carrega o projeto e obtém a lista de layouts
projeto = arcpy.mp.ArcGISProject(arquivo_aprx)
layouts = projeto.listLayouts()

# Define as opções de exportação para JPEG
dpi = 300
jpeg_quality = 300  

# Registra o tempo inicial
inicio = time.time()

# Registra a data no final do arq
current_date = datetime.now().strftime("%d%m%Y")

#Itera sobre os layouts, exportando cada um para um arquivo JPEG
for layout in layouts:
    nome_jpeg = f"{estudo}_{layout.name}_{cliente}_{current_date}"
    caminho_jpeg = os.path.join(pasta_jpeg, nome_jpeg)
    print(f"Exportando {layout.name} para {caminho_jpeg}")
    layout.exportToJPEG(caminho_jpeg, resolution=dpi, jpeg_quality=jpeg_quality)

# Registra o tempo final e tempo gasto
fim = time.time()
tempo_gasto = fim - inicio

print("Todos os layouts foram exportados com sucesso.")
print(f"Tempo gasto: {tempo_gasto:.2f} segundos.")