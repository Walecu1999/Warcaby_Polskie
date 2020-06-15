Raport z projektu realizowanego na przedmiocie Jêzyki Symboliczne w semestrze letnim 2019/20 na Politechnice Krakowskiej.
Link do repozytorium na GitHub: https://github.com/Walecu1999/Warcaby_Polskie 

Projekt stworzy³: Maciej Walczyk						Nr indeksu: 130599

Za³o¿enie projektu: 

Za³o¿eniem projektu by³o stworzenie w jêzyku Python aplikacji(czy te¿ gry) – Warcaby Polskie(100-polowe).
Stworzenie takiego projektu mia³o prowadziæ do drugiego i najwa¿niejszego za³o¿enia: Poznania i nauki jêzyka programowania Python. W moim skromnym mniemaniu, oba te za³o¿enia zosta³y spe³nione w zadowalaj¹cym stopniu.

Realizacja projektu:

Od pocz¹tku zamys³em by³o oparcie siê na bibliotece Pygame. Nie by³a ona konieczna do wykonania tego projektu, poniewa¿ opiera siê on w g³ównej mierze na oknie aplikacji. Równie dobrze mo¿na by³o u¿yæ biblioteki tkinter, która bardzo dobrze poradzi³aby sobie z wymaganiami mojej aplikacji. Jednak chcia³em zaznajomiæ siê z bibliotek¹ Pygame, aby móc w przysz³oœci wykorzystaæ j¹ do innych w³asnych projektów.
Pocz¹tkowo najwiêkszy problem stanowi³o rozplanowanie ca³ego projektu. Jakich funkcji i klas bêdê potrzebowa³, jak je napisaæ by póŸniej móc z nich swobodnie korzystaæ. Stworzona zosta³a klasa Pionek, której obiekty posiada³y wspó³rzêdn¹ X, wspó³rzêdn¹ Y, kolor piona, ekran na którym s¹ wyœwietlane oraz to czy dany obiekt jest damk¹. Zdecydowa³em siê stworzyæ trzy listy: listê pionków bia³ych, listê czarnych pionków i listê pozosta³ych nie zape³nionych pól, która tak naprawdê te¿ by³a list¹ „Pionków”. Przy ka¿dym zbiciu piona, powiêksza³a siê lista pustych pól a usuwany zostawa³ element, który odpowiada³ za zbitego piona w liœcie pionków bia³ych czy te¿ czarnych.
Wraz z rozwojem projektu problem stanowiæ zaczê³a sk³adnia Pythona, której dopiero siê uczy³em. Pomimo kilku podobieñstw do jêzyka C++, z którym mia³em najwiêcej do czynienia do tej pory, nowoœci wprowadzone w Pythonie, pomimo ¿e finalnie okaza³y siê bardzo przyjazne i pomocne,
na pocz¹tku sprawi³y wiele problemu. 
Najwiêkszy problem w stworzeniu funkcjonalnych Warcabów by³y problemy: mo¿liwoœæ odznaczenia piona, poprawne podœwietlenie zaznaczonego piona oraz przede wszystkim mo¿liwoœæ wielokrotnego bicia. Ka¿dy ruch jest sprawdzany i w momencie gdy ruch jest nieprawid³owy wyœwietlana jest odpowiednia wiadomoœæ. W momencie gdy pionek osi¹gnie ostatni¹ liniê przeciwnika zamienia siê w damkê. Damki w moim projekcie poruszaj¹ siê tak samo jak pionki tylko z mo¿liwoœci¹ ruchu i bicia zarówno do przodu jak i do ty³u. W momencie zakoñczenia rozgrywki wyœwietlany jest napis oznajmiaj¹cy wynik i po kilku sekundach aplikacja zostaje zamkniêta.


