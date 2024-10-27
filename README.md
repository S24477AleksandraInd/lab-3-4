# Lab 3

## Dane wejściowe

Po wstępnej analizie (`.assets/CollegeDistance.html`) danych można zauważyć następujące zależności:
 - Aż 2% studentów ma 0 dystans do uczelni
 - Region ma dużą zależność od czesnego
 - Region jest również zależny od zarobków
 - Zbiór danych nie zawiera żadnych braków lub odchyleń


## Stworzone modele

### Wstępna analiza

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

Kopia raportu znajduje się w [`.assets/report-copy`](.assets/report-copy).

## Github Actions oraz *self-hosted runners*

Do uruchamiania zadań w GH Actions pierwotnie używałam kontenera zdefiniowanego w `compose.yml`

Później przeniosłam się na [runnery wewnątrz kubernetes-a (ARC)](https://github.com/actions/actions-runner-controller/blob/master/docs/quickstart.md).

# Lab 4
