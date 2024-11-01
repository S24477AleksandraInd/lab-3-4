import pandas as pd
from sklearn.preprocessing import RobustScaler

dataset_raw = pd.read_csv(".assets/CollegeDistance.csv")

# drop unused columns
dataset = dataset_raw.drop(columns=["rownames"])

# encode gender
dataset["gender"] = dataset["gender"].apply(lambda v: 1 if v == "male" else 0)

# encode ethnicity
# dataset = pd.get_dummies(
#     dataset, columns=["ethnicity"], prefix=["ethnicity"], prefix_sep="_", dtype=int
# )

# scale data
# scaler = RobustScaler()
# dataset["education"] = dataset["education"].astype(float)
# scalable_columns = dataset.select_dtypes(include=["float64"]).columns
# dataset[scalable_columns] = scaler.fit_transform(dataset[scalable_columns])

# Create a test dataset
dataset_test = dataset.sample(frac=0.3, random_state=7312)

if __name__ == "__main__":
    import pandas_profiling as pp

    report = pp.ProfileReport(dataset)
    report.to_file(".assets/CollegeDistance.html")
