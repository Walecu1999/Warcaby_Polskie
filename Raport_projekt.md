Raport z projektu realizowanego na przedmiocie J�zyki Symboliczne w semestrze letnim 2019/20 na Politechnice Krakowskiej.
Link do repozytorium na GitHub: https://github.com/Walecu1999/Warcaby_Polskie 

Projekt stworzy�: Maciej Walczyk						Nr indeksu: 130599

Za�o�enie projektu: 

Za�o�eniem projektu by�o stworzenie w j�zyku Python aplikacji(czy te� gry) � Warcaby Polskie(100-polowe).
Stworzenie takiego projektu mia�o prowadzi� do drugiego i najwa�niejszego za�o�enia: Poznania i nauki j�zyka programowania Python. W moim skromnym mniemaniu, oba te za�o�enia zosta�y spe�nione w zadowalaj�cym stopniu.

Realizacja projektu:

Od pocz�tku zamys�em by�o oparcie si� na bibliotece Pygame. Nie by�a ona konieczna do wykonania tego projektu, poniewa� opiera si� on w g��wnej mierze na oknie aplikacji. R�wnie dobrze mo�na by�o u�y� biblioteki tkinter, kt�ra bardzo dobrze poradzi�aby sobie z wymaganiami mojej aplikacji. Jednak chcia�em zaznajomi� si� z bibliotek� Pygame, aby m�c w przysz�o�ci wykorzysta� j� do innych w�asnych projekt�w.
Pocz�tkowo najwi�kszy problem stanowi�o rozplanowanie ca�ego projektu. Jakich funkcji i klas b�d� potrzebowa�, jak je napisa� by p�niej m�c z nich swobodnie korzysta�. Stworzona zosta�a klasa Pionek, kt�rej obiekty posiada�y wsp�rz�dn� X, wsp�rz�dn� Y, kolor piona, ekran na kt�rym s� wy�wietlane oraz to czy dany obiekt jest damk�. Zdecydowa�em si� stworzy� trzy listy: list� pionk�w bia�ych, list� czarnych pionk�w i list� pozosta�ych nie zape�nionych p�l, kt�ra tak naprawd� te� by�a list� �Pionk�w�. Przy ka�dym zbiciu piona, powi�ksza�a si� lista pustych p�l a usuwany zostawa� element, kt�ry odpowiada� za zbitego piona w li�cie pionk�w bia�ych czy te� czarnych.
Wraz z rozwojem projektu problem stanowi� zacz�a sk�adnia Pythona, kt�rej dopiero si� uczy�em. Pomimo kilku podobie�stw do j�zyka C++, z kt�rym mia�em najwi�cej do czynienia do tej pory, nowo�ci wprowadzone w Pythonie, pomimo �e finalnie okaza�y si� bardzo przyjazne i pomocne,
na pocz�tku sprawi�y wiele problemu. 
Najwi�kszy problem w stworzeniu funkcjonalnych Warcab�w by�y problemy: mo�liwo�� odznaczenia piona, poprawne pod�wietlenie zaznaczonego piona oraz przede wszystkim mo�liwo�� wielokrotnego bicia. Ka�dy ruch jest sprawdzany i w momencie gdy ruch jest nieprawid�owy wy�wietlana jest odpowiednia wiadomo��. W momencie gdy pionek osi�gnie ostatni� lini� przeciwnika zamienia si� w damk�. Damki w moim projekcie poruszaj� si� tak samo jak pionki tylko z mo�liwo�ci� ruchu i bicia zar�wno do przodu jak i do ty�u. W momencie zako�czenia rozgrywki wy�wietlany jest napis oznajmiaj�cy wynik i po kilku sekundach aplikacja zostaje zamkni�ta.


