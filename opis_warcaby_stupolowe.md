Link do repozytorium: https://github.com/Walecu1999/Warcaby_Polskie/
5.  Warcaby Stupolowe, (zwane tak�e Warcabami Polskimi) dyscyplina sportowa b�d�ca mi�dzynarodow� odmian� znanej gry planszowej � warcaby.
Powsta�a we Francji w pierwszej po�owie XVIII wieku, a jej g��wn� r�nic� od warcab�w standardowych jest zwi�kszony rozmiar planszy z 64 do 100 p�l.
Opis zadania
0 Okno z siatk� przycisk�w 8x8 oraz przyciskiem do resetowania gry.
0 Przyciski reprezentuj� pola planszy do gry w warcaby. Pola puste - przyciski bez
tekstu. Pola z pionkami gracza 1 - przycisk z tekstem �C�. Pola z pionkami gracza
2 - przycisk z tekstem �B�. Damki oznaczane s� dodatkow� liter� d (�Cd�, �Bd�).
0 Nad plansz� wy�wietlana jest informacja �Tura gracza 1� lub �Tura gracza 2�.
0 Gracz wybiera pionka (tekst pola zmienia si� z �C� na �[C]� lub z �B� na �[B]�), a
potem pole na kt�re chce wykona� ruch. Je�li ruch jest dozwolony, pionek jest
przestawiany. Je�li nie, to wy�wietlany jest komunikat �ruch niedozwolony�.
0 Zasady jak w warcabach (https://pl.wikipedia.org/wiki/Warcaby, dowolny
wariant). Zwyk�e pionki i damki maj� by� obiektami dw�ch r�nych klas
dziedzicz�cych po klasie Pionek.
0 Gdy gra si� ko�czy, wy�wietlane jest okienko z napisem �Wygra� gracz 1� lub
�Wygra� gracz 2�, zale�nie kto wygra� gr�. Mo�liwe jest zresetowanie planszy
bez zamykania g��wnego okna.
Testy
1. Wykonanie po dwa ruchy przez ka�dego z graczy.
2. Niepowodzenie b��dnego ruchu pionkiem.
3. Wykonanie bicia pojedynczego pionka.
4. Wykonanie bicia przynajmniej dw�ch pionk�w.
5. Zamiana pionka w damk�.
6. Bicie damk�.
7. Wygrana gracza graj�cego czarnymi pionkami.
8. Rozpocz�cie nowej gry po zwyci�stwie jednego z graczy.
Wskazane jest przygotowanie specjalnych pocz�tkowych rozstawie� pionk�w dla test�w
d, e, f, g, h.