# Zabbix LLD Maker

Script para criação de itens LLD para o Zabbix.

* Testado no Zabbix 2.2 e 4.0

Modo de utilização:

# Modo script

* Cria arquivo de configuração inicial (cuidado: Essa opção vai destruir todo o conteúdo do arquivo [se existir]):
<pre>/etc/zabbix/scripts/notify_lld.py startupconfig</pre>

* Cria um item:
<pre>/etc/zabbix/scripts/notify_lld.py createitem 1 "Exemplo" "Trigger de teste"</pre>

* Mostra na tela todos os itens criados:

<pre>/etc/zabbix/scripts/notify_lld.py discovery</pre>

* Exemplo de output:
<pre>{"data": [{"{#INFO}": "Exemplo", "{#STATUS}": "1", "{#DESC}": "Trigger de teste", "{#NID}": 1551885187}]}</pre>

* Deleta item:
<pre>/etc/zabbix/scripts/notify_lld.py deleteitem 1551885187</pre>

* Exemplo de output:
<pre>/etc/zabbix/scripts/notify_lld.py discovery
/etc/zabbix/scripts/notify_lld.py discovery
{"data": []}</pre>

#Modo LLD Zabbix

No arquivo de configuração do Zabbix ex:*/etc/zabbix/zabbix_agentd.conf* inserir a linha:

<pre>UserParameter=notify_lld[*],/etc/zabbix/scripts/notify_lld.py $1 $2 $3</pre>

* Reiniciar o Agente do Zabbix (sudo systemctl restart zabbix-agent)

Na interface web do Zabbix, criar/editar um host, configurar o agente no host, ir em *Regras de descoberta* e clicar em "Criar regra de descoberta". No nome colocar qualquer nome, na chave colocar: *notify_lld[discovery]*, no intervalo de atualização colocar 30 segundos (ou mais) e em *Manter dados de recursos perdidos por (em dias)* deixar o valor *1* (não é necessário mais do que isso.

Em *Protótipos de itens*, criar um item, exemplo: *#{#NID} - {#INFO} - {#DESC}* e na chave *notify_lld[status,{#NID}]*.

Em *Protótipos de trigger*, criar as triggers com as severidades correspondentes, exemplo:

* Nome:  #{#NID} [{#INFO}] - {#DESC}
* Expressão: {HOST:notify_lld[status,{#NID}].last()}=1

Defini que o status 1 é a severidade *Informação*. Você pode montar todas as outras triggers com as severidades desejadas.

Qualquer dúvida, por favor mandar e-mail para:

willian.o.jesus@gmail.com
