# Lab 4

## Jak sklonować repozytorium

0. Zainstaluj git na swoim komputerze

1. Sklonuj repozytorium

```sh
git clone git@github.com:S24477AleksandraInd/lab-3-4.git
```

## Uruchom

### Lokalnie

0. Zainstaluj `Python 3.11` oraz `poetry`.

> [!TIP]
> Do zarządzania wersjami w pythonie użyj PyEnv

1. Zainstaluj zależności do uczenia maszynowego

```sh
poetry install --with learning
```

2. Stwórz model

```sh
poetry run python3 -m asi_labs.lab3.learn
```

> [!IMPORTANT]
> Może być wymagane zaistalowanie bibliotek `libgomp1 wkhtmltopdf` do wygenerowania raportu. Mimo ewentualnego błędu w tym module, model zostanie wygenerowany.
> Więcej informacji https://pypi.org/project/pdfkit/

3. Zainstaluj zależności do API

```sh
poetry install --with api
```

4. Uruchom API

```sh
poetry run python3 -m asi_labs.lab4.api
```

### Docker compose

1. Utwórz plik `compose.yml`

```yaml
services:
  api:
    image: s24477/lab4-api:latest
    ports:
      - "8000:8000"
```

2. Uruchom

```sh
docker compose up
```

> [!NOTE]
> Docker automatycznie pobierze obraz z Docker Huba

### Docker

```sh
docker run -it --rm -p 8000:8000 s24477/lab4-api:latest
```

> [!NOTE]
> Docker automatycznie pobierze obraz z Docker Huba

## Tworzenie obrazu

```sh
git clone git@github.com:S24477AleksandraInd/lab-3-4.git
cd lab-3-4
docker compose build
```

# Lab 3

## Zadania z labu

### Eksploracja i wstępna analiza danych

- Przetwarzanie danych -> `asi_labs/lab3/dataset.py`
- Eksploracja danych -> `assets/report-copy/CollegeDistance.html`

### Inżynieria cech i przygotowanie danych

- Inżynieria cech -> `asi_labs/lab3/dataset.py`

### Wybór i trenowanie modelu

- Wybór modelu -> `asi_labs/lab3/learn.py` oraz dalsza część README.md
- Trenowanie modelu -> `asi_labs/lab3/learn.py`

### Ocena i optymalizacja modelu

- Ocena poprzez raporty -> `assets/report-copy/`
- Optymalizacja modelu -> `asi_labs/lab3/learn.py`
- Skrócona ocena -> dalsza część README.md

## Stworzone modele

### Wstępna analiza modeli względem danych

Pierwsza analiza danych pozwoliła na porównanie następującej gamy model ML:

```
           RMSLE    MAPE  TT (Sec)
br        0.3856  2.0547     0.122
ridge     0.3852  2.0647     0.092
lar       0.3852  2.0653     0.093
lr        0.3848  2.0682     0.095
huber     0.3776  2.1839     0.125
gbr       0.3848  2.6154     0.245
catboost  0.3899  2.4579     2.384
ada       0.4159  1.9984     0.132
lightgbm  0.3898  2.4825     0.243
rf        0.3829  2.9293     0.182
omp       0.3897  2.9115     0.092
knn       0.3880  4.3424     0.105
et        0.3838  2.6361     0.160
xgboost   0.3946  2.6437     0.195
lasso     0.6168  1.0606     0.120
en        0.6168  1.0606     0.120
llar      0.6168  1.0606     0.092
dummy     0.6168  1.0606     0.091
dt        0.4109  5.1157     0.099
par       0.4502  4.9982     0.093
```

W tych danych można zauważyć, że większość modeli ma podobne wyniki. Zdecydowałam się na wybór modelu "Lars Regressor" ze względu na porównywane wyniki z innymi i niski Train Time.

### Ostateczny model

```
         MAE     MSE    RMSE      R2   RMSLE    MAPE
Mean  0.4201  0.2656  0.5145  0.2558  0.2799  2.3366
Std   0.0294  0.0312  0.0303  0.1004  0.0186  1.2025
```

## Podsumowanie

Pełny raport z trenowania został wygenerowany w [Reapply "fix(tmp): use ubuntu latest" #23](https://github.com/S24477AleksandraInd/lab-3-4/actions/runs/11542692322).

Kopia raportu znajduje się w [`assets/report-copy`](assets/report-copy).

Wszystkie raporty znajdują są dostępne [tutaj](https://github.com/S24477AleksandraInd/lab-3-4/actions?query=event%3Apush+is%3Asuccess+branch%3Amain)

## Github Actions oraz _self-hosted runners_

Do uruchamiania zadań w GH Actions pierwotnie zastosowano kontener zdefiniowany w `compose.yml`

Z dalszym rozwojem projektu wykorzystano [runnery wewnątrz kubernetes-a (ARC)](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/quickstart-for-actions-runner-controller).
