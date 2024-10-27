from pycaret.regression import setup
from .dataset import dataset, dataset_test, dataset_raw
from pathlib import Path
import jinja2
import os
import datetime
import pdfkit
import shutil
import base64

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

start_time = datetime.datetime.now()
model = s.create_model("lar")
tuned = s.tune_model(model, n_iter=24 * 24 * 6, optimize="RMSE")
end_time = datetime.datetime.now()

tt = end_time - start_time

final_model = tuned

# Print final model
print(final_model)

images = [
    s.plot_model(final_model, save=True, verbose=False),
    s.plot_model(final_model, plot="error", save=True, verbose=False),
    s.plot_model(final_model, plot="feature_all", save=True, verbose=False),
    s.plot_model(final_model, plot="learning", save=True, verbose=False),
    s.plot_model(final_model, plot="vc", save=True, verbose=False),
]

# Create .models directory if it does not exist
Path(".models").mkdir(exist_ok=True)

for image in images:
    target_path = Path(".models") / Path(image).name
    if target_path.exists():
        target_path.unlink()
    shutil.move(image, ".models")

images = [".models/" + Path(image).name for image in images]

# make a html report
templates = Path(__file__).parent / "templates"
env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates))
template = env.get_template("report.html")

# open images and convert them to base64

def image_to_base64(image_path):
    with open(image_path, "rb") as fi:
        return base64.b64encode(fi.read()).decode("utf8")

images_base64 = { f"{Path(image).name}_base64": image_to_base64(image) for image in images }
print(images_base64.keys())

# data for pull
s.predict_model(final_model, dataset_test)

html = template.render(
    dataset=dataset,
    dataset_test=dataset_test,
    dataset_raw=dataset_raw,
    generated_at=datetime.datetime.now().isoformat(),
    images=images_base64,
    metrics=s.pull().drop(columns=["Model"]),
    training_time=tt,
    model_name=str(final_model),
)

with open(".models/report.html", "w", encoding="utf8") as f:
    f.write(html)

pdfkit.from_string(
    html,
    ".models/report.pdf",
    options={
        "encoding": "UTF-8",
        "page-size": "A4",
        "orientation": "Landscape",
        "enable-local-file-access": True,
    },
)
