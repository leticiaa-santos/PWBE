import os
import pandas as pd
import openpyxl
import io
from .models import Ambientes, Historico, Sensores
from django.http import JsonResponse, HttpResponse, FileResponse
import zipfile
import io

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # pasta onde está o script
ambientes_excel = os.path.join(BASE_DIR, 'excel', 'ambientes.xlsx')

# sensores
umidade_excel = os.path.join(BASE_DIR, 'excel', 'umidade.xlsx')
contador_excel = os.path.join(BASE_DIR, 'excel', 'contador.xlsx')
luminosidade_excel = os.path.join(BASE_DIR, 'excel', 'luminosidade.xlsx')
temperatura_excel = os.path.join(BASE_DIR, 'excel', 'temperatura.xlsx')


def ler_excel(request):
    ler_excel_ambientes()
    ler_excel_sensor()
    return JsonResponse({'mensagem': 'Os dados foram importados com sucesso!'})

def exportar_excel(request):
    # arquivo zip
    zip_buffer = io.BytesIO()  

    # abrir e escrever dentro do arquivo
    with zipfile.ZipFile(zip_buffer, 'w') as zf:
        # Exportar ambientes
        ambientes = Ambientes.objects.all().values()
        df_ambientes = pd.DataFrame(ambientes)
        ambiente_csv = io.StringIO()
        # abre o arquivo para colocar dentro, ele salva e cria
        df_ambientes.to_csv(ambiente_csv, index=False, sep=';')
        zf.writestr('ambientes.csv', ambiente_csv.getvalue())

        # Exportar sensores
        sensores = Sensores.objects.all().values()
        df_sensores = pd.DataFrame(sensores)
        sensores_csv = io.StringIO()
        df_sensores.to_csv(sensores_csv, index=False, sep=';')
        zf.writestr('sensores.csv', sensores_csv.getvalue())

    zip_buffer.seek(0)

    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="dados.zip"'
    return response

def ler_excel_ambientes():
    df = pd.read_excel(ambientes_excel)
    #importados os ambientes
    for _, row in df.iterrows():
        criar_ambiente(
            sig=row['sig'],
            descricao=row['descricao'],
            ni=row['ni'],
            responsavel=row['responsavel']
        )
    data = df.to_dict(orient='records')
    return JsonResponse({'mensagem': 'dados importados com sucesso!'})
    
    
def criar_ambiente(sig, descricao, ni, responsavel):
    ambiente = Ambientes.objects.create(
        sig=sig,
        descricao=descricao,
        ni=ni,
        responsavel=responsavel
    )
    return ambiente

def exportar_ambiente():
    ambientes = Ambientes.objects.all().values()
    df = pd.DataFrame(list(ambientes))
    return df


def ler_excel_sensor():
    df = pd.concat([pd.read_excel(umidade_excel), 
                   pd.read_excel(contador_excel), 
                   pd.read_excel(luminosidade_excel),
                   pd.read_excel(temperatura_excel)])
    print(df)
    
    for _, row in df.iterrows():
        sensor = criar_sensor(
            sensor = row['sensor'],
            mac_address = row['mac_address'],
            unidade_med = row['unidade_medida'],
            latitude = row['latitude'],
            longitude = row['longitude'],
            status = row['status']
        )
        
        print(sensor)


def criar_sensor(sensor, mac_address,  unidade_med, latitude, longitude, status):
    sensor_criado = Sensores.objects.create(
        sensor = sensor,
        mac_address = mac_address,
        unidade_med =  unidade_med,
        latitude = latitude,
        longitude = longitude,
        status = status
    )
    return sensor_criado

def exportar_sensores():
    sensores = Ambientes.objects.all().values()
    df = pd.DataFrame(list(sensores))
    return df