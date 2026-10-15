import json
from operator import itemgetter

def estrai_clienti()->list:
    
    #importo il file e lo salvo come lista di dizionari dentro clienti 
    with open("C:\\Users\\PC_161\\Documents\\GitHub\\PROVA\\es_19_03\\clienti.json", "r", encoding="utf-8") as f:
        clienti = json.load(f)

    return clienti


def ordina_priorita_2 (lista:list[dict])->list[dict]:
    
    key = 'priorita'
    lista_ordinata = []
    interlista = []

    #lista dei valori che puo assumere la priorita di un cliente 
    lista_priorita = [5,4,3,2,1]        

    #ordino in base alle priorita
    for cont in lista_priorita:

        #scorro i dizionari 
        for elm in lista:
            #se il contatore è uguale al valore di priorita aggiungi il dizionario alla nuova lista,
            # ad ogni ciclo 'for cont in lista_priorita:' verranno aggiunti alla nuova lista prima le priorita '5', poi '4', ecc.
            if cont == elm[key]:

                interlista.append(elm)
        interlista = ordina_patrimonio(interlista)
        for elm in interlista:
            lista_ordinata.append(elm)
        interlista = []

    return lista_ordinata

def ordina_patrimonio(lista:list[dict])->list[dict]:

    key = 'patrimonio'

    for  i in range(len(lista)):
        for j in range (len(lista)):

            if lista[j][key] < lista[i][key]:
                temp = lista[i]
                lista [i] = lista[j]
                lista [j] = temp

    return lista

def ordina_priorità(lista:list[dict])->list[dict]:
    
    lista_ordinata = sorted(lista, key=itemgetter("priorita", "patrimonio"), reverse= True)
            
    return lista_ordinata

def inserisci_utente(lista:list[dict])->list[dict]:

    diz = {}

    for elm in lista[0]:

        valore = input(f"inserisci {elm} del nuovo utente\n")
        diz[elm] = valore

    lista.append(diz)
    return lista
    

        

def main()->None:
    
    #lista con i dati estratti dal file 
    clienti = estrai_clienti()
    
    #priorita_moduli = ordina_priorità(clienti)

    #funzione che ordina in modo decrescete le priorita dei vari clienti 
    priorita = ordina_priorita_2(clienti)
    
    print (f"LA LISTA ORDINATA è:\n\n{patrimoni}\n\n")

    #inserimento utente 
    nuovo_utente = inserisci_utente(patrimoni)
    lista_aggiornata = ordina_priorita_2(nuovo_utente)
    lista_aggiornata_finale = ordina_patrimonio(lista_aggiornata)
    print (f"LA LISTA ORDINATA AGGIORNATA è:\n\n{lista_aggiornata_finale}\n\n")

if __name__ == "__main__":
    main()