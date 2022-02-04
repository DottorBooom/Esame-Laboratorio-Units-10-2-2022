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
    def get_data(self):
        if not self.can_read:
            raise ExamException("Impossibile aprire il file")
        else:
            data = []
            my_file = open(self.name, 'r')

            for line in my_file:
                
                elements = line.split(',')
                elements[1] = int(elements[1])
                data.append(elements)

            my_file.close()
            return data

#==============================
#  Classe figlia di CSV
#==============================

class CSVFileTimeSeriesFile(CSVFile):

    def __init__(self, name) -> None:
        super().__init__(name)

    def get_data(self):
        return super().get_data()
#==============================
#  Metodo per calcolare la media
#==============================

def compute_avg_monthly_difference(time_series, first_year, last_year) -> list[float]:
    pass

#==============================
#  Main per eseguuire comandi in locale
#==============================

def main() -> None:
    file = CSVFileTimeSeriesFile("data.csv")
    print(file.get_data())

if __name__ == "__main__":
    main()