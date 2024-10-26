from pycaret.regression import setup
from .dataset import dataset

# dataset = dataset[["unemp", "wage", "distance", "score"]]

dataset = dataset.drop(columns=["rownames"])

# convert fcollege mcollege	home	urban into yes/no into booleans

dataset["fcollege"] = dataset["fcollege"].apply(lambda x: x == "yes")
dataset["mcollege"] = dataset["mcollege"].apply(lambda x: x == "yes")
dataset["home"] = dataset["home"].apply(lambda x: x == "yes")
dataset["urban"] = dataset["urban"].apply(lambda x: x == "yes")

print(dataset)

s = setup(
    data=dataset,
    target="score",
    session_id=33,
    categorical_features=["gender", "ethnicity", "income", "region"],
    numeric_features=["unemp", "wage", "distance", "tuition", "education"],
    # use_gpu=True,
    # log_experiment="mlflow",
    # log_data=True,
    # log_profile=True,
    # profile=True,
)

models = s.compare_models(include=["lr", "lasso", "en", "rf", "xgboost"])

best = s.get_leaderboard()

print(best)

eval_res = s.evaluate_model(best["Model"])

print(eval_res)


# print pandas profile
# profile = s._profile()

# s.create_api(best["Model"], "Best")
