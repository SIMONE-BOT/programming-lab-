file = open("shamppo-dati", "r")
somma = 0
for line in file:
    a = line.split(",")
    try:
        somma += float(a[1])
    except Exception as e:
        print("scemo di merda\n {}".format(e))

print(somma)

