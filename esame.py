#==============================
#  Librerie da importare
#==============================

from abc import ABC, abstractmethod
from dateutil.parser import parse
#import datetime

#==============================
#  Classe per le Exception
#==============================

class ExamException(Exception):
        """Classe creata apposta per poter alzare eccezioni di errori rilevati durante l'eseczione del programma"""
        pass

#==============================
#  Classe padre per file CSV
#==============================

class CSVFile(ABC):
    
    @abstractmethod
    def __init__(self,name) -> None:
        """Metodo costruttore. Crea un instanza del file per verificare se è possibile aprirlo.
        Se non è possibile setta una variabile a 'False' così da alzare un Exception nel get_data()
        """
        if type(name) is not str:
            raise ExamException(f"Name non è una stringa. Tipo di dato inserito: {type(name)}")

        self.name = name

        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()

        except Exception:
            self.can_read = False

    @abstractmethod
    def get_data(self) -> list[list]:
        """Metodo che trasforma, se leggibile, il file da csv a lista di liste"""
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

class CSVTimeSeriesFile(CSVFile):

    def __init__(self, name) -> None:
        super().__init__(name)

    def is_date(self,string) -> bool:
        """Metodo di supporto per verificare se la stringa passata sia una data computabile"""
        try:
            parse(string)
            return True
        except ValueError:
            return False

        # format = "%Y-%m"
        # try:
        #     datetime.datetime.strptime(string, format)
        #     return True
        # except ValueError:
        #     return False
        # except TypeError:
        #     return False;

    def get_data(self) -> list[list]:
        """Metodo che, utilizzando il risultato della classe padre, prende la lista di liste ed effettua tutti i controlli necessari"""
        unclean_data = super().get_data()

        clean_data = []
        for i in unclean_data:

            # if i[0] != "data":
            #     i[1].replace("\n","")
            #     if i[1].isdigit():
            #         i[1] = int(i[1])
            #         clean_data.append(i[0:2])
            #     else:
            #         i[1] = 0
            #         clean_data.append(i[0:2])

            if i[0] != 'date':
                try:
                    if not self.is_date(str(i[0])) or int(i[1]) < 0:
                        continue
                except:
                    continue

                if clean_data:
                    for j in clean_data:
                            prev_date = j[0]
                            if i[0] == prev_date:   
                                raise ExamException("Rilevato record di timestamp duplicato")

                    prev_date = clean_data[-1][0]
                    if i[0] < prev_date:
                        raise ExamException("Rilevato record di timestamp non ordinato")

                clean_data.append([i[0],int(i[1])])

        if not clean_data:
            raise ExamException("File vuoto o errato")

        return clean_data

#==============================
#  Metodo per sanificare i dati
#==============================

def sanitize(time_series, first_year, last_year):
    if not isinstance(first_year,str):
        raise ExamException(f"First_year non è un valore computabile. Tipo di dato inserito: {type(first_year)}")
    if not isinstance(last_year,str):
        raise ExamException(f"Last_year non è un valore computabile. Tipo di dato inserito: {type(last_year)}")
    if first_year.isdigit() is False:
        raise ExamException(f"First_year non è un valore trasformabile ad intero. Valore inserito: {first_year}")
    if last_year.isdigit() is False:
        raise ExamException(f"Last_year non è un valore trasformabile ad intero. Valore inserito: {last_year}")
    if first_year >= last_year:
        raise ExamException("Il valore di last_layer e/o di first_layer è inesatto")
    if not isinstance(time_series,list):
        raise ExamException(f"Time_series non è una lista di liste. Valore passato: {time_series}")
    if first_year < time_series[0][0][:4]:
        raise ExamException("First_year non è presente all'interno del file")
    if last_year > time_series[-1][0][:4]:
        raise ExamException("Last_year non è presente all'interno del file")

#==============================
#  Metodo per calcolare la media
#==============================

def compute_avg_monthly_difference(time_series, first_year, last_year) -> list[float]:

    sanitize(time_series,first_year,last_year)

    data = []

    count = 1
    current_year = int(time_series[0][0][:4])
    for i in time_series:
        
        if i[0][5:8] == "01" and count >= 13:
            current_year = int(i[0][:4])
        
        if count >= 13: 
                count = 1
                current_year = int(i[0][:4])
        elif int(i[0][:4]) != current_year and count <= 12:
            for count in range(count,13):
                data.append(0)
            count = 1
            current_year = int(i[0][:4])
        
        if i[0][:4] >= first_year and i[0][:4] <= last_year:
            if int(i[0][5:8]) != count:
                for count in range(count,int(i[0][5:8])):
                    data.append(0)
                data.append(i[1])
                count = count + 2
            else:
                data.append(i[1])
                
                count = count + 1
                
        if(current_year > int(last_year)):
            break        

    final_data = []

    years = int(len(data)/12)

    for i in range(12):
        count = 0
        somma = 0

        for j in range(1,years):
        #     years_sum += (data[i + (12*j)] - data[i + (12*(j-1))])

            if (data[i+(12*j)] == 0 or data[i+(12*(j-1))] == 0) and years == 2:
                somma = 0
            else: 
                if (data[i+(12*j)] == 0 or data[i+(12*(j-1))] == 0) and years > 2:
                    count += 1
                    if(years - count < 2):
                        somma = 0
                        j = years
                    else:
                        somma += 0
                else:
                    somma += data[i+(12*j)] - data[i+(12*(j-1))]
        try:
            final_data.append(somma/(years-1-count))
        except:
            final_data.append(0)

    return final_data

#==============================
#  Main per eseguuire comandi in locale
#==============================

def main() -> None:
    file = CSVTimeSeriesFile('data.csv')
    #print(file.get_data()[:124])
    print(compute_avg_monthly_difference(file.get_data(),"1949","1951"))

if __name__ == '__main__':
    main()