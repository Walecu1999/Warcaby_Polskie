Link do repozytorium: https://github.com/Walecu1999/Warcaby_Polskie/
5.  Warcaby Stupolowe, (zwane tak¿e Warcabami Polskimi) dyscyplina sportowa bêd¹ca miêdzynarodow¹ odmian¹ znanej gry planszowej – warcaby.
Powsta³a we Francji w pierwszej po³owie XVIII wieku, a jej g³ówn¹ ró¿nic¹ od warcabów standardowych jest zwiêkszony rozmiar planszy z 64 do 100 pól.
Opis zadania
0 Okno z siatk¹ przycisków 8x8 oraz przyciskiem do resetowania gry.
0 Przyciski reprezentuj¹ pola planszy do gry w warcaby. Pola puste - przyciski bez
tekstu. Pola z pionkami gracza 1 - przycisk z tekstem “C”. Pola z pionkami gracza
2 - przycisk z tekstem “B”. Damki oznaczane s¹ dodatkow¹ liter¹ d (“Cd”, “Bd”).
0 Nad plansz¹ wyœwietlana jest informacja “Tura gracza 1” lub “Tura gracza 2”.
0 Gracz wybiera pionka (tekst pola zmienia siê z “C” na “[C]” lub z “B” na “[B]”), a
potem pole na które chce wykonaæ ruch. Jeœli ruch jest dozwolony, pionek jest
przestawiany. Jeœli nie, to wyœwietlany jest komunikat “ruch niedozwolony”.
0 Zasady jak w warcabach (https://pl.wikipedia.org/wiki/Warcaby, dowolny
wariant). Zwyk³e pionki i damki maj¹ byæ obiektami dwóch ró¿nych klas
dziedzicz¹cych po klasie Pionek.
0 Gdy gra siê koñczy, wyœwietlane jest okienko z napisem “Wygra³ gracz 1” lub
“Wygra³ gracz 2”, zale¿nie kto wygra³ grê. Mo¿liwe jest zresetowanie planszy
bez zamykania g³ównego okna.
Testy
1. Wykonanie po dwa ruchy przez ka¿dego z graczy.
2. Niepowodzenie b³êdnego ruchu pionkiem.
3. Wykonanie bicia pojedynczego pionka.
4. Wykonanie bicia przynajmniej dwóch pionków.
5. Zamiana pionka w damkê.
6. Bicie damk¹.
7. Wygrana gracza graj¹cego czarnymi pionkami.
8. Rozpoczêcie nowej gry po zwyciêstwie jednego z graczy.
Wskazane jest przygotowanie specjalnych pocz¹tkowych rozstawieñ pionków dla testów
d, e, f, g, h.