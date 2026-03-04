# Fehlerliste

Teilweise werden die Wörter mit Bindestrichen gebrochen. In einer Zeile steht dann am Ende "in seiner Woh-" und in der nächsten "nung. Und ". Wenn wir die Zeilen zusammen fügen müssen wir die Bindestriche am Ende der Wörter entfernen.

001
- automatische Erkennung des speaker window failed, vllt. manueller override nötig?

002
- keine Spalten

003
- "1 Im Buch: Mrs. Boggle"

008
- PolizistWird, PolizistVorsicht

013
- in manchen Zeilen gibt es kein Leerzeichen zwischen Speaker Name und Text

014
- in manchen Zeilen gibt es kein Leerzeichen zwischen Speaker Name und Text

015
- keine Spalten

022
- automatische Erkennung des speaker window failed, vllt. manueller override nötig?

023
- keine Spalten

040
- irgendwas komisch

057
- drei Spalten

066
- irgendwas komisch

091
- irgendwas ist hier falsch, es werden gar keine Namen erkannt

102
- es werden kaum REGIE rows gefunden, vllt. Schriftart anders?

107
- "REGIE","(lacht)","15" sollte eigentlich nicht REGIE sondern Person sein, passiert wenn "(lacht)" das einzige ist was in der Zeile hinter dem Namen steht, ließe sich vermeiden, in dem die Kursiverkennung vor dem Algorithmus läuft und Zeilen mit der Kursiv-Datenbank während des Alorithmus abgeglichen werden. So können Zeilen, die tatsächlich einen Sprecher haben aber sonst nur Kursiv troztdem dem Sprecher zugeordnet werden

120
- es werden kaum REGIE rows gefunden, vllt. Schriftart anders?

121
- es werden zu viele Sachen der REGIE zugeordnet

137
- kann es sein dass die leerzeichen fehlen?

141
- irgendwas ist komisch

148
- irgendwas ist komisch

158
- irgendwas ist komisch

166
- alle Namen uppercase, konvertieren vor Check

169
- alle Namen uppercase, konvertieren vor Check

172
- alle Namen uppercase, konvertieren vor Check

173
- es werden kaum REGIE rows gefunden, vllt. Schriftart anders?

177
- alle Namen uppercase, konvertieren vor Check

187
- Seitenzahl ist nicht einfach nur die Nummer, sondern "- X -" (X markiert die Seitenzahl)

# Verbesserungsideen
- momentan checken wir Zeilen die KOMPLETT kursiv geschrieben sind erst nach dem Hauptalgorithmus als eine Art Cleaning
- besser wäre es die kursiven Zeilen vorher schon zu sammeln und im Hauptalgorithmus mit der aktuellen Zeile zu vergleichen
- Seite 14 oä., also "Seite" und dann eine Zahl erkennen und rauswerfen
- nach manchen Namen kommt ein Punkt ('.'), Semikolon (';'), Fragezeichen ('?'), Apostroph ('`') statt einem Doppelpunkt weil sich vertippt wurde -> müsste man abfangen
- character normalisation wär cool als pre-processing, gibt viele verschiedene versionen von Bindestrichen/Hyphens, Apostrophen usw., maybe use https://textacy.readthedocs.io/en/latest/

# Progress
- 21611 rows
- 18564 rows
- 13389 rows
- 10651 rows
- 08129 rows