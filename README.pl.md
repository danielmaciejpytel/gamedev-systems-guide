<h1 align="center">GameDev Systems Guide</h1>

<p align="center"><b>Praktyczne systemy dla responsywnych, spójnych gier.</b><br>
Samouczki niezależne od silnika: kamera, animacja, locomotion, kontakt z podłożem i przejścia między rozgrywką a scenami.</p>

<p align="center">
  <img src="https://img.shields.io/badge/typ-przewodnik-2E86AB?style=for-the-badge&labelColor=1f2937" alt="Przewodnik">
  <img src="https://img.shields.io/badge/samouczki-20-F6AE2D?style=for-the-badge&labelColor=1f2937" alt="20 samouczków">
  <img src="https://img.shields.io/badge/silnik-dowolny-E4572E?style=for-the-badge&labelColor=1f2937" alt="Niezależny od silnika">
  <img src="https://img.shields.io/badge/język_treści-angielski-2E86AB?style=for-the-badge&labelColor=1f2937" alt="Język treści: angielski">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/przykłady-biblioteka_standardowa_Pythona-F6AE2D?style=flat-square&labelColor=1f2937" alt="Przykłady używają tylko biblioteki standardowej Pythona">
</p>

<p align="center">
  <b>Polski</b> · <a href="README.md">English</a> ·
  <a href="#zacznij-lekturę">Zacznij lekturę</a> ·
  <a href="#samouczki">Samouczki</a> ·
  <a href="#przykłady-i-ćwiczenia">Przykłady i ćwiczenia</a> ·
  <a href="#uruchamianie-testów">Uruchamianie testów</a>
</p>

Każdy samouczek przedstawia problem, sposób implementacji i scenariusz weryfikacji w grze. To przewodnik do czytania, a nie gra ani wtyczka. Samouczki i przykłady są wyłącznie po angielsku; `README.pl.md` to polska wersja tej strony, a nie tłumaczenie przewodnika.

## Zacznij lekturę

- Budujesz kompletny system: zacznij od [Who actually controls the camera?](tutorials/01-camera-ownership.md) i czytaj po kolei.
- Masz konkretny problem: wybierz odpowiedni temat w sekcji [Samouczki](#samouczki).
- Chcesz poćwiczyć w silniku: skorzystaj z [planu ćwiczeń w silniku](PRACTICE.md).

Materiał nie zależy od silnika. Nazwy typów, kości, pól i zasobów są przykładowe. Bloki oznaczone `text` to pseudokod, który wymaga adaptera do jednostek, osi, API i cyklu aktualizacji Twojego silnika. Nie są gotową wtyczką.

## Samouczki

Kamera:

1. [Who actually controls the camera?](tutorials/01-camera-ownership.md)
2. [Input, pause, and different clocks](tutorials/02-input-and-time.md)
3. [Predictable angles, corrections, and resets](tutorials/03-angles-limits-and-resets.md)
4. [Soft rotation limits and return to center](tutorials/04-soft-rotation-limits.md)
5. [FOV: horizontal, vertical, and aspect ratio](tutorials/05-fov-and-projection.md)
6. [Parameter smoothing and partial updates](tutorials/06-parameter-blending.md)
7. [Depth of field and a dynamic focus target](tutorials/07-depth-of-field.md)
8. [Camera motion layers and player comfort](tutorials/08-camera-motion-and-comfort.md)
9. [Rigs, reflection, and stable data contracts](tutorials/09-rigs-and-data-contracts.md)

Locomotion i animacja:

10. [Locomotion: intent, actual movement, and stride phase](tutorials/10-locomotion.md)
11. [Animation selection tables, wildcards, and fallback](tutorials/11-animation-selection.md)
12. [Clip playback, blending, and events](tutorials/12-clips-blending-and-events.md)
13. [State machines and smooth transitions through inertialization](tutorials/13-state-machines-and-inertialization.md)
14. [Damping, interpolation, and springs](tutorials/14-damping-and-springs.md)
15. [Root motion, target alignment, and stride length](tutorials/15-root-motion-and-stride.md)
16. [Floor IK and stable ground contact](tutorials/16-floor-ik.md)

Sceny, pojazdy i konfiguracja:

17. [Scenes, request queues, and returning control](tutorials/17-scenes-and-control-handover.md)
18. [Vehicle camera: boom, autocenter, and collision](tutorials/18-vehicle-camera.md)
19. [Switching perspective and blending the full view](tutorials/19-perspectives-and-proxy.md)
20. [Configuration, caches, and evidence of correct behavior](tutorials/20-configuration-and-debugging.md)

## Przykłady i ćwiczenia

- **[`examples/camera_math.py`](examples/camera_math.py)** — matematyka kamery i wygładzanie. Samodzielny, tylko biblioteka standardowa. Pokazuje matematykę i proste mechanizmy, a nie renderer ani kompletny graf animacji.
- **[`tests/test_camera_math.py`](tests/test_camera_math.py)** — testy zachowania dla przykładów.
- **[`PRACTICE.md`](PRACTICE.md)** — plan ćwiczeń w silniku: dziesięć ćwiczeń z oczekiwanym wynikiem i dowodem do zebrania. Powtarzaj je przy różnych liczbach klatek, podczas pauzy i w zwolnionym tempie.

## Uruchamianie testów

Z katalogu głównego repozytorium:

```sh
python -m unittest discover -s tests -v
```

Płynna kamera, animacja i ruch wpływają na jakość gry. Jasne cele, projekt poziomów, dźwięk, balans i dostępność wymagają jednak własnych iteracji i testów z graczami.
