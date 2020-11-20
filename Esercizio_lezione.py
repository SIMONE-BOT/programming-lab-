class CSVFile:
    
    def __init__(self,name):
        self.name = name
    def get_data(self):
        
        values = []
        my_file = open(self.name, "r")
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                
                date = elements [0]
                value = elements[1]
                values.append(float(value))
        return values
    pass            



mio_file = CSVFile("shamppo-dati") 


print (mio_file.get_data())




