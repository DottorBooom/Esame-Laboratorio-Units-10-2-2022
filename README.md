# Esame-Laboratorio-Units-10-2-2022

Repository dedicato all appello del 10/02/2002 del Laboratorio di Programmazione gestito dal professor Sarusso. 
Corso di Inteligenza Artificiale e Data Analytics dell Università degli Studi di Trieste anno 2021/22.

In questo file README.md terrò traccia di tutte le modifiche apportate al programma, possibilmente passo dopo passo per garantire una corretta fluidità tra i vari aggiornamenti del codice.

Il codice è scritto, e verrà scritto, interamente il locale sulla mia macchina utilizzando VScode e le varie estensioni da esso fornito. Aggiungerò eventuali link per metodi e/o funzioni che troverò in internet.

**04/02/2022** 
> 18:34 - Inizio scrittura del codice.

> 19:05 - Caricato file esame.py con un primo tamplate. All'interno ho creato una classe "CSVFile" sulla base di quella fatta a lezione. Ho implementato l'utilizzo di @abstractmethod sull' "init" e sul "get_data" e creato una classe figlia "CSVFileTimeSeriesFile" con i rispettivi metodi. Ho creato il corpo del metodo "compute_avg_monthly_difference" e di un "main" per permettermi una facile esecuzione in locale dei comandi. La stampa del file come lista di liste viene eseguito correttamente, come il "raise ExamException" in caso di file non trovato. Provo alcuni dubbi sull'utilizzo di @abstractmethod e di come ho utilizzato la classe padre, anche se svolge il suo compito a regola d'arte. 
