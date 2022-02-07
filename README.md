# Esame-Laboratorio-Units-10-2-2022

Repository dedicato all appello del 10/02/2002 del Laboratorio di Programmazione gestito dal professor Sarusso. 
Corso di Inteligenza Artificiale e Data Analytics dell Università degli Studi di Trieste anno 2021/22.

In questo file README.md terrò traccia di tutte le modifiche apportate al programma, possibilmente passo dopo passo per garantire una corretta fluidità tra i vari aggiornamenti del codice.

Il codice è scritto, e verrà scritto, interamente il locale sulla mia macchina utilizzando VScode e le varie estensioni da esso fornito. Aggiungerò eventuali link per metodi e/o funzioni che troverò in internet.

**04/02/2022** 
> 18:34 - Inizio scrittura del codice.

> 19:05 - Caricato file esame.py con un primo tamplate. All'interno è stata create una classe "CSVFile" sulla base di quella fatta a lezione. Implementato l'utilizzo di @abstractmethod sull' "init" e sul "get_data" e creato una classe figlia "CSVFileTimeSeriesFile" con i rispettivi metodi. Definito il corpo del metodo "compute_avg_monthly_difference" e di un "main" per permettere una facile esecuzione in locale dei comandi. La stampa del file come lista di liste viene eseguito correttamente, come il "raise ExamException" in caso di file non trovato. Provo alcuni dubbi sull'utilizzo di @abstractmethod e di come è stata utilizzata la classe padre, anche se svolge il suo compito a regola d'arte. 

**05/02/2022**
> 18:18 - Finito la funzione che calcola la media, fatta in modo un po' rudimentale quindi sarà di sicuro soggetta a modifica. Modifica della classe "CSVFile" così da sfruttare al meglio l'ereditarietà. Molto velocemente, nella classe madre viene creata una lista di liste, la quale ritorna nella classe figlia dove il secondo elemento di ogni sotto lista viene trasformato ad intero. Per ora vi è in programma di modificare la classe della media e di creare una classe per il testig. Saranno da implementare tutti i vari errori, probabilmente verrà utilizzata una funzione per "sanificare" i dati. Darò una rilettura più approfondita all' intera consegna per evidenziare tutti i casi particolari consigiati dal professore. P.S. Vi è un vuoto tra ieri sera e sta sera causa febbre. Ho dovuto fermarmi 2-3 volte poichè non riuscivo a pensare.

**06/02/2022**

>18:10 - Aggiunti controlli relativi all'inserimento degli anni nella funzione avg. Controlli sul tipo di dato e convertibilità ad interi. pianifica in corso per il controllo del nome passato alla classe CSVFile e controllo su tutto il file preso in input.

**07/02/2022**

>17:55 - BIG UPDATE. Posto a distanza di un giorno dopo aver portato aggiornamento SOSTANZIALI al progetto. Elencherò passo per passo tutti i cambiamenti apportati e, nonostante mi piacerebbe ammetterlo, non sono tutte farina del mio sacco. Pubblicherò infatti i link delle pagine che mi hanno suggerito o fatto scoprire metodi molto utili.

