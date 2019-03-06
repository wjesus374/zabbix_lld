#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import json
import pprint
import time

import sys

pp = pprint.PrettyPrinter(indent=4)

def readconf(configfile):
    configfile = configfile
    with open(configfile, "r") as jsonfile:
        data = json.load(jsonfile)

    return data

def writeconf(configfile,data):
    configfile = configfile
    data = data

    with open(configfile,"w", encoding="utf8") as outfile:
        json.dump(data, outfile, ensure_ascii=False)

def startupconfig(configfile):
    configfile = configfile
    #Data dict
    zbxdata = {}
    zbxdata["data"] = []

    with open(configfile,"w", encoding="utf8") as outfile:
        json.dump(zbxdata, outfile, ensure_ascii=False)

def createitem(data,info,desc,status):
    zbxdata = data
    zbxinfo = info
    zbxdesc = desc
    zbxstatus = status

    #print("Criando novo item")
    #zbxdata["data"].append({"{#NID}": int(time.time()), "{#INFO}": "Item de teste", "{#DESC}": "Descrição do item", "{#STATUS}" : 1})
    zbxdata["data"].append({"{#NID}": int(time.time()), "{#INFO}": zbxinfo, "{#DESC}": zbxdesc, "{#STATUS}" : zbxstatus})
    return zbxdata

def deleteitem(data,nid):
    zbxdata = data
    nid = int(nid)

    #for info in zbxdata["data"]:
    #    if str(info["{#NID}"]) == str(nid):
    #        print(info)
    #        info.clear()
    #        #del info["{#NID}"]

    for i in range(len(zbxdata["data"])):
         if zbxdata["data"][i]["{#NID}"] == nid:
            del zbxdata["data"][i]
            break

    return zbxdata

def help():
    print("===AJUDA===")
    print("* Criar arquivo de controle inicial [ZERA O ARQUIVO]:")
    print("notify_lld.py startupconfig")
    print("* Criar item:")
    print("notify_lld.py createitem 1 [número da severidade] \"INFORMAÇÃO\" \"DESCRIÇÃO\"")
    print("* Deletar item:")
    print("notify_lld.py deleteitem 123456789 [número do ID do item]")
    print("* Verificar status do item:")
    print("notify_lld.py status 123456789 [número do ID do item]")

if __name__ == "__main__":

    if sys.argv[1] == "discovery":
        #Ler configurações existentes
        data = readconf("/tmp/zbxnotify.json")
        #Print data
        #pp.pprint(data)
        #print(data)
        print(json.dumps(data,ensure_ascii=False))

    if sys.argv[1] == "startupconfig":
        #Criar arquivo de configuração inicial
        startupconfig("/tmp/zbxnotify.json")

    if sys.argv[1] == "createitem":
        try:
            status = sys.argv[2]
            info = sys.argv[3]
            desc = sys.argv[4]
            #Ler configurações existentes
            data = readconf("/tmp/zbxnotify.json")
            #Criar novo item
            cdata = createitem(data,info,desc,status)
            #Gravar novo item
            writeconf("/tmp/zbxnotify.json",cdata)
        except NameError as e:
            print(e)
        except IndexError as e:
            print("===ERRO===")
            print("Mensagem: [%s]" %(e))
            help()

    if sys.argv[1] == "deleteitem":
        try:
            nid = int(sys.argv[2])
            #Ler configurações existentes
            data = readconf("/tmp/zbxnotify.json")
            #Deletar item
            ddata = deleteitem(data,nid)
            #Gravar modificações
            writeconf("/tmp/zbxnotify.json",ddata)
        except NameError as e:
            print("===ERRO===")
            print("Mensagem: [%s]" %(e))
            help()

    if sys.argv[1] == "status":
        try:
            status = 9
            nid = int(sys.argv[2])
            #Ler configurações existentes
            data = readconf("/tmp/zbxnotify.json")
            #Print status
            for i in range(len(data["data"])):
                if data["data"][i]["{#NID}"] == nid:
                    #print(nid)
                    status = data["data"][i]["{#STATUS}"]
                    #print(data["data"][i]["{#STATUS}"])
                    break

            if status != 9:
                print(data["data"][i]["{#STATUS}"])
            else:
                print(status)

        except NameError as e:
            print("===ERRO===")
            print("Mensagem: [%s]" %(e))
            help()

    if sys.argv[1] == "help":
            help()
