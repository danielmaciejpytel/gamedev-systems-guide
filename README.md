# GameDev Systems Guide

Praktyczne tutoriale po polsku o systemach, które pomagają zbudować responsywną i spójną grę: kamerze, animacji, lokomocji, kontakcie z podłożem oraz przejściach między gameplayem i scenami.

Każdy tutorial przedstawia problem, sposób rozwiązania i scenariusz sprawdzenia w grze. Zacznij od właściciela kamery, jeśli budujesz cały system. Przy konkretnym problemie wybierz odpowiedni temat ze spisu.

## Jak korzystać

Materiał jest niezależny od konkretnego silnika. Nazwy typów, kości, pól i zasobów są przykładowe. Fragmenty oznaczone `text` to pseudokod, który wymaga adaptera do jednostek, osi, API i cyklu aktualizacji Twojego silnika. Nie stanowią gotowego pluginu.

Przykłady Python są samodzielne i korzystają wyłącznie z biblioteki standardowej. Pokazują matematykę i zachowanie prostych mechanizmów. Nie symulują renderera ani kompletnego grafu animacji.

```sh
python -m unittest discover -s tests -v
```

## Tutoriale

- [Kto naprawdę steruje kamerą?](tutorials/01-wlasnosc-kamery.md)
- [Wejście, pauza i różne zegary](tutorials/02-wejscie-i-czas.md)
- [Kąty, korekty i resety bez niespodzianek](tutorials/03-katy-limity-i-resety.md)
- [Miękkie granice obrotu i powrót do środka](tutorials/04-miekkie-granice.md)
- [FOV: poziomy, pionowy i zależny od ekranu](tutorials/05-fov-i-projekcja.md)
- [Wygładzanie parametrów i częściowe aktualizacje](tutorials/06-blend-parametrow.md)
- [Głębia ostrości i dynamiczny cel](tutorials/07-glebia-ostrosci.md)
- [Warstwy ruchu kamery i komfort gracza](tutorials/08-warstwy-ruchu-kamery.md)
- [Rig, refleksja i stabilne kontrakty](tutorials/09-rig-i-kontrakty-danych.md)
- [Lokomocja: intencja, rzeczywisty ruch i faza kroku](tutorials/10-lokomocja.md)
- [Tabele doboru animacji, wildcardy i fallback](tutorials/11-dobor-animacji.md)
- [Odtwarzanie klipów, blend i zdarzenia](tutorials/12-klipy-blend-i-zdarzenia.md)
- [Maszyna stanów i płynne przejścia przez inercję](tutorials/13-maszyna-stanow-i-inercja.md)
- [Damping, interpolacja i sprężyny](tutorials/14-damping-i-sprezyny.md)
- [Root motion, dopasowanie celu i długość kroku](tutorials/15-root-motion-i-korekta-kroku.md)
- [Floor IK i stabilny kontakt z podłożem](tutorials/16-floor-ik.md)
- [Sceny, kolejki żądań i oddawanie sterowania](tutorials/17-sceny-i-przejecie-kontroli.md)
- [Kamera pojazdu: boom, autocenter i kolizje](tutorials/18-kamera-pojazdu.md)
- [Przełączanie perspektywy i blend pełnego widoku](tutorials/19-perspektywy-i-proxy.md)
- [Konfiguracja, cache i dowody poprawnego działania](tutorials/20-konfiguracja-i-debugowanie.md)

## Przykłady i ćwiczenia

- [Matematyka kamery i wygładzanie](examples/camera_math.py)
- [Testy zachowania przykładów](tests/test_camera_math.py)
- [Plan ćwiczeń w silniku](PRACTICE.md)

Płynna kamera, animacje i ruch to część jakości gry. Czytelne cele, projekt poziomów, dźwięk, balans oraz dostępność wymagają również własnych iteracji i testów z graczami.
