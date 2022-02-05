# Esame-Laboratorio-Units-10-2-2022

Repository dedicato all appello del 10/02/2002 del Laboratorio di Programmazione gestito dal professor Sarusso. 
Corso di Inteligenza Artificiale e Data Analytics dell Università degli Studi di Trieste anno 2021/22.

In questo file README.md terrò traccia di tutte le modifiche apportate al programma, possibilmente passo dopo passo per garantire una corretta fluidità tra i vari aggiornamenti del codice.

Il codice è scritto, e verrà scritto, interamente il locale sulla mia macchina utilizzando VScode e le varie estensioni da esso fornito. Aggiungerò eventuali link per metodi e/o funzioni che troverò in internet.

**04/02/2022** 
> 18:34 - Inizio scrittura del codice.

> 19:05 - Caricato file esame.py con un primo tamplate. All'interno ho creato una classe "CSVFile" sulla base di quella fatta a lezione. Ho implementato l'utilizzo di @abstractmethod sull' "init" e sul "get_data" e creato una classe figlia "CSVFileTimeSeriesFile" con i rispettivi metodi. Ho creato il corpo del metodo "compute_avg_monthly_difference" e di un "main" per permettermi una facile esecuzione in locale dei comandi. La stampa del file come lista di liste viene eseguito correttamente, come il "raise ExamException" in caso di file non trovato. Provo alcuni dubbi sull'utilizzo di @abstractmethod e di come ho utilizzato la classe padre, anche se svolge il suo compito a regola d'arte. 

**05/02/2022**
> 18:18 - Ho completato la funzione che calcola la media, fatta in modo un po' rudimentale quindi sarà di sicuro soggetta a modifica, anche se fa il suo lavoro. Ho modificato la classe "CSVFile" così da sfruttare al meglio l'ereditarietà. Molto velocemente, nella classe madre credo una lista di liste, nella figlia rendo il secondo elemento di ogni sotto lista un intero. Per ora ho in programma di modificare la classe della media e di creare una classe per il testig. Saranno da implementare tutti i vari errori, probabilmente utilizzerò una funzione per "sanificare" i dati. Darò una rilettura più approfondita all' intera consegna per evidenziare tutti i casi particolari consigiati dal professore. P.S. Vi è un vuoto tra ieri sera e sta sera causa febbre. Ho dovuto fermarmi 2-3 volte poichè non riuscivo a pensare.
