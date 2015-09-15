from data.functions import priskoll

price = priskoll(raw_input("Var god ange alder: "))
if price == "err":
    print("ERROR: Alder maste vara mellan 0 - 130 ar!")
else:
    print "Din biljett kostar: " + str(price) + " kr."