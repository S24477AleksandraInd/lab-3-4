from pycaret.regression import setup
from .dataset import dataset
from pathlib import Path

# print(dataset)

s = setup(
    data=dataset,
    target="score",
    session_id=33,
    categorical_features=["gender", "ethnicity", "income", "region"],
    numeric_features=["unemp", "wage", "distance", "tuition", "education"],
    verbose=False,
    # use_gpu=True,
    # log_experiment="mlflow",
    # log_data=True,
    # log_profile=True,
    # profile=True,
)

models = s.compare_models(include=["lr", "lasso", "en", "rf", "xgboost"])

best = s.get_leaderboard()

# print(best)

eval_res = s.evaluate_model(best["Model"])

# print(eval_res)

for _, row in best.iterrows():
    Path(".models").mkdir(exist_ok=True)
    s.save_model(row["Model"], f'.models/{row["Model Name"]}')
    p = s.plot_model(row["Model"], save=True, verbose=False)
    Path(p).rename(f".models/{row['Model Name']} Residuals.png")
    p = s.plot_model(row["Model"], plot="error", save=True, verbose=False)
    Path(p).rename(f".models/{row['Model Name']} Error.png")
