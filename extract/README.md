# Fehlerliste

Teilweise werden die Wörter mit Bindestrichen gebrochen. In einer Zeile steht dann am Ende "in seiner Woh-" und in der nächsten "nung. Und ". Wenn wir die Zeilen zusammen fügen müssen wir die Bindestriche am Ende der Wörter entfernen.

002
- keine Spalten

003
- "1 Im Buch: Mrs. Boggle"

008
- PolizistWird, PolizistVorsicht

015
- keine Spalten

023
- keine Spalten

057
- drei Spalten

107
- "REGIE","(lacht)","15" sollte eigentlich nicht REGIE sondern Person sein, passiert wenn "(lacht)" das einzige ist was in der Zeile hinter dem Namen steht, ließe sich vermeiden, in dem die Kursiverkennung vor dem Algorithmus läuft und Zeilen mit der Kursiv-Datenbank während des Alorithmus abgeglichen werden. So können Zeilen, die tatsächlich einen Sprecher haben aber sonst nur Kursiv troztdem dem Sprecher zugeordnet werden

187
- Seitenzahl ist nicht einfach nur die Nummer, sondern "- X -" (X markiert die Seitenzahl)

# Verbesserungsideen
- momentan checken wir Zeilen die KOMPLETT kursiv geschrieben sind erst nach dem Hauptalgorithmus als eine Art Cleaning
- besser wäre es die kursiven Zeilen vorher schon zu sammeln und im Hauptalgorithmus mit der aktuellen Zeile zu vergleichen