1. Partendo dal codice che avevo pubblicato ieri sera mi sono messo a fare del testing, utilizzando il codice gentilmente fornito da un mio compagno che ha avuto la voglia di scrivere diversi test e dare un punteggio al risultato. Di seguito linko il suo repository. [testing.py](https://github.com/Jac-Zac/Programming_Lab_Exam_2022).
2. Subito dopo aver provato ad eseguire il testing, ho riscontrato dei problemi con i file che vengono passati alla classe CSV. Molto velocemente, Jac utilizza ``` with tempfile.NamedTemporaryFile('w+t') as file: ``` per creare un file temporaneo sotto %appdata% che riempirà con valori che poi verranno passato alla classe CSV. Questo funzionerebbe perfettamente se fossimo su un sistema unix-like... Purtroppo python ritorna un errore numero 13: permesso negato. Quest'ultimo è dovuto all'apertura del file dalla classe CSV mentre è già aperto come file temporaneo. Windows automaticamente blocca l'accesso e termina in modo critico il programma. Sono quindi intervenuto per riscrivere il file di testing utilizzando un file di supporto .csv che viene creato nella stessa cartella. Il testing viene eseguito correttamente senza nessun problema.
3. Passo successivo: RISTRUTTURARE. Salta subito all'occhio che l'ultima versione del programma che ho caricato che lavora solo in un ambiente quasi perfetto. Un singolo valore sballato e tutto va in errore. Mi sono quindi messo a risolvere un problema con un .strip() che restituiva un "index out of range"...... errore che non pensavo pottessere essere generato da un metodo del genere. Sostituito da un semplice ```.replace("\n","")```. Ho iniziato ad usare il metodo [isdigit](https://careerkarma.com/blog/python-isalpha-isnumeric-isalnum/#:~:text=The%20Python%20isnumeric()%20method,method%20returns%20the%20value%20False%20.) per verificare se la seconda colonna, teoricamente passata come stringa, fosse convertibile SOLO ad intero. Poi avrei dovuto verificare se fosse positivo ma anche se fosse stato una stringa prima di esso. Dopo decine di minuti passati a risolvere errori, cercare soluzioni e alternative ho capito che il mio sistema di if -> else era inconsistente. Stavo finendo col ritrovarmi in marea di if per controllare se la stringa era convertibile a intero, se era di un certo tipo, se rispettava una certa lunghezza. Riassumendo in una sola parola:"INUTILE". Sono quindi passato al costrutto ```try except```. LA MIGLIORE SELTA DEL GIORNO. Poichè il professore riciede di ignorare le righe in cui vi sono valori non computabili e alzare un errore solo con un timestamp, quello che mi basta fare è forzare una conversione della seconda colonna ad intero, verificare se l'intero sia positivo e se la prima colonna sia una data valida. Il controllo rimane in mano al try except, se il valore è errato scatterà un errore che farà slittare il programma alla prossima riga.
4. L'esame sta finalmete prendendo forma. Ho inizato a cercare un metodo per verificare se la prima colonna fosse una data valida e ho trovato 2 metodi. La prima è utilizzare il metodo [parse()](https://dateutil.readthedocs.io/en/stable/parser.html) della libbrearia "dateutil", mentre il secondo utilizza [strptime()](https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python) della libbrearia datetime. Ho provato entrambe e svolgono praticamente lo stesso compito. Ho scelto di utilizzare parse() per una scelta di estetica, anche se il secondo metodo l'ho lasciato commentato nel codice. Ho quindi creato una funizione di supporto chiamata, indovinate come, is_date(string). Quest'ultima prende in input una stringa e restituisce vero se la stringa è una data valida, falso di conseguenza.
5. Passiamo al prossimo controllo, quello più delicato: i timestamp. Nonostante sia un controllo delicato ho scelto un metodo molto semplice e basilare. Tutte le volte che prendo in considerazione una riga, valuto prima se la data è già presente tra i dati validati, e alzo un eccezione di conseguenza, poi se il record precedente è in ordine cronologico. (Grazie a python mi basta semplicemente confrontare le stringhe con un maggiore o minore). 
6. Ultimo ma non meno importante se la lista contiene almeno un valore. In caso contrario alzo un errore. Un semplice if not e via.

> Come potete ben notare ho completamente ribaltato il codice. Questo mi dovrà imporre di dover ribaltare anche il metodo avg. Per ora il testing mi permette un solido 26. Ho ancora qualche dubbio sullo skippare le righe delle tabelle, pensavo che forse sarebbe meglio semplicemente inserire uno 0 o un valore nullo così da non dover verificare la il mese nella stringa. Stavo anche pensando ci convertire l'intero esercizio in inglese, così per metterlo una spanna sopra gli altri.
