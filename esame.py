#==============================
#  Librerie da importare
#==============================

from abc import ABC, abstractmethod

#==============================
#  Classe per le Exception
#==============================

class ExamException(Exception):
        pass

#==============================
#  Classe padre per file CSV
#==============================

class CSVFile(ABC):
    
    @abstractmethod
    def __init__(self,name) -> None:
        self.name = name

        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))

    @abstractmethod
    def get_data(self) -> list[list]:
        if not self.can_read:
            raise ExamException("Impossibile aprire il file")
        else:
            data = []
            my_file = open(self.name, 'r')

            for line in my_file:
                
                elements = line.split(',')
                data.append(elements)

            my_file.close()
            return data

#==============================
#  Classe figlia di CSV
#==============================

class CSVFileTimeSeriesFile(CSVFile):

    def __init__(self, name) -> None:
        super().__init__(name)

    def get_data(self) -> list[list]:
        data = super().get_data()

        elements = []
        for i in data:
            i[1] = int(i[1])
            elements.append(i)

        return elements

#==============================
#  Metodo per calcolare la media
#==============================

def compute_avg_monthly_difference(time_series, first_year, last_year) -> list[float]:

    if type(first_year) is not str:
        raise ExamException(f"First_year non è un valore computabile. Tipo di dato inserito: {type(first_year)}")
    if type(last_year) is not str:
        raise ExamException(f"Last_year non è un valore computabile. Tipo di dato inserito: {type(last_year)}")
    if first_year.isdigit() is False:
        raise ExamException(f"First_year non è un valore trasformabile ad intero. Valore inserito: {first_year}")
    if last_year.isdigit() is False:
        raise ExamException(f"Last_year non è un valore trasformabile ad intero. Valore inserito: {last_year}")

    data = [i[1] for i in time_series if int(i[0][:4]) >= int(first_year) and int(i[0][:4]) <= int(last_year)]
    years = int(last_year)-int(first_year)+1
    result = [[]for i in range(0,years)]    

    conta = 0

    for i in range(0,len(data)):
        if i != 0 and i % 12 == 0: 
                conta+=1
        result[conta].append(data[i])

    avg = []
    somma = 0
    for i in range(0,12):
        for j in range(1,years):
            somma += result[j][i] - result[j-1][i]
        avg.append(somma/(years-1)) 
        somma = 0
    
    return avg

#==============================
#  Main per eseguuire comandi in locale
#==============================

def main() -> None:
    file = CSVFileTimeSeriesFile("data.csv")

    print(compute_avg_monthly_difference(file.get_data(),"1949","1951"))

if __name__ == "__main__":
    main()