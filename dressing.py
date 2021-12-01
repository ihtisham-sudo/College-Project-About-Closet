print("        How I Get Dressed Up Every Morning?       ")
print("-----------------------------------")
print("I have to decide what should I wear Today hmm")
print("-----------------------------------")
print("Let's start")
print("-----------------------------------")
print("Firstly, I'll get up from my bed")
print("Then i'll go to the bathroom to take shower")
print("Then i'll get back to my closet to pick up my clothes")
print("There i'll decide which shirt I should wear")
sweatshirt = 'sweatshirt'
Teeshirt = 'Teeshirt'
checkshirt = 'checkshirt'
sweatshirt = input("Should I wear a sweatshirt? (y/n) \n")
Teeshirt = input("Should I wear a Teeshirt? (y/n) \n")
checkshirt = input("should I wear a checkshirt? (y/n) \n")

if ((sweatshirt == "y") and (Teeshirt != "y") and (checkshirt != "y")):
    print("I'll wear sweatshirt")
elif ((Teeshirt == "y") and (sweatshirt != "y") and (checkshirt != "y")):
    print("I'll wear Teeshirt")
elif ((checkshirt == "y") and (sweatshirt != "y") and (Teeshirt != "y")):
    print("I'll wear checkshirt")
else:
    print("Invalid Input")
print("-----------------------------------")
print("Great, Now I should choose Pants")
print("-----------------------------------")
Pant = 'Pant'
Jeans = 'Jeans'
Shorts = 'Shorts'
Pant = input("Should I wear a Pant? (y/n) \n")
Jeans = input("Should I wear a Jeans? (y/n) \n")
Shorts = input("Should I wear a Shorts? (y/n) \n")

if ((Pant == "y") and (Jeans != "y") and (Shorts != "y")):
    print("I'll wear Pant")
elif ((Jeans == "y") and (Pant != "y") and (Shorts != "y")):
    print("I'll wear Jeans")
elif ((Shorts == "y") and (Pant != "y") and (Jeans != "y")):
    print("I'll wear Shorts")
else:
    print("Invalid Input")
print("-----------------------------------")
print("Great, Now I should choose Shoes")
print("-----------------------------------")
Sneakers = 'Sneakers'
Flipflop = 'Flipflop'
Sandal = 'Sandal'
Sneakers = input("Should I wear a Sneakers? (y/n) \n")
Flipflop = input("Should I wear a Flipflop? (y/n) \n")
Sandal = input("Should I wear a Sandal? (y/n) \n")

if ((Sneakers == "y") and (Flipflop != "y") and (Sandal != "y")):
    print("I'll wear Sneakers")
elif ((Flipflop == "y") and (Sneakers != "y") and (Sandal != "y")):
    print("I'll wear Flipflop")
elif ((Sandal == "y") and (Sneakers != "y") and (Flipflop != "y")):
    print("I'll wear Sandal")
else:
    print("Invalid Input")
print("-----------------------------------")
print("Great, Now I should choose socks")
print("-----------------------------------")
BlueSocks = 'BlueSocks'
RedSocks = 'RedSocks'
BlackSocks = 'BlackSocks'
RedSocks = input("Should I wear a RedSocks? (y/n) \n")
BlueSocks = input("Should I wear a BlueSocks? (y/n) \n")
BlackSocks = input("Should I wear a BlackSocks? (y/n) \n")
if ((BlueSocks == "y") and (RedSocks != "y") and (BlackSocks != "y")):
    print("I'll wear BlueSocks")
elif ((RedSocks == "y") and (BlueSocks != "y") and (BlackSocks != "y")):
    print("I'll wear RedSocks")
elif ((BlackSocks == "y") and (BlueSocks != "y") and (RedSocks != "y")):
    print("I'll wear BlackSocks")
else:
    print("Invalid Input")
print("-----------------------------------")
print("Great, I have completed my dressing")
print("-----------------------------------")
