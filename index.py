import os
import glob
import schedule
import time
from datetime import datetime

# Encontrar todos os arquivos de vídeo
videos = glob.glob('**/*.mp4', recursive=True)

# Função para excluir arquivos de vídeo
def excluir_arquivos():
    for video in videos:
        try:
            os.remove(video)
            print(f"Arquivo excluído: {video}")
        except Exception as e:
            print(f"Erro ao excluir arquivo {video}: {str(e)}")

# Agendar a exclusão diária
schedule.every().day.at("23:59").do(excluir_arquivos)

# Loop principal
while True:
    schedule.run_pending()
    time.sleep(1)