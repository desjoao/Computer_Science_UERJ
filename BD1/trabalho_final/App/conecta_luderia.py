from ui_luderia import UI
from datetime import datetime, date
import psycopg2 as pg2
import traceback
import sys
from comandos import (CMD_CLIENTE, CMD_COMPRA, CMD_CADASTRAR_CLIENTE, 
                      CMD_ALTERAR_CLIENTE, CMD_APAGAR_CLIENTE, 
                      CMD_REGISTRAR_COMPRA, CMD_ALTERAR_COMPRA,
                      CMD_LISTAR_CLIENTES, CMD_APAGAR_COMPRA, CMD_LISTAR_COMPRAS)

class Connect:
    def __init__(self, nome_programa: str):
        self.ui = UI(nome_programa=nome_programa)
        self.login_frame = None
        self.conn = None
        self.comando_ui = None
        self.dados_ui = None # Usado para armazenar dados de formulários
        self.utils = self.ui.utils

        self.utils.log_inicio()

    # --- Métodos de Conexão e Fluxo de App ---

    def login(self):
        """Exibe a tela de login e obtém credenciais."""
        try:
            self.login_frame = self.ui.criar_frame()
            self.ui.entry_box(self.login_frame, 'dbname')
            self.ui.entry_box(self.login_frame, 'user')
            self.ui.entry_box(self.login_frame, "password", mask=True)
            self.ui.entry_box(self.login_frame, 'host')
            self.ui.entry_box(self.login_frame, 'port')
            # Usa o método de UI para enviar as entradas
            self.ui.botao_enviar_entradas(self.login_frame, 'Enviar', self.receber_dados_login)
            self.ui.iniciar_handler()
            return self.dados_ui
        
        except Exception:
            msg = 'Erro na interface de login. ' + traceback.format_exc()
            self.utils.log_erro(msg)
            sys.exit()

    def conecta(self, dbname: str, user: str, password: str, host: str, port: str):
        """Estabelece a conexão com o PostgreSQL."""
        try:
            self.conn = pg2.connect(host=host, port=port, database=dbname, user=user, password=password)
            self.ui.mensagem_info("", "Conexão estabelecida com sucesso.")
            return True

        except pg2.Error as e:
            msg = 'Erro ao conectar ao PostgreSQL'
            self.ui.mensagem_erro('Erro', f'Erro ao conectar com o PostgreSQL:\n{e}')
            self.utils.log_erro(msg + traceback.format_exc())
            return False

    def receber_dados_login(self, _, dados: dict):
        """Callback para receber os dados de login da UI e fechar o mainloop."""
        self.dados_ui = dados
        self.ui.finalizar_handler() # Finaliza o mainloop de login

    def receber_dados_e_comando(self, comando: int, dados: dict = None):
        """Callback genérico para receber dados e comando de qualquer janela Toplevel da UI."""
        self.comando_ui = comando
        self.dados_ui = dados
        #self.ui.finalizar_handler() # Finaliza o mainloop para retornar ao fluxo principal

    # --- Utilidades ---
    def _to_date(self, value):
        if value is None or value == '':
            return None
        if isinstance(value, date):
            return value
        # Se for string no formato ISO (YYYY-MM-DD)
        if isinstance(value, str):
            value = value.strip()
            if not value:
                return None
            # Tente formatos comuns
            for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"):
                try:
                    return datetime.strptime(value, fmt).date()
                except (ValueError, AttributeError):
                    pass
        # Último recurso: deixe o driver tentar adaptar
        return value

    def _clean_str(self, s):
        if s is None:
            return None
        s = str(s).strip()
        return s if s else None
    
    # --- Métodos de Manipulação de UI (Menus) ---

    def menu_principal(self):
        """Exibe o Menu Principal (Cliente/Compra)."""
        self.comando_ui = None # Reseta o comando
        self.ui.menu_principal(self.receber_dados_e_comando)
        #self.ui.iniciar_handler() # Inicia o mainloop e espera o comando
        return self.comando_ui

    def menu_cliente(self):
        """Exibe o Menu Cliente (Cadastrar/Alterar/Apagar)."""
        self.comando_ui = None
        self.ui.menu_cliente(self.receber_dados_e_comando)
        #self.ui.iniciar_handler()
        return self.comando_ui

    def menu_compra(self):
        """Exibe o Menu Compra (Novo/Alterar)."""
        self.comando_ui = None
        self.ui.menu_compra(self.receber_dados_e_comando)
        #self.ui.iniciar_handler()
        return self.comando_ui

    # --- Métodos de CRUD (Cliente) ---

    def cadastrar_cliente_ui(self):
        """Lança a UI de cadastro e espera o botão 'Cadastrar'."""
        self.dados_ui = None
        self.ui.form_cliente_cadastro(self.receber_dados_e_comando, CMD_CADASTRAR_CLIENTE)
        #self.ui.iniciar_handler()
        
        if self.dados_ui:
            self._inserir_cliente(self.dados_ui)

    def alterar_cliente_ui(self):
        """Lança a UI de alteração e espera o botão 'Alterar'."""
        self.dados_ui = None
        self.ui.form_cliente_alterar(self.receber_dados_e_comando, CMD_ALTERAR_CLIENTE)
        #self.ui.iniciar_handler()
        
        if self.dados_ui:
            self._alterar_cliente(self.dados_ui)

    def apagar_cliente_ui(self):
        """Lança a UI para deletar por CPF e espera o botão 'Apagar'."""
        self.dados_ui = None
        self.ui.form_cliente_apagar(self.receber_dados_e_comando, CMD_APAGAR_CLIENTE)
        #self.ui.iniciar_handler()
        
        if self.dados_ui:
            cpf = self.dados_ui.get("CPF")
            self._apagar_cliente(cpf)


    # --- Métodos de CRUD (Compra) ---

    def registrar_compra_ui(self):
        """Lança a UI de registro de compra."""
        self.dados_ui = None
        self.ui.form_compra_registro(self.receber_dados_e_comando, CMD_REGISTRAR_COMPRA)
        #self.ui.iniciar_handler()
        
        if self.dados_ui:
            self._registrar_compra(self.dados_ui)

    def alterar_compra_ui(self):
        """Lança a UI de alteração de compra."""
        self.dados_ui = None
        self.ui.form_compra_alterar(self.receber_dados_e_comando, CMD_ALTERAR_COMPRA)
        
        if self.dados_ui:
            self._alterar_compra(self.dados_ui)

    def apagar_compra_ui(self):
        """Lança a UI para apagar uma compra."""
        self.dados_ui = None
        self.ui.form_compra_apagar(self.receber_dados_e_comando, CMD_APAGAR_COMPRA)
        if self.dados_ui:
            self._apagar_compra(self.dados_ui)

    def _apagar_compra(self, respostas: dict):
        cpfcliente = self._clean_str(respostas.get("cpfcliente"))
        idjogo = self._clean_str(respostas.get("idjogo"))
        cursor = None
        try:
            if not all([cpfcliente, idjogo]):
                self.ui.mensagem_erro("Erro", "cpfcliente e idjogo são obrigatórios.")
                return
            cursor = self.conn.cursor()
            sql = "DELETE FROM compra WHERE cpfcliente = %s AND idjogo = %s"
            cursor.execute(sql, (cpfcliente, idjogo))
            if cursor.rowcount == 0:
                self.ui.mensagem_erro("Falha", "Nenhum registro de compra encontrado.")
            else:
                self.conn.commit()
                self.ui.mensagem_info("Sucesso", "Compra apagada com sucesso.")
        except Exception as e:
            if self.conn: self.conn.rollback()
            error_msg = f"Não foi possível apagar a compra.\n{type(e).__name__}: {str(e)}"
            self.ui.mensagem_erro("Erro de BD", error_msg)
            self.utils.log_erro(error_msg + traceback.format_exc())
        finally:
            if cursor: cursor.close()

    def _listar_clientes(self):
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT cpf, nome, email, endereco, datanascimento FROM cliente ORDER BY nome;")
            linhas = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]
            data = [tuple(l) for l in linhas]
            self.ui.gera_tabela("Clientes", colunas, data)
        except Exception as e:
            msg = 'Não foi possível listar clientes'
            self.ui.mensagem_erro("Erro de BD", f"Não foi possível listar clientes.\n{e}")
            self.utils.log_erro(msg + traceback.format_exc())
        finally:
            if cursor: cursor.close()

    def _listar_compras(self):
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT cpfcliente, idjogo, datacompra
                FROM compra
                ORDER BY datacompra DESC;
            """)
            linhas = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]
            data = [tuple(l) for l in linhas]
            self.ui.gera_tabela("Compras", colunas, data)
        except Exception as e:
            msg = 'Não foi possível listar compras'
            self.ui.mensagem_erro("Erro de BD", f"{msg}.\n{e}")
            self.utils.log_erro(msg + traceback.format_exc())
        finally:
            if cursor: cursor.close()

    # --- Métodos de BD (Cliente) ---

    def _inserir_cliente(self, respostas: dict):
        cpf = self._clean_str(respostas.get("CPF"))
        nome = self._clean_str(respostas.get("nome"))
        email = self._clean_str(respostas.get("email"))
        endereco = self._clean_str(respostas.get("endereco"))
        datanascimento = self._to_date(respostas.get("datanascimento"))
        
        cursor = None
        try:
            if not all([cpf, nome, datanascimento]):
                self.ui.mensagem_erro("Erro", "CPF, Nome e Data de Nascimento são obrigatórios.")
                return
            cursor = self.conn.cursor()
            sql = """INSERT INTO cliente (cpf, nome, email, endereco, datanascimento) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (cpf, nome, email, endereco, datanascimento))
            self.conn.commit()
            self.ui.mensagem_info("Sucesso", f"Cliente '{nome}' cadastrado com sucesso!")
        
        except Exception as e:
            if self.conn: self.conn.rollback()
            error_msg = f"Não foi possível inserir o cliente.\n{type(e).__name__}: {str(e)}"
            self.ui.mensagem_erro("Erro de BD", error_msg)
            self.utils.log_erro(error_msg + traceback.format_exc())

        finally:
            if cursor: cursor.close()

    def _alterar_cliente(self, respostas: dict):
        cpf = self._clean_str(respostas.get("CPF"))
        nome = self._clean_str(respostas.get("nome"))
        email = self._clean_str(respostas.get("email"))
        endereco = self._clean_str(respostas.get("endereco"))
        datanascimento = self._to_date(respostas.get("datanascimento"))
        
        cursor = None
        try:
            if not cpf:
                self.ui.mensagem_erro("Erro", "CPF é obrigatório para alteração.")
                return
            
            cursor = self.conn.cursor()
            sql = """UPDATE cliente SET 
                     nome = %s, email = %s, endereco = %s, datanascimento = %s 
                     WHERE cpf = %s"""
            cursor.execute(sql, (nome, email, endereco, datanascimento, cpf))

            if cursor.rowcount == 0:
                 self.ui.mensagem_erro("Falha", "Nenhum cliente encontrado com o CPF informado.")
            else:
                self.conn.commit()
                self.ui.mensagem_info("Sucesso", f"Cliente CPF {cpf} alterado com sucesso!")
        
        except Exception as e:
            if self.conn: self.conn.rollback()
            msg = 'Não foi possível alterar o cliente'
            self.ui.mensagem_erro("Erro de BD", f"Não foi possível alterar o cliente.\n{e}")
            self.utils.log_erro(msg + traceback.format_exc())

        finally:
            if cursor: cursor.close()

    def _apagar_cliente(self, cpf: str):
        cursor = None
        try:
            if not cpf:
                self.ui.mensagem_erro("Erro", "CPF é obrigatório para exclusão.")
                return

            cursor = self.conn.cursor()
            
            # Deletar em tabelas relacionadas (OBS: Depende da sua FK ser CASCADE DELETE, se não for,
            # você deve fazer o DELETE em Compra primeiro, e depois em Cliente)
            # Assumindo que você precisa deletar manualmente em Compra, se houver:
            sql_compra = "DELETE FROM compra WHERE cpfcliente = %s"
            cursor.execute(sql_compra, (cpf,))
            
            sql_cliente = "DELETE FROM cliente WHERE cpf = %s"
            cursor.execute(sql_cliente, (cpf,))

            if cursor.rowcount == 0:
                 self.ui.mensagem_erro("Falha", "Nenhum cliente encontrado com o CPF informado.")
            else:
                self.conn.commit()
                self.ui.mensagem_info("Sucesso", f"Cliente CPF {cpf} e registros de compra relacionados apagados com sucesso!")
        
        except Exception as e:
            if self.conn: self.conn.rollback()
            msg = 'Não foi possível apagar o cliente'
            self.ui.mensagem_erro("Erro de BD", f"Não foi possível apagar o cliente.\n{e}")
            self.utils.log_erro(msg + traceback.format_exc())

        finally:
            if cursor: cursor.close()
    
    # --- Métodos de BD (Compra) ---

    def _registrar_compra(self, respostas: dict):
        cpfcliente = self._clean_str(respostas.get("cpfcliente"))
        idjogo = self._clean_str(respostas.get("idjogo"))
        datacompra = self._to_date(respostas.get("datacompra"))
        
        cursor = None
        try:
            if not all([cpfcliente, idjogo, datacompra]):
                self.ui.mensagem_erro("Erro", "Todos os campos são obrigatórios.")
                return

            cursor = self.conn.cursor()
            sql = """INSERT INTO compra (cpfcliente, idjogo, datacompra) VALUES (%s, %s, %s)"""
            cursor.execute(sql, (cpfcliente, idjogo, datacompra))
            self.conn.commit()
            self.ui.mensagem_info("Sucesso", f"Compra registrada com sucesso para CPF {cpfcliente}.")
        
        except Exception as e:
            if self.conn: self.conn.rollback()
            error_msg = f"Não foi possível registrar a compra.\n{type(e).__name__}: {str(e)}"
            self.ui.mensagem_erro("Erro de BD", error_msg)
            self.utils.log_erro(error_msg + traceback.format_exc())

        finally:
            if cursor: cursor.close()
    
    def _alterar_compra(self, respostas: dict):
        cpfcliente = self._clean_str(respostas.get("cpfcliente"))
        idjogo_antigo = self._clean_str(respostas.get("idjogo_antigo"))
        idjogo_novo = self._clean_str(respostas.get("idjogo_novo"))
        datacompra = self._to_date(respostas.get("datacompra"))
        cursor = None
        try:
            if not all([cpfcliente, idjogo_antigo, idjogo_novo, datacompra]):
                self.ui.mensagem_erro("Erro", "Todos os campos são obrigatórios.")
                return
            
            cursor = self.conn.cursor()
            
            # Verifica a existência do ID antigo (se for a PK, basta o WHERE)
            # Assumindo que a PK da tabela Compra é (cpfcliente, idjogo)
            sql = """UPDATE compra SET 
                     idjogo = %s, datacompra = %s 
                     WHERE cpfcliente = %s AND idjogo = %s"""

            cursor.execute(sql, (idjogo_novo, datacompra, cpfcliente, idjogo_antigo))

            if cursor.rowcount == 0:
                 self.ui.mensagem_erro("Falha", "Nenhum registro de compra encontrado para este cliente e ID de jogo.")
            else:
                self.conn.commit()
                self.ui.mensagem_info("Sucesso", f"Registro de compra alterado com sucesso para CPF {cpfcliente}.")
        
        except Exception as e:
            if self.conn: self.conn.rollback()
            msg = 'Não foi possível alterar o registro de compra'
            self.ui.mensagem_erro("Erro de BD", f"Não foi possível alterar o registro de compra.\n{e}")
            self.utils.log_erro(msg + traceback.format_exc())

        finally:
            if cursor: cursor.close()


