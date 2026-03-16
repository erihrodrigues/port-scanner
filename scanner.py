import nmap # Importa a biblioteca python-nmap para controlar o Nmap pelo Python
import pyfiglet # Importa a biblioteca que cria banners em ASCII
import os # Biblioteca para interagir com o sistema operacional
import json # Biblioteca para trabalhar com arquivos JSON
from datetime import datetime # Importa datetime para usar data e hora

def main(): # Função principal do programa
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Cria timestamp com data e hora para nomear arquivos

    os.makedirs("results", exist_ok=True) # Cria a pasta "results" se ela não existir

    banner = pyfiglet.figlet_format("Port Scanner", font="doom") # Cria um banner ASCII com o texto Port Scanner
    print(banner) # Exibe o banner no terminal

    print("Author: Erica Almeida") # Mostra o nome do autor
    print("Simple Nmap Automation Tool") # Mostra descrição do projeto
    print("----------------------------------") 

    nm = nmap.PortScanner() # Cria o objeto PortScanner que executa os scans com Nmap

    target = input("Enter target IP or domain: ") # Solicita ao usuário o IP ou domínio que será escaneado
    options = "-sV -sC" # Define argumentos que serão usados pelo Nmap
                        # -sV: detecta versão dos serviços nas portas
                        # -sC: executa scripts padrão do Nmap

    print(f"\nScanning target {target} ... please wait\n") # Mostra mensagem de início do scan

    try: # Bloco para capturar possíveis erros durante o scan
        nm.scan(target, arguments=options) # Executa o scan no alvo com as opções definidas
    except Exception as e: # Caso ocorra erro
        print("Error during scan:", e) # Mostra o erro
        return # Encerra a função

    print("\nScan Results") # Título da seção de resultados
    print("----------------------------------")

    print(f"Hosts found: {len(nm.all_hosts())}") # Mostra quantos hosts foram encontrados no scan

    filename = f"results/scan_{timestamp}.txt" # Define nome do arquivo TXT com timestamp
    json_filename = f"results/scan_{timestamp}.json" # Define nome do arquivo JSON com timestamp

    scan_results = { # Cria estrutura de dicionário para armazenar resultados
        "target": target, # Armazena o alvo escaneado
        "scan_time": timestamp, # Armazena horário do scan
        "arguments": options, # Armazena argumentos usados no Nmap
        "hosts": {}} # Estrutura onde serão guardados os hosts encontrados

    with open(filename, "w") as file: # Abre o arquivo TXT para escrita

        for host in nm.all_hosts(): # Percorre todos os hosts encontrados pelo Nmap

            scan_results["hosts"][host] = { # Cria entrada do host no JSON
                "hostname": nm[host].hostname(), # Nome do host
                "state": nm[host].state(), # Estado do host (up/down)
                "protocols": {}} # Estrutura para protocolos do host
                
            host_info = f"Host: {host} ({nm[host].hostname()})" # Cria string com IP e hostname
            state_info = f"State: {nm[host].state()}" # Cria string com estado do host

            print(host_info) # Mostra host no terminal
            print(state_info) # Mostra estado no terminal

            file.write(host_info + "\n") # Escreve host no arquivo TXT
            file.write(state_info + "\n") # Escreve estado no arquivo TXT

            for protocol in sorted(nm[host].all_protocols()): # Percorre protocolos encontrados (ex: tcp)

                protocol_info = f"Protocol: {protocol}" # Cria texto do protocolo
                print(protocol_info) # Mostra protocolo no terminal
                file.write(protocol_info + "\n") # Escreve protocolo no arquivo

                scan_results["hosts"][host]["protocols"][protocol] = {} # Cria estrutura do protocolo no JSON

                port_info = nm[host][protocol] # Pega informações das portas desse protocolo

                for port in sorted(port_info): # Percorre todas as portas encontradas

                    state = port_info[port]['state'] # Obtém estado da porta (open, closed, filtered)
                    service = port_info[port]['name'] # Obtém nome do serviço rodando na porta
                    product = port_info[port].get('product', '') # Obtém nome do software do serviço
                    version = port_info[port].get('version', '') # Obtém versão do software

                    version_info = f"{product} {version}".strip() # Junta produto e versão em uma string

                    line = f"Port: {port} | State: {state} | Service: {service} | Version: {version_info}" # Cria linha de resultado

                    print(line) # Mostra resultado da porta no terminal
                    file.write(line + "\n") # Escreve resultado da porta no arquivo TXT

                    scan_results["hosts"][host]["protocols"][protocol][port] = { # Salva dados da porta no JSON
                        "state": state,
                        "service": service,
                        "product": product,
                        "version": version }

    with open(json_filename, "w") as json_file: # Abre arquivo JSON para escrita
        json.dump(scan_results, json_file, indent=4) # Salva dicionário scan_results no JSON formatado

    print(f"\nTXT results saved to {filename}") # Informa onde o arquivo TXT foi salvo
    print(f"JSON results saved to {json_filename}") # Informa onde o JSON foi salvo
    print("\nScan completed successfully.") 

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    main() # Executa a função principal