# Warstwy ruchu kamery i komfort gracza

## Problem
Wyłączenie jednego mnożnika nie usuwa wszystkich ruchów widoku. Kołysanie z animacji, parallax, odrzut, proceduralna reakcja pojazdu i scena mają osobne źródła.

## Projekt
Zdefiniuj osobne kanały: `bodyMotion`, `lookOffset`, `weaponKick`, `vehicleMotion`, `sceneMotion`. Każdy powinien mieć własną wagę, przestrzeń i etap składania.

```text
vehicleContribution = vehiclePose * vehicleModeWeight * comfortVehicleWeight
```

Zerowanie którejkolwiek z dwóch wag usuwa tę składową, ale nie wpływa na pozostałe kanały. Nie nazywaj pojedynczego pola „wyłącz wszystkie ruchy”, jeśli faktycznie steruje tylko parallax.

## Przestrzenie
Offset boczny względem kamery różni się od offsetu względem klatki piersiowej czy trajektorii. Przelicz wektor przez transformację właściwej przestrzeni. Zapamiętaj konwencję osi i kolejność mnożenia transformacji.

## Opcje komfortu
Udostępnij niezależne ustawienia kołysania, przechyłu, drgań i rozmycia. Ruch potrzebny do przekazania trafienia można częściowo zastąpić dźwiękiem, HUD-em i animacją broni. Nagła zmiana FOV także wpływa na odbiór ruchu.

## Sprawdź w grze
Wyłączaj kanały pojedynczo. Testuj chodzenie, sprint, spojrzenie w dół, kolizję pojazdu i scenę. Zapisuj wkład każdego kanału przed złożeniem. Dzięki temu diagnoza nie zależy od zgadywania.

---

[Spis treści](../README.md) · [Poprzedni tutorial](07-glebia-ostrosci.md) · [Następny tutorial](09-rig-i-kontrakty-danych.md)
