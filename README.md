# CiFlask

Questa applicazione consente di cifrare qualsiasi testo tu desideri scegliendo una tua chiave

## Prerequisiti

Per usare questo programma hai bisogno di:

- **MacO or Linux**
- **Python** (version 3.6 or higher).

## Installazione

1. Clona la repository:
```bash
   git clone https://github.com/
   cd CiFlask
   ```
2. Installa i requisiti:

- **MacOs**
```zsh
   pip3 install -r requirements.txt
   ```

- **Linux**
```bash
   pip install -r requirements.txt
   ```
   
## Utilizzo

To run CiFlask esegui da terminale:
- **MacOs**
```zsh
   flask --app CiFlask.py run
   ```
- **Linux**
```bash
   flask --app CiFlask.py run
   ```
Sarà necessario (una volta eseguito il programma) aprire il tuo browser e scrivere nella barra URL quanto segue "127.0.0.1:5000".
Una volta fatto ciò ti verrà chiesto di:
1. **"Cifrare"** o **"Decifrare"**
2. Scegli il cifrario da usare tra: **Cesare**,**Sostituzione** o **Vigenere**:
3. Alla fine inserisci il testo da cifrare(decifrare) con la sua chiave personale ed è pronto 

## Attenzione

Questo programma apre(di default) la porta 5000 del tuo computer ma lasciando così come è il codice nessuno apparte il tuo computer potrà vederlo.
Se hai intenzione di far vedere anche alle altre persone presenti nella **tua rete** allora dovrai eseguire:
```bash
   flask --app Test8.py run --host 0.0.0.0
   ```
Naturalmente questo renderà possibile alle altre persone di connettersi al tuo computer per poter vedere il sito. Ma è da tenere in considerazione eventuali problemi di sicurezza.
Io non sarò responsabile di alcun tipo di problema che potrà essere causato dal mio programma. La responsabilità sarà totalmente di chi lo vorrà utilizzare
## Contributi

Sono ben accetti aiuti di risoluzione di eventuali problemi, se trovi bug o hai da condividere dei suggerimenti, per favore apri una segnalazione o invia una richiesta di pull.


