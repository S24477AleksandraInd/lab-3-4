import pandas as pd

dataset_raw = pd.read_csv(".assets/CollegeDistance.csv")

# drop the rownames column

dataset = dataset_raw.drop(columns=["rownames"])

# convert fcollege mcollege	home	urban into yes/no into booleans

dataset["fcollege"] = dataset["fcollege"].apply(lambda x: x == "yes")
dataset["mcollege"] = dataset["mcollege"].apply(lambda x: x == "yes")
dataset["home"] = dataset["home"].apply(lambda x: x == "yes")
dataset["urban"] = dataset["urban"].apply(lambda x: x == "yes")
