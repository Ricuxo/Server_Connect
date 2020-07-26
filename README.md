Uma classe para conexão com servidor para envio de comandos. A intenção é utilizar a outra classe https://github.com/Ricuxo/OracleDB_Connect e criar um check list para banco de dados.

### Dependências

* paramiko 

### Exemplo de utilização

```python
from conn_server import SSH

host = '192.168.0.150'
souser = 'root'
sopass = 'oracle'
ssh = SSH(host=host, username=souser, passwd=sopass)
cmd = "ls -ltr /tmp"
result = ssh.exec_cmd(host, cmd)
print(result)
```

### Exemplo da saída

```python
PS D:\OneDrive\DESENVOLVIMENTOS\WORK\CHECKLIST_BANCO> python .\test.py
total 0
drwx------. 2 root   root     6 Jul 25 15:07 vmware-root_1115-4022177631
drwx------. 2 root   root     6 Jul 26 15:03 vmware-root_1098-2722239121
drwx------. 2 root   root     6 Jul 26 15:44 vmware-root_1091-4021784385
drwxr-xr-x. 2 oracle oinstall 6 Jul 26 15:45 hsperfdata_oracle
```

### Observação

* Todas as variáveis devem ser alteradas.
* Nesse exemplo estou enviando comandos com o usuário root, não é o recomendado

Para mais exemplos acesse: http://hsslab.com.br/
