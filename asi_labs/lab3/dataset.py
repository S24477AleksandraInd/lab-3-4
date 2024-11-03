import pandas as pd
from sklearn.preprocessing import RobustScaler

dataset_raw = pd.read_csv("assets/CollegeDistance.csv")


def transform_df(df: pd.DataFrame):
    df["gender"] = df["gender"].apply(lambda v: 1 if v == "male" else 0)

    # encode ethnicity
    df = pd.get_dummies(
        df, columns=["ethnicity"], prefix=["ethnicity"], prefix_sep="_", dtype=int
    )

    # scale data
    scaler = RobustScaler()
    df["education"] = df["education"].astype(float)
    scalable_columns = df.select_dtypes(include=["float64"]).columns
    df[scalable_columns] = scaler.fit_transform(df[scalable_columns])

    return df


# drop unused columns
dataset = dataset_raw.drop(columns=["rownames"])

dataset = transform_df(dataset)

# Create a test dataset
dataset_test = dataset.sample(frac=0.3, random_state=7312)

if __name__ == "__main__":
    import pandas_profiling as pp

    report = pp.ProfileReport(dataset)
    report.to_file("assets/CollegeDistance.html")
