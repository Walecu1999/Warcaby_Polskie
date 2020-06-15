Raport z projektu realizowanego na przedmiocie Języki Symboliczne w semestrze letnim 2019/20 na Politechnice Krakowskiej.
Link do repozytorium na GitHub: https://github.com/Walecu1999/Warcaby_Polskie 

Projekt stworzył: Maciej Walczyk						Nr indeksu: 130599

Założenie projektu: 

Założeniem projektu było stworzenie w języku Python aplikacji(czy też gry) – Warcaby Polskie(100-polowe).
Stworzenie takiego projektu miało prowadzić do drugiego i najważniejszego założenia: Poznania i nauki języka programowania Python. W moim skromnym mniemaniu, oba te założenia zostały spełnione w zadowalającym stopniu.

Linki do projektu:

list comperhension: 
https://github.com/Walecu1999/Warcaby_Polskie/blob/1cf1a78552793444ab8def220e4587aff9ffaee2/plansza.py#L30
https://github.com/Walecu1999/Warcaby_Polskie/blob/1cf1a78552793444ab8def220e4587aff9ffaee2/plansza.py#L32
https://github.com/Walecu1999/Warcaby_Polskie/blob/1cf1a78552793444ab8def220e4587aff9ffaee2/plansza.py#L34

klasy:
https://github.com/Walecu1999/Warcaby_Polskie/blob/1cf1a78552793444ab8def220e4587aff9ffaee2/plansza.py#L11
https://github.com/Walecu1999/Warcaby_Polskie/blob/34f304e5fb5fe45be3748b158a37033d6786ec3b/Pionek.py#L7

Wyjątki:
https://github.com/Walecu1999/Warcaby_Polskie/blob/1cf1a78552793444ab8def220e4587aff9ffaee2/plansza.py#L360

Main:
https://github.com/Walecu1999/Warcaby_Polskie/blob/34f304e5fb5fe45be3748b158a37033d6786ec3b/main.py#L5

Główna pętla:
https://github.com/Walecu1999/Warcaby_Polskie/blob/34f304e5fb5fe45be3748b158a37033d6786ec3b/main.py#L68

Parę testów:
https://github.com/Walecu1999/Warcaby_Polskie/blob/34f304e5fb5fe45be3748b158a37033d6786ec3b/main.py#L35


Realizacja projektu:

Od początku zamysłem było oparcie się na bibliotece Pygame. Nie była ona konieczna do wykonania tego projektu, ponieważ opiera się on w głównej mierze na oknie aplikacji. Równie dobrze można było użyć biblioteki tkinter, która bardzo dobrze poradziłaby sobie z wymaganiami mojej aplikacji. Jednak chciałem zaznajomić się z biblioteką Pygame, aby móc w przyszłości wykorzystać ją do innych własnych projektów.
Początkowo największy problem stanowiło rozplanowanie całego projektu. Jakich funkcji i klas będę potrzebował, jak je napisać by później móc z nich swobodnie korzystać. Stworzona została klasa Pionek, której obiekty posiadały współrzędną X, współrzędną Y, kolor piona, ekran na którym są wyświetlane oraz to czy dany obiekt jest damką. Zdecydowałem się stworzyć trzy listy: listę pionków białych, listę czarnych pionków i listę pozostałych nie zapełnionych pól, która tak naprawdę też była listą „Pionków”. Przy każdym zbiciu piona, powiększała się lista pustych pól a usuwany zostawał element, który odpowiadał za zbitego piona w liście pionków białych czy też czarnych.
Wraz z rozwojem projektu problem stanowić zaczęła składnia Pythona, której dopiero się uczyłem. Pomimo kilku podobieństw do języka C++, z którym miałem najwięcej do czynienia do tej pory, nowości wprowadzone w Pythonie, pomimo że finalnie okazały się bardzo przyjazne i pomocne,
na początku sprawiły wiele problemu. 
Największy problem w stworzeniu funkcjonalnych Warcabów były problemy: możliwość odznaczenia piona, poprawne podświetlenie zaznaczonego piona oraz przede wszystkim możliwość wielokrotnego bicia. Każdy ruch jest sprawdzany i w momencie gdy ruch jest nieprawidłowy wyświetlana jest odpowiednia wiadomość. W momencie gdy pionek osiągnie ostatnią linię przeciwnika zamienia się w damkę. Damki w moim projekcie poruszają się tak samo jak pionki tylko z możliwością ruchu i bicia zarówno do przodu jak i do tyłu. W momencie zakończenia rozgrywki wyświetlany jest napis oznajmiający wynik i po kilku sekundach aplikacja zostaje zamknięta.


