# Kto naprawdę steruje kamerą?

## Problem
Kamera obraca się poprawnie przez jedną klatkę, a potem wraca. Najczęściej kilka systemów zapisuje ten sam wynik: wejście gracza, animacja, scenariusz i kamera pojazdu.

## Zbuduj przepływ danych
Rozdziel `LookController` zbierający intencję, `ViewState` przechowujący stan, `ViewPoseSolver` rozwiązujący pozę i `RenderView` przekazujący wynik do renderera. Obiekt kamery w scenie nie musi być aktywnym widokiem. Aktywację powierz `ViewDirector`, który wybiera właściciela według jawnego priorytetu.

```text
urządzenie -> LookController -> ViewState -> ViewPoseSolver -> RenderView
                                   ^
                        scena / pojazd / wspomaganie
```

Przy kamerze osadzonej w szkielecie zmieniaj wejście solvera, a nie transformację, którą animacja zapisze ponownie. Zdecyduj, czy obrót poziomy należy do ciała, czy do lokalnego widoku. Zastosowanie pełnej delty w obu miejscach podwaja obrót.

```text
if freeBodyHeading:
    actor.yaw += look.yaw
    view.localYawDelta = 0
else:
    view.localYawDelta = look.yaw
view.localPitchDelta = look.pitch
```

## Sprawdź w grze
Dodaj podgląd: aktywny właściciel, źródło yaw i końcowy yaw. Przetestuj obrót, wejście do pojazdu i powrót ze sceny. W każdej klatce powinien istnieć jednoznaczny autor końcowego widoku.

---

[Spis treści](../README.md) · [Następny tutorial](02-wejscie-i-czas.md)
