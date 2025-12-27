import os
import json
import time
import socket
from datetime import datetime

class Utils:
    def __init__(self, nome_programa:str):
        self.__version__ = "1.0.0.0"
        self.nome = nome_programa
        self.user = os.environ.get('USER')
        self.maquina = socket.gethostname()
        pasta_logs = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(pasta_logs):
            os.makedirs(pasta_logs)
        self.caminho_log = os.path.join(pasta_logs, f'log{self.nome}.txt')
    
    def read_json(self, name: str):
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            file_name = name + '.json'
            path_json = os.path.join(path, file_name)
            with open(path_json, encoding = 'utf-8') as json_file:
                return json.load(json_file)
        
        except FileNotFoundError as e:
            msg = f'Arquivo {name} não encontrado.'
            print(msg)
            return None
    
    def log_acerto(self, msg: str):
        msg = f'{datetime.now()};{self.user};{self.maquina};{self.nome};OK;{msg}\n'
        with open (self.caminho_log, 'a') as f:
            f.write(msg)
    
    def log_erro(self, msg:str):
        msg = f'{datetime.now()};{self.user};{self.maquina};{self.nome};NOK;{msg}\n'
        with open (self.caminho_log, 'a') as f:
            f.write(msg)
    
    def log_inicio(self):
        global tempo_inicio
        tempo_inicio = time.time()
        msg = f'{datetime.now()};{self.user};{self.maquina};{self.nome};OK;INÍCIO:{tempo_inicio}\n'
        with open(self.caminho_log, 'a') as f:
            f.write(msg)
    
    def log_fim(self):
        global tempo_inicio
        tempo_fim = time.time()
        diff = tempo_fim - tempo_inicio
        msg = f'{datetime.now()};{self.user};{self.maquina};{self.nome};OK;FIM:{tempo_fim};DURACAO:{diff}\n'
        with open(self.caminho_log, 'a') as f:
            f.write(msg)