# Plan ćwiczeń w silniku

Zbuduj niewielką scenę testową i przechodź przez zadania w podanej kolejności.

| Ćwiczenie | Oczekiwany wynik | Dowód |
|---|---|---|
| Jeden właściciel kamery | Brak podwójnego yaw i nadpisania transformacji | Log właściciela i kątów |
| FOV przy zmianie proporcji | Zachowanie wybranej osi FOV | Zrzuty tej samej sceny |
| Powtarzane żądanie przejścia | Osiągnięcie celu w zadanym czasie | Wykres wartości i czasu |
| Cel DOF znika | Kontrolowany fallback | Nagranie i log providera |
| Mieszanie chodu i biegu | Brak podwójnych kroków | Log events i odsłuch |
| Ruch przy ścianie | Animacja zgodna z rzeczywistym ruchem | Prędkość żądana i rzeczywista |
| Schody i platforma | Stabilna stopa podporowa | Podgląd trace oraz IK |
| Kamera przy przeszkodzie | Brak clippingu i łagodny powrót | Nagranie boom |
| Szybkie odwrócenie przejścia | Ciągłość widoku i optyki | Log aktywnej perspektywy |
| Przerwanie sceny | Przywrócenie poprawnego sterowania | Log blokad i snapshotu |

Powtórz ćwiczenia przy różnych FPS, pauzie i slow motion. Dodaj brak zasobu, teleport i zmianę konfiguracji w runtime. Oddziel wynik testu matematyki od potwierdzenia działania integracji oraz oceny odczucia przez gracza.
