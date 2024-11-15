import datetime

hora_texto = "11 a.m." 

# Corrigindo o formato:
hora_texto = hora_texto.replace(" a.m.", " AM")  # Ou hora_texto.replace(" a.m.", " AM").upper()

# Convertendo para o objeto de data e hora:
hora_formatada = datetime.datetime.strptime(hora_texto, "%I %p").strftime("%H:%M")

print(hora_formatada)  # Saída: 11:00