if __name__ == "__main__":
    nome = 'interface_luderia'
    connector = Connect(nome_programa=nome)
    
    # 1. Login e Conexão (Usa iniciar/finalizar_handler para coletar dados)
    respostas_login = connector.login()
    if not respostas_login:
        sys.exit()
    
    if not connector.conecta(dbname = respostas_login['dbname'],
                             user = respostas_login['user'],
                             password = respostas_login['password'],
                             host = respostas_login['host'],
                             port = respostas_login['port']):
        sys.exit()

    connector.login_frame.destroy()
    connector.ui.root.withdraw()

    # 2. Loop principal de navegação (AGORA NÃO USA iniciar_handler)
    while True:
        comando_principal = connector.menu_principal()

        if comando_principal == CMD_CLIENTE:
            while True:
                comando_cliente = connector.menu_cliente()
                
                if comando_cliente == CMD_CADASTRAR_CLIENTE:
                    connector.cadastrar_cliente_ui()
                elif comando_cliente == CMD_ALTERAR_CLIENTE:
                    connector.alterar_cliente_ui()
                elif comando_cliente == CMD_APAGAR_CLIENTE:
                    connector.apagar_cliente_ui()
                elif comando_cliente == CMD_LISTAR_CLIENTES:
                    connector._listar_clientes()
                else: 
                    break
        
        elif comando_principal == CMD_COMPRA:
            while True:
                comando_compra = connector.menu_compra()

                if comando_compra == CMD_REGISTRAR_COMPRA:
                    connector.registrar_compra_ui()
                elif comando_compra == CMD_ALTERAR_COMPRA:
                    connector.alterar_compra_ui()
                elif comando_compra == CMD_APAGAR_COMPRA:
                    connector.apagar_compra_ui()
                elif comando_compra == CMD_LISTAR_COMPRAS:
                    connector._listar_compras()
                else: 
                    break

        else: 
            break
    
    # Fim da aplicação
    # Não precisa de finalizar_handler aqui se já está saindo do loop e chamando sys.exit()
    if connector.conn:
        connector.conn.close()
    connector.utils.log_fim()
    sys.exit()