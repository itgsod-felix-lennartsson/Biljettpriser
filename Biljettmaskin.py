from data.functions import priskoll

price = priskoll(raw_input("Var god ange alder: ")) # Tar input från användare om dess ålder och skickar vidare till functions/priskoll.
if price == "err": # Kollar om errormeddelande för att åldern inte är 0-130 år är givet.
    print("ERROR: Alder maste vara mellan 0 - 130 ar!")
else: # Kod nedan körs förutsatt att error ovan inte är givet.
    print "Din biljett kostar: " + str(price) + " kr." # Skriver ut kostnaden för användarens biljett. Pris förvaras i price, vilken defineras av functions/priskoll ovan.