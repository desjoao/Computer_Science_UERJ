import sys
import traceback
from utils import Utils
import tkinter as tk
import ttkbootstrap as ttb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from tkinter.ttk import (Frame)
from tkinter import (ttk, filedialog, messagebox, BOTH)
from comandos import (CMD_CLIENTE, CMD_COMPRA, CMD_CADASTRAR_CLIENTE, CMD_ALTERAR_CLIENTE, 
                      CMD_APAGAR_CLIENTE, CMD_REGISTRAR_COMPRA, CMD_ALTERAR_COMPRA,
                      CMD_LISTAR_CLIENTES, CMD_APAGAR_COMPRA, CMD_LISTAR_COMPRAS)

class UI(Frame):
    def __init__(self, nome_programa: str):
        try:
            self.utils = Utils(nome_programa)
            # ... (Mantenha a leitura do config.ui e configuração de variáveis) ...
            self.config = self.utils.read_json('config.ui')
            self.__entradas = {}
            self.__resp_entrada = {}
            self.__frames = {}
            self.comando_selecionado = None # Novo atributo
            self.app_toplevel = None      # Novo atributo para rastrear a janela Toplevel atual

            # Diagramação
            ## Entry Box
            self.entry_fill = self.config["LAYOUT"]["TEntry"]["fill"]
            self.entry_padx = self.config["LAYOUT"]["TEntry"]["padx"]
            self.entry_pady = self.config["LAYOUT"]["TEntry"]["pady"]
            self.entry_expand = self.config["LAYOUT"]["TEntry"]["expand"]
            self.entry_state = self.config["LAYOUT"]["TEntry"]["state"]
            ## Date Box
            self.date_fill = self.config["LAYOUT"]["TDate"]["fill"]
            self.date_padx = self.config["LAYOUT"]["TDate"]["padx"]
            self.date_pady = self.config["LAYOUT"]["TDate"]["pady"]
            self.date_expand = self.config["LAYOUT"]["TDate"]["expand"]
            # Frame
            self.fr_fill = self.config["LAYOUT"]["TFrame"]["fill"]
            self.fr_pady = self.config["LAYOUT"]["TFrame"]["pady"]
            self.fr_expand = self.config["LAYOUT"]["TFrame"]["expand"]
            ## Label
            self.lbl_fill = self.config["LAYOUT"]["TLabel"]["fill"]
            self.lbl_padx = self.config["LAYOUT"]["TLabel"]["padx"]
            self.lbl_pady = self.config["LAYOUT"]["TLabel"]["pady"]
            self.lbl_side = self.config["LAYOUT"]["TLabel"]["side"]
            self.lbl_width = self.config["LAYOUT"]["TLabel"]["width"]
            self.lbl_expand = self.config["LAYOUT"]["TLabel"]["expand"]
            ## Button
            self.btn_fill = self.config["LAYOUT"]["TButton"]["fill"]
            self.btn_padding = self.config["LAYOUT"]["TButton"]["padding"]
            self.btn_side = self.config["LAYOUT"]["TButton"]["side"]
            self.btn_expand = self.config["LAYOUT"]["TButton"]["expand"]
            self.btn_state = self.config["LAYOUT"]["TButton"]["state"]
            ## Notebook
            self.ntb_fill = self.config["LAYOUT"]["TNotebook"]["fill"]
            self.ntb_padx = self.config["LAYOUT"]["TNotebook"]["padx"]
            self.ntb_pady = self.config["LAYOUT"]["TNotebook"]["pady"]
            self.ntb_padding = self.config["LAYOUT"]["TNotebook"]["padding"]
            self.ntb_expand = self.config["LAYOUT"]["TNotebook"]["expand"]
            ## Table
            self.tbl_fill = self.config["LAYOUT"]["TTabela"]["fill"]
            self.tbl_padx = self.config["LAYOUT"]["TTabela"]["padx"]
            self.tbl_pady = self.config["LAYOUT"]["TTabela"]["pady"]
            self.tbl_expand = self.config["LAYOUT"]["TTabela"]["expand"]
            self.tbl_paginated = self.config["LAYOUT"]["TTabela"]["paginated"]
            self.tbl_searchable = self.config["LAYOUT"]["TTabela"]["searchable"]
            # Top Level 
            self.top_size = (int(self.config["LAYOUT"]["TopLevel"]["width"]),
                                   int(self.config["LAYOUT"]["TopLevel"]["height"]))
            self.top_position = (int(self.config["LAYOUT"]["TopLevel"]["horizontal"]),
                                      int(self.config["LAYOUT"]["TopLevel"]["vertical"]))

            # Root
            self.root = ttb.Window(themename=self.config["LAYOUT"]["ROOT"]["theme"],
                                size=(self.config["LAYOUT"]["ROOT"]["width"],
                                        self.config["LAYOUT"]["ROOT"]["height"]),
                                    position=(self.config["LAYOUT"]["ROOT"]["position_horizontal"],
                                                self.config["LAYOUT"]["ROOT"]["position_vertical"]),
                                    resizable=(self.config["LAYOUT"]["ROOT"]["resizable_width"],
                                            self.config["LAYOUT"]["ROOT"]["resizable_heigth"]))
            
            super().__init__()

            # Estilização
            style = ttk.Style()
            TButton = self.config["LAYOUT"]["TButton"]
            self.button_bootstyle = TButton["theme"]
            style.configure("TButton", font = (TButton["font"], int(TButton["font_size"]), TButton["font_style"]))
            
            TLabel = self.config["LAYOUT"]["TLabel"]
            self.label_bootstyle = TLabel["theme"]
            style.configure("TLabel", font = (TLabel["font"], int(TLabel["font_size"]), TLabel["font_style"]))
            
            TEntry = self.config["LAYOUT"]["TEntry"]
            self.entry_bootstyle = TEntry["theme"]
            style.configure("TEntry", font = (TEntry["font"], int(TEntry["font_size"]), TEntry["font_style"]))
            
            TDate = self.config["LAYOUT"]["TDate"]
            self.date_bootstyle = TDate["theme"]
            
            TNotebook = self.config["LAYOUT"]["TNotebook"]
            self.notebook_bootstyle = TNotebook["theme"]
            style.configure("TNotebook", tabposition = TNotebook["tabposition"])
            
            TFrame = self.config["LAYOUT"]["TFrame"]
            self.frame_bootstyle = TFrame["theme"]
            style.configure("TFrame", borderwidth = TFrame["borderwidth"], relief = TFrame["relief"])
            
            TTabela = self.config["LAYOUT"]["TTabela"]
            self.tabela_bootstyle = TTabela["theme"]

        except Exception as e:
            msg = "Erro no construtor da classe UI."
            print(msg, traceback.format_exc())
            raise e(msg)
    
    # Métodos de Controle

    def iniciar_handler(self):
        """Inicia o mainloop do root."""
        try:
            self.root.mainloop()

        except Exception:
            pass
    
    def finalizar_handler(self):
        """Para o mainloop do root."""
        try:
            self.root.quit()
        
        except Exception:
            pass
    
    def destruir_toplevel(self):
        """Destrói a janela Toplevel rastreada."""
        if self.app_toplevel and self.app_toplevel.winfo_exists():
            self.app_toplevel.destroy()
            self.app_toplevel = None

    # Métodos de Entrada de Dados

    def enviar_entradas(self, callback_fn, comando: int = None, apenas_dados: bool = False):
        """Coleta dados e executa a função de callback, fechando o mainloop."""
        try:
            for chave, valor in self.__entradas.items():
                # DateEntry retorna um date object, Entry retorna string
                if hasattr(valor, 'entry'):  # É um DateEntry
                    date_val = valor.entry.get()
                    # Se for um date object, converte para string ISO
                    if hasattr(date_val, 'strftime'):
                        self.__resp_entrada.update({chave: date_val.strftime('%Y-%m-%d')})
                    else:
                        self.__resp_entrada.update({chave: str(date_val)})
                else:  # É um Entry normal
                    self.__resp_entrada.update({chave: valor.get()})
            
            # Se a UI tem um Toplevel (formulário/menu), fecha ele.
            self.destruir_toplevel()
            
            # Chama o callback no Connect com o comando e os dados coletados
            if apenas_dados:
                callback_fn(self.__resp_entrada)
            else:
                callback_fn(comando, self.__resp_entrada)
            self.limpar_entradas()
            
        except Exception as e:
            self.mensagem_erro("Erro de UI", f"Falha ao processar as entradas.\n{str(e)}")
            # Se for um erro no formulário, só fecha a janela
            self.destruir_toplevel()
            # E retorna um comando Nulo para o Connect
            callback_fn(None, None)

    def receber_entradas(self):
        return self.__resp_entrada

    def limpar_entradas(self):
        self.__entradas = {}
        self.__resp_entrada = {}
    
    def entry_box(self, frame: Frame, rotulo: str, mask=False):
        """Cria um Label e um Entry box e armazena a referência."""
        try:
            newframe = ttb.Frame(frame)
            newframe.pack(fill=self.fr_fill, expand=self.fr_expand, pady=self.fr_pady)
            lbl = ttb.Label(newframe, text=rotulo, width=self.lbl_width, bootstyle=self.label_bootstyle)
            lbl.pack(fill=self.lbl_fill, side = self.lbl_side, padx=self.lbl_padx, pady=self.lbl_pady)
            entrada = ttb.Entry(newframe, show='*' if mask else '', bootstyle=self.entry_bootstyle)
            entrada.pack(fill=self.entry_fill, padx=self.entry_padx, pady=self.entry_pady)
            self.__entradas.update({rotulo: entrada})
        
        except Exception:
            pass

    def date_box(self, frame: Frame, rotulo: str):
        """Cria um Label e um DateEntry box e armazena a referência."""
        try:
            newframe = ttb.Frame(frame)
            newframe.pack(fill=self.fr_fill, expand=self.fr_expand, pady=self.fr_pady)
            lbl = ttb.Label(newframe, text=rotulo, width=self.lbl_width, bootstyle=self.label_bootstyle)
            lbl.pack(fill=self.lbl_fill, side = self.lbl_side, padx=self.lbl_padx, pady=self.lbl_pady)
            date_box = ttb.DateEntry(newframe, bootstyle=self.date_bootstyle)
            date_box.pack(fill=self.date_fill, padx=self.date_padx, pady=self.date_pady)
            self.__entradas.update({rotulo: date_box})
        
        except Exception:
            pass

    # --- Métodos de Botão e Frame ---

    def criar_frame(self, elemento_pai = None):
        """Cria um frame e o empacota."""
        try:
            if not elemento_pai:
                frame = ttb.Frame(self.root)
            else:
                frame = ttb.Frame(elemento_pai)
            
            frame.pack(fill=self.fr_fill, expand=self.fr_expand, pady=self.fr_pady)
            return frame
        
        except Exception:
            pass

    def _comando_e_fecha(self, callback_fn, comando):
        """Chama a função de callback com o comando e destrói o Toplevel."""
        self.destruir_toplevel()
        callback_fn(comando, None) # Passa o comando e dados vazios
    
    def botao_simples(self, frame: Frame, rotulo: str, callback_fn, comando: int = None):
        """Cria um botão que executa um comando via callback."""
        try:
            comando_fn = lambda: self._comando_e_fecha(callback_fn, comando)
            
            botao = ttb.Button(frame, text=rotulo, command=comando_fn, bootstyle=self.button_bootstyle)
            botao.pack(fill=self.btn_fill, expand=self.btn_expand, pady=5)
        
        except Exception:
            print('Erro ao criar botão', traceback.format_exc())
            sys.exit()

    def botao_enviar_entradas(self, frame: Frame, rotulo: str, callback_fn, comando: int = None):
        """Cria o botão 'Enviar' ou 'Cadastrar' que coleta e envia os dados."""
        try:
            newframe = ttb.Frame(frame)
            newframe.pack()
            # Usa o método enviar_entradas da UI, que por sua vez chama o callback
            botao = ttb.Button(newframe, text=rotulo, 
                               command=lambda: self.enviar_entradas(callback_fn, comando), 
                               bootstyle=self.button_bootstyle)
            botao.pack(fill=self.btn_fill, side=self.btn_side, pady=10)
        
        except Exception:
            print('Erro ao criar botão de envio', traceback.format_exc())
            sys.exit()

    # --- Métodos de Mensagens e Tabela ---

    def mensagem_info(self, titulo:str, msg:str):
        messagebox.showinfo(title=titulo, message=msg)
    
    def mensagem_erro(self, titulo:str, msg:str):
        messagebox.showerror(title=titulo, message=msg)

    def gera_tabela(self, titulo, colunas, dados):
        """Gera uma tabela em um novo Toplevel."""
        try:
            app = ttb.Toplevel(self.root, size=self.top_size, position=self.top_position)
            app.title(titulo)

            coldata = [{"text": c, "stretch": True} for c in colunas]
            table = Tableview(
                master=app,
                coldata=coldata,
                rowdata=dados,
                paginated=self.tbl_paginated,
                searchable=self.tbl_searchable,
                bootstyle=self.tabela_bootstyle
            )
            table.pack(fill=self.tbl_fill, expand=self.tbl_expand, padx=self.tbl_padx, pady=self.tbl_pady)

        except Exception:
            self.mensagem_erro("Erro de UI", "Erro ao gerar tabela.")

    # --- Métodos de Menus (Requisitos 1 e 3) ---

    def _criar_janela_menu(self, titulo: str, botoes: dict, callback_fn):
        """Cria uma janela Toplevel genérica para menus."""
        self.limpar_entradas() # Limpa entradas antigas
        self.app_toplevel = ttb.Toplevel(self.root, size=self.top_size, position=self.top_position)
        self.app_toplevel.title(titulo)
        
        # O Protocolo de janela (X no canto) é configurado para interromper o mainloop
        fechar_fn = lambda: self._comando_e_fecha(callback_fn, None)
        self.app_toplevel.protocol("WM_DELETE_WINDOW", fechar_fn)

        frame = self.criar_frame(self.app_toplevel)
        
        for rotulo, comando in botoes.items():
            # O botão fechará o Toplevel e chamará o callback
            self.botao_simples(frame, rotulo, callback_fn, comando)
            
        # Oculta o root (janela principal) enquanto o menu está aberto
        # self.root.withdraw() # Já está oculto no main do connect.py
        
        self.root.wait_window(self.app_toplevel) # Bloqueia o main loop até que a janela seja destruída
        
    def menu_principal(self, callback_fn):
        """Requisito 1: Menu Principal."""
        botoes = {
            "Cliente": CMD_CLIENTE,
            "Compra": CMD_COMPRA
        }
        self._criar_janela_menu('Menu Principal', botoes, callback_fn)

    def menu_cliente(self, callback_fn):
        """Requisito 2: Menu Cliente."""
        botoes = {
            "Cadastrar cliente": CMD_CADASTRAR_CLIENTE,
            "Alterar cliente": CMD_ALTERAR_CLIENTE,
            "Apagar cliente": CMD_APAGAR_CLIENTE,
            "Listar clientes": CMD_LISTAR_CLIENTES
        }
        self._criar_janela_menu('Menu Cliente', botoes, callback_fn)

    def menu_compra(self, callback_fn):
        """Requisito 3: Menu Compra."""
        botoes = {
            "Registrar nova compra": CMD_REGISTRAR_COMPRA,
            "Alterar registro de compra": CMD_ALTERAR_COMPRA,
            "Apagar registro de compra": CMD_APAGAR_COMPRA,
            "Listar compras": CMD_LISTAR_COMPRAS
        }
        self._criar_janela_menu('Menu Compra', botoes, callback_fn)
    # --- Métodos de Formulários (Requisito 2.2, 2.3, 2.4) ---

    def form_cliente_cadastro(self, callback_fn, comando):
        """Requisito 2.2: Formulário de Cadastro de Cliente."""
        self.limpar_entradas()
        self.app_toplevel = ttb.Toplevel(self.root, size=self.top_size, position=self.top_position)
        self.app_toplevel.title('Cadastramento de Clientes')
        self.app_toplevel.protocol("WM_DELETE_WINDOW", lambda: callback_fn(None, None))

        frame = self.criar_frame(self.app_toplevel)
        self.entry_box(frame, 'CPF')
        self.entry_box(frame, 'nome')
        self.entry_box(frame, 'email')
        self.entry_box(frame, 'endereco')
        self.date_box(frame, 'datanascimento')
        self.botao_enviar_entradas(frame, 'Cadastrar', callback_fn, comando)

        self.root.wait_window(self.app_toplevel)

    def form_cliente_alterar(self, callback_fn, comando):
        """Requisito 2.3: Formulário de Alteração de Cliente."""
        self.limpar_entradas()
        self.app_toplevel = ttb.Toplevel(self.root, size=self.top_size, position=self.top_position)
        self.app_toplevel.title('Alteração de Cliente')
        self.app_toplevel.protocol("WM_DELETE_WINDOW", lambda: callback_fn(None, None))

        frame = self.criar_frame(self.app_toplevel)
        self.entry_box(frame, 'CPF') # CPF obrigatório para WHERE
        self.entry_box(frame, 'nome')
        self.entry_box(frame, 'email')
        self.entry_box(frame, 'endereco')
        self.date_box(frame, 'datanascimento')
        self.botao_enviar_entradas(frame, 'Alterar', callback_fn, comando)

        self.root.wait_window(self.app_toplevel)

    def form_cliente_apagar(self, callback_fn, comando):
        """Requisito 2.4: Formulário para Apagar Cliente."""
        self.limpar_entradas()
        self.app_toplevel = ttb.Toplevel(self.root, size=self.top_size, position=self.top_position)
        self.app_toplevel.title('Apagar Cliente')
        self.app_toplevel.protocol("WM_DELETE_WINDOW", lambda: callback_fn(None, None))

        frame = self.criar_frame(self.app_toplevel)
        self.entry_box(frame, 'CPF')
        self.botao_enviar_entradas(frame, 'Apagar', callback_fn, comando)

        self.root.wait_window(self.app_toplevel)

    # --- Métodos de Formulários de Compra (Requisito 3.2, 3.3) ---

    def form_compra_registro(self, callback_fn, comando):
        """Requisito 3.2: Formulário de Registro de Nova Compra."""
        self.limpar_entradas()
        self.app_toplevel = ttb.Toplevel(self.root, size=self.top_size, position=self.top_position)
        self.app_toplevel.title('Registro de Nova Compra')
        self.app_toplevel.protocol("WM_DELETE_WINDOW", lambda: callback_fn(None, None))

        frame = self.criar_frame(self.app_toplevel)
        self.entry_box(frame, 'cpfcliente')
        self.entry_box(frame, 'idjogo')
        self.date_box(frame, 'datacompra')
        self.botao_enviar_entradas(frame, 'Registrar', callback_fn, comando)

        self.root.wait_window(self.app_toplevel)

    def form_compra_alterar(self, callback_fn, comando):
        """Requisito 3.3: Formulário de Alteração de Registro de Compra."""
        self.limpar_entradas()
        self.app_toplevel = ttb.Toplevel(self.root, size=self.top_size, position=self.top_position)
        self.app_toplevel.title('Alteração de Registro de Compra')
        self.app_toplevel.protocol("WM_DELETE_WINDOW", lambda: callback_fn(None, None))

        frame = self.criar_frame(self.app_toplevel)
        self.entry_box(frame, 'cpfcliente')
        self.entry_box(frame, 'idjogo_antigo') # Para a cláusula WHERE (o registro existente)
        self.entry_box(frame, 'idjogo_novo')   # O novo valor do idjogo
        self.date_box(frame, 'datacompra')
        self.botao_enviar_entradas(frame, 'Alterar', callback_fn, comando)

        self.root.wait_window(self.app_toplevel)
    
    def form_compra_apagar(self, callback_fn, comando):
        """Formulário para apagar um registro de compra."""
        self.limpar_entradas()
        self.app_toplevel = ttb.Toplevel(self.root, size=self.top_size, position=self.top_position)
        self.app_toplevel.title('Apagar Registro de Compra')
        self.app_toplevel.protocol("WM_DELETE_WINDOW", lambda: callback_fn(None, None))

        frame = self.criar_frame(self.app_toplevel)
        self.entry_box(frame, 'cpfcliente')
        self.entry_box(frame, 'idjogo')
        self.botao_enviar_entradas(frame, 'Apagar', callback_fn, comando)

        self.root.wait_window(self.app_toplevel)