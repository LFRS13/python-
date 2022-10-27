
iphone = 2980
sansung = 2540
tablet = 1950
ps5 = 2100
notebook = 2350

qtdiphone = int(input("digite a quantida de iphone"))
qtdsansung = int(input("digite a quantidade de sansung"))
qtdtablet = int(input("digite a quantidade de tablete"))
qtdps5 = int(input("digite a quantidade de ps5"))
qtdnotebook = int(input("digite a quantidade de notebook"))

valortotal = (qtdiphone*iphone)+(qtdsansung*sansung)+(qtdtablet*tablet)+(qtdps5*ps5)+(qtdnotebook*notebook)
print (valortotal)
valordaparcela3x = (valortotal/3)
print ( valortotal/3)
valordaparcela = (valortotal * (5/100)+valortotal)/6
print (valordaparcela)
valordesconto = (valortotal-(valortotal*(10/100)))
print (valordesconto)

