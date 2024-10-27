from pycaret.regression import setup
from .dataset import dataset, dataset_test
from pathlib import Path
import os

s = setup(
    data=dataset,
    target="score",
    test_data=dataset_test,
    remove_outliers=True,
    fold=24,
    session_id=2024,
    use_gpu=os.getenv("ASI_USE_GPU") == "1",
    index=False,
)

"""
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
"""

model = s.create_model("lar")
tuned = s.tune_model(model, n_iter=24 * 24 * 6, optimize="RMSE")

# Compare models
# models = compare_models(n_select=3)

# Tune top 3 models
# tuned_models = [tune_model(model) for model in models]

# Blend tuned models
# blended_model = blend_models(tuned_models)
final_model = tuned

# Print final model
print(final_model)

Path(".models").mkdir(exist_ok=True)
s.save_model(final_model, ".models/output_model")
p = s.plot_model(final_model, save=True, verbose=False)
Path(p).rename(".models/Residuals.png")
p = s.plot_model(final_model, plot="error", save=True, verbose=False)
Path(p).rename(".models/Error.png")
