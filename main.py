import re
from flask import Flask
from flask import request, render_template
from var_dump import var_dump
import json
import csv


studenti=[]

app = Flask(__name__)

data = 0

#--------------------------- Route / ALL ---------------------------------------------

@app.route('/')
def index():
    """
    Metoda která nám umožnuje být na Indexu stránky - Spuštění
    """
    return render_template("index.html")#vrací na stránku +++

@app.route('/index.html')
def index2():
    """
    Metoda která nám umožnuje být na Indexu stránky
    """
    return render_template("index.html")#vrací na stránku


@app.route('/registrace.html')
def moje_zkouska():
    """
    Metoda která nám umožnuje být na registrace.html
    """
    return render_template('registrace.html')#vrací na stránku
#---------------------------
@app.route('/vypis.html', methods=['GET'])
def vypis():
    """
    Metoda čte data CSV a zapisuje je do Listu,
        List se filtruje do listů podle tříd a posílají se na vypis.html   

    """
    studenti2 = []
    with open('Data/tabulka.csv') as soubor:
        Cteni_csv = csv.reader(soubor, delimiter=',')
        for bunka in Cteni_csv:
            studenti2.append(bunka)
    
    a4 = []       
    for x in studenti2:
        if(x[2]=="A4"):
            a4.append(x)        

    e4 = []       
    for x in studenti2:
        if(x[2]=="E4"):
            e4.append(x)
    
    c4a = []       
    for x in studenti2:
        if(x[2]=="C4a"):
            c4a.append(x)

    c4b = []       
    for x in studenti2:
        if(x[2]=="C4b"):
            c4b.append(x)

    a3 = []       
    for x in studenti2:
        if(x[2]=="A3"):
            a3.append(x)
    
    e3 = []       
    for x in studenti2:
        if(x[2]=="E3"):
            e3.append(x)

    c3 = []       
    for x in studenti2:
        if(x[2]=="C3"):
            c3.append(x)

    a2 = []       
    for x in studenti2:
        if(x[2]=="A2"):
            a2.append(x)
    e2 = []       
    for x in studenti2:
        if(x[2]=="E2"):
            e2.append(x)
    
    c2 = []       
    for x in studenti2:
        if(x[2]=="C2"):
            c2.append(x)

    a1 = []       
    for x in studenti2:
        if(x[2]=="A1"):
            a1.append(x)

    e1 = []       
    for x in studenti2:
        if(x[2]=="E1"):
            e1.append(x)

    c1 = []       
    for x in studenti2:
        if(x[2]=="C1"):
            c1.append(x)
    
    
            
    

    return render_template('vypis.html', ucastnici=studenti2, ca4=a4, ce4=e4, cc4a=c4a, cc4b=c4b, ca3=a3, ce3=e3, cc3=c3, ca2=a2, ce2=e2, cc2=c2, ca1=a1, ce1=e1, cc1=c1 ), 200   #vraci na stranku + posila list



#--------------------------- POST / Kontrola / List ---------------------------------------------

@app.route("/check.html", methods=["GET","POST"])
def check():
    """
    Check kontroluje příchozí imput data z formuláře na stránce registrace.html
    """    

    #inputs
    je_plavec = (request.form["je_plavec"])
    kanoe_kamarad = request.form["kanoe_kamarad"]

    jm = request.form["jm"]
    prj = request.form["prj"]
    trida = request.form["trida"]

    #Kontrola
    if ((je_plavec == "1") or (je_plavec == 1)):
        je_plavec = True
    else:
        je_plavec = False
    if je_plavec == False:
        return render_template("400.html")#vrací na stránku error plavec
    if not re.search("^[a-zA-Z0-9]{2,20}$", jm):
        return render_template("400.html")#vrací na stránku error jmeno
    if not re.search("^[a-zA-Z0-9]{2,20}$", prj):
        return render_template("400.html")#vrací na stránku error prijmeni
    
    if ((not re.search("^[a-zA-Z0-9]{2,20}$", kanoe_kamarad))):
        bez = str("bez kamarada")
        studenti.append([jm, prj, trida, je_plavec, bez])#pridani do listu 
                #return render_template("400.html")#vrací na stránku error
    else:
        studenti.append([jm, prj, trida, je_plavec, kanoe_kamarad])#pridani do listu         
                #return render_template("400.html")#vrací na stránku error
    
    

    file = open('Data/tabulka.csv', 'a+', newline ='')
    with file:
        write = csv.writer(file)
        write.writerows(studenti)
    """
    Import Studenta do listu a poté do CSV
    """
        
    studenti.clear()
    """
    List se vyčistí, aby se neduplikovali data do CSV
    """

    return render_template("200.html")#vrací na stránku c

#------------------------------------------------------------------------



#------------------------------------------------------------------------
#------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)