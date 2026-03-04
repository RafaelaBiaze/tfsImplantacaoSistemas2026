# Documentação Técnica e de Segurança

## Permissões Aplicadas
Para seguir o princípio do menor privilégio (evitando `sudo` desnecessário), as seguintes configurações foram aplicadas no diretório `/var/www/technova`:
- **Owner (Usuário Atual):** O usuário que executa o script recebe a posse dos arquivos (`chown $USER`). Isso permite atualizar o site futuramente sem precisar usar credenciais de root.
- **Group (`www-data`):** O grupo padrão do Nginx tem permissão de leitura e execução.
- **CHMOD 750:** `rwxr-x---`. O dono pode ler, escrever e executar. O grupo (Nginx) pode ler e acessar as pastas. Outros usuários do sistema operacional estão bloqueados de ver os arquivos da empresa.

## Configurações do Nginx
- **Logs:** Logs isolados em `/var/log/nginx/technova_access.log` e `technova_error.log` para facilitar auditoria e debug.
- **Segurança de Rota:** A diretiva `try_files` protege o servidor garantindo que apenas arquivos existentes sejam servidos, direcionando rotas inválidas para a página `/404.html` sem vazar a estrutura de diretórios padrão.
- **Autostart:** O comando `systemctl enable nginx` foi executado para garantir alta disponibilidade, iniciando o servidor web automaticamente em caso de reinicialização do S.O.