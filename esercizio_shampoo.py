values = []
my_file = open("shamppo-dati","r")
for line in my_file:
 elements = line.split(',')
    if elements[0] != 'Date':
        date = elements [0]
        value = elements[1]
        values.append(float(value))


print (values)
def my_list_sum(the_list):
    sum = 0
    for item in the_list:
        sum = sum + item 
        print ("\t\t\t somma: {}".format(sum))
    print("\n La somma degli shamppo venduti negli ultimi tre anni corrisponde a: {}".format(sum))
my_list_sum(values)    





