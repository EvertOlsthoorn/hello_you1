import time

def beginstukje():
    time.sleep(1)
    print("MAI's LEVEN")
    print("                     ")
    time.sleep(1)
    print("Mai: Hallo, ik ben Mai. Ik heb net mijn tweede kind ter wereld gebracht en eindelijk, na twee dagen kan ik naar huis.")
    time.sleep(1)
    print("A. Ze gaan veilig naar huis.")
    print("B. Buurvrouw/vriendin belt het gezin op")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje2()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        beginstukje1()

def verhaalstukje2():
    time.sleep(1)
    print("Ze keert terug naar huis, met haar man en twee kinderen en leven verder")
    print("                     ")
    time.sleep(1)
    print("Mai: Mijn familie heeft geldproblemen en de enige manier om het op te lossen is door een familiering te verkopen, want anders worden we binnenkort uit huis geschopt. Wat moet ik doen?")
    time.sleep(1)
    print ("A. Familiering verkopen")
    print ("B. Familiering houden")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje4()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje5()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje2()

def verhaalstukje3():
    time.sleep(1)
    print("Mai: We zijn gebeld door onze buurvrouw en informeert over iets vreselijks. Het huis van onze buurman is vernield, met de buurman en buurmans dochter daarbinnen. Het huis van ons gezin is ook beschedigt en we mogen er niet meer binnenkomen. Alle hoop op een mooie toekomst is verloren")
    print("                     ")
    time.sleep(1)
    print ("A. Vluchten naar Nederland")
    print ("B. Naar familie")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje7()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje8()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje3()

def verhaalstukje4():
    time.sleep(1)
    print("Het leven gaat door")
    print("                     ")
    time.sleep(1)
    print("A. Familie gaat op een wandeling. Later worden ze gebeld door de buurvrouw.")
    print("B. Familie gaat op wandeling, maar word niet gebeld.")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje3()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje13()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje4()

def verhaalstukje5():
    time.sleep(1)
    print("Door armoede uit huis geschopt")
    print("                     ")
    time.sleep(1)
    print("A. Mai's gezin gaat naar het huis van familieleden om te blijven wonen")
    print("B. Mai's gezin gaat naar het huis van familieleden om te blijven wonen")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje8()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje8()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje5()

def verhaalstukje7():
    time.sleep(1)
    print("Vluchten naar Lochem, Nederland")
    print("                     ")
    time.sleep(1)
    print("A. Ze ging opzoek naar een taalschool in Lochem")
    print("b. Ze besloot direct online taallessen te volgen")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje14()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje16()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje7()

def verhaalstukje8():
    time.sleep(1)
    print("Ze zijn bij familie")
    print("                     ")
    time.sleep(1)
    print("A. Familie gaat op wandeltocht")
    print("B. Familie besluit die dag niet te wandelen, omdat het te hard regent")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje10()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje11()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje8()

def verhaalstukje10():
    print("Ze zijn bij familie")
    time.sleep(1)
    print("                     ")
    time.sleep(1)
    print("A. Familie wil eerst wegens vaderlandsliefde het land niet verlaten")
    print("B. Familie besluit dat het hier niet meer veilig is en vluchten weg")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje9()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje7()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje10()

def verhaalstukje9():
    time.sleep(1)
    print("Ze leven op straat")
    print("                     ")
    time.sleep(1)
    print("A. Familie is uiteindelijk gedwongen te besluiten dat leven in dit land geen leven is en besluiten toch te vluchten")
    print("B. Familie is uiteindelijk gedwongen te besluiten dat leven in dit land geen leven is en besluiten toch te vluchten")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje7()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje7()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje9()

def verhaalstukje11():
    time.sleep(1)
    print("Het huis word door een raket verwoest met het familie als slachtoffers")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje25()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje25()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje11()

def verhaalstukje12():
    time.sleep(1)
    print("Familie leeft nog lang en gelukkig")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje25()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje25()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje12()

def verhaalstukje13():
    time.sleep(1)
    print("Familie word oud en sterft in een gelukkig leven")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje24()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje24()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje13()

def verhaalstukje14():
    time.sleep(1)
    print("Er was geen taalschool in Lochem")
    print("                     ")
    time.sleep(1)
    print ("A. Je geeft op en besluit maar Engels te gaan leren")
    print ("B. Je besluit online Nederlands te leren")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje15()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje16()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje14()

def verhaalstukje15():
    time.sleep(1)
    print("Ze gaf op en besloot Engels te leren in plaats van Nederlands")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje17()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje17()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje15()

def verhaalstukje16():
    time.sleep(1)
    print("Mai leerde online Nederlands")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje17()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje17()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje16()

def verhaalstukje17():
    time.sleep(1)
    print("Ze werkt als verkoopster bij de Hema")
    print("                     ")
    time.sleep(1)
    print("A. Ze mist per ongeluk een aantal werkdagen door familierpoblemen, zonder af te bellen")
    print("B. Ze mist per ongeluk een aantal werkdagen door familierpoblemen, maar ze belt deze keer af")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje18()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje19()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje17()

def verhaalstukje18():
    time.sleep(1)
    print("Ze word ontslagen bij de Hema en word dan verkoopster bij het Kruidvat")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje20()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje20()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje18()

def verhaalstukje19():
    time.sleep(1)
    print("Ze heeft een goede werktijd bij de Hema")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje20()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje20()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje19()

def verhaalstukje20():
    time.sleep(1)
    print("Ze doet de opliding verkoopspecialist")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje21()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje21()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje20()

def verhaalstukje21():
    time.sleep(1)
    print("Twee jaar later doet Mai aan project 'Maakt Bemind'")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje22()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje22()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje21()

def verhaalstukje22():
    print("Ze publiceert haar verhaal over Syrie")
    print("                     ")
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje23()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje23()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje22()

def verhaalstukje23():
    time.sleep(1)
    print("Haar verhaal maakt een enorme impact op vele Nederlandsers")
    print("                     ")
    time.sleep(1)
    print("Klik op A of B om verder te gaan")
    antwoord= input("Maak een keuze, A of B? ")
    print("                ")
    if antwoord=="A" or antwoord=="a":
        verhaalstukje26()
    elif antwoord=="B" or antwoord=="b":
        verhaalstukje26()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje23()

def verhaalstukje24():
    time.sleep(1)
    print("EINDE")

def verhaalstukje25():
    time.sleep(1)
    print("EINDE")

def verhaalstukje26():
    time.sleep(1)
    print("EINDE")

beginstukje()
