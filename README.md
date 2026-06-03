# Comando & Controle (C&C) 🎮

Um servidor de Comando e Controle (C2) desenvolvido em Python para gerenciamento remoto de máquinas através de conexões de socket.

## ⚠️ Aviso Legal

**Este projeto é exclusivamente para fins educacionais e de pesquisa de segurança.** O uso não autorizado deste software é ilegal. Use apenas em ambientes controlados nos quais você tem permissão explícita.

## 📋 Descrição

Este projeto implementa um sistema de Comando e Controle (C2) em Python que permite comunicação bidirecional entre um servidor controlador e máquinas clientes. O sistema permite executar comandos remotos, gerenciar arquivos e capturar screenshots das máquinas clientes.

## 🏗️ Arquitetura

O projeto é composto por três componentes principais:

### 1. **c2.py** - Servidor C2 (Controlador)
- Aguarda conexões de clientes na porta 4444
- Fornece uma interface de linha de comando para interagir com clientes conectados
- Gerencia upload/download de arquivos
- Captura screenshots remotos
- Exibe saída colorida com feedback visual

### 2. **backdoor.py** - Cliente (Backdoor)
- Conecta ao servidor C2
- Executa comandos enviados remotamente
- Suporta upload/download de arquivos
- Captura e envia screenshots
- Executa operações em shell do sistema operacional

### 3. **system.py** - Cliente Alternativo
- Cliente de conexão com threading
- Suporta comunicação bidirecional com o servidor
- Implementação mais simples com reconexão automática
- Interface interativa de linha de comando

## ⚙️ Funcionalidades

### Servidor (c2.py)
- ✅ Aguarda conexões de clientes
- ✅ Shell remoto interativo
- ✅ Upload de arquivos para a máquina alvo
- ✅ Download de arquivos da máquina alvo
- ✅ Captura de screenshots remotos
- ✅ Interface colorida com feedback visual
- ✅ Menu de ajuda integrado

### Cliente (backdoor.py / system.py)
- ✅ Conecta ao servidor C2
- ✅ Executa comandos remotos
- ✅ Gerencia arquivos (upload/download)
- ✅ Captura screenshots
- ✅ Navegação de diretórios (cd)
- ✅ Reconexão automática

## 🛠️ Requisitos

- **Python 3.x**
- **termcolor** - Para colorizar a saída do terminal
- **pyautogui** - Para captura de screenshots (apenas para backdoor.py)
- **socket** - Biblioteca padrão de Python

### Instalação de dependências

```bash
pip install termcolor pyautogui
```

## 🚀 Como usar

### 1. Iniciar o Servidor C2

```bash
python c2.py
```

O servidor aguardará conexões na porta 4444:
```
[-] Waiting for connections
+ Connect with: ('192.168.1.100', 54321)
* Shell~192.168.1.100:
```

### 2. Conectar um Cliente

**Opção A - Usar backdoor.py:**
```bash
python backdoor.py
```

**Opção B - Usar system.py:**
```bash
# Edite o arquivo system.py e configure:
SERVER_IP = "seu_ip_servidor"
SERVER_PORT = 5000

python system.py
```

### 3. Comandos Disponíveis

No servidor C2, use os seguintes comandos:

| Comando | Descrição |
|---------|-----------|
| `help` | Mostra lista de comandos disponíveis |
| `exit` | Encerra a sessão com o alvo |
| `clear` | Limpa a tela do terminal |
| `cd <diretório>` | Muda de diretório na máquina alvo |
| `upload <arquivo>` | Envia arquivo para a máquina alvo |
| `download <arquivo>` | Baixa arquivo da máquina alvo |
| `screenshot` | Captura screenshot da máquina alvo |
| Qualquer comando | Executado no shell do alvo |

### Exemplo de uso

```bash
* Shell~192.168.1.100: whoami
usuario

* Shell~192.168.1.100: ls
arquivo1.txt
arquivo2.txt
diretorio/

* Shell~192.168.1.100: screenshot
[Screenshot capturado e salvo como screenshot0]

* Shell~192.168.1.100: upload importante.txt
[Arquivo enviado para a máquina alvo]

* Shell~192.168.1.100: exit
```

## 📝 Estrutura do Código

### **backdoor.py** (Cliente Backdoor)

**Funções principais:**
- `data_send(data)` - Envia dados em formato JSON
- `data_recv()` - Recebe dados em formato JSON
- `upload_file(file)` - Envia arquivo para o servidor
- `download_file(file)` - Recebe arquivo do servidor
- `screenshot()` - Captura screenshot da tela
- `shell()` - Loop principal que processa comandos remotos

### **c2.py** (Servidor)

**Funções principais:**
- `data_recv()` - Recebe dados do cliente
- `data_send(data)` - Envia comandos para o cliente
- `upload_file(file)` - Envia arquivo para o cliente
- `download_file(file)` - Recebe arquivo do cliente
- `t_commun()` - Loop de comunicação com o cliente

### **system.py** (Cliente Alternativo)

**Funções principais:**
- `connect(ip, port)` - Conecta ao servidor
- `receive_messages(client)` - Thread que recebe mensagens
- `main_loop(client)` - Loop de envio de mensagens

## 🔗 Dependências Externas

- **termcolor**: [https://pypi.org/project/termcolor/](https://pypi.org/project/termcolor/)
- **pyautogui**: [https://pypi.org/project/PyAutoGUI/](https://pypi.org/project/PyAutoGUI/)
- **Socket**: Biblioteca padrão do Python

## 📊 Fluxo de Comunicação

```
┌─────────────────────────────────────────────────────┐
│           SERVIDOR C2 (c2.py)                       │
│    Porta 4444 - Aguarda conexões                    │
│    Interface interativa do operador                 │
└──────────────┬──────────────────────────────────────┘
               │ Socket TCP
               │
┌──────────────▼──────────────────────────────────────┐
│         CLIENTE (backdoor.py/system.py)             │
│    Conecta ao servidor na porta 4444                │
│    Executa comandos remotamente                     │
│    Envia/recebe arquivos e screenshots              │
└─────────────────────────────────────────────────────┘
```

## ⚠️ Considerações de Segurança

1. **Sem criptografia** - A comunicação é em texto plano (JSON)
2. **Porta padrão** - Use portas não convencionais em produção
3. **Autenticação** - Não há mecanismo de autenticação implementado
4. **Firewall** - Certifique-se de configurar regras de firewall adequadas
5. **Logs** - Não há registro de atividades implementado

## 🎓 Propósito Educacional

Este projeto foi desenvolvido para fins educacionais, ajudando a entender:
- Comunicação via sockets em Python
- Execução remota de comandos
- Transferência de arquivos em rede
- Conceitos de C2 e infraestrutura maliciosa
- Segurança defensiva e análise de ameaças

## 📄 Licença

Este projeto não possui licença especificada.

## 👨‍💻 Autor

[deVictorS](https://github.com/deVictorS)

---

**Nota:** Este é um projeto exclusivamente educacional para fins de pesquisa em segurança ofensiva. O uso não autorizado é ilegal.
