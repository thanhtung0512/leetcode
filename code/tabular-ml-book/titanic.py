from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.metrics import accuracy_score
titanic_path = (
    "https://media.githubusercontent.com/media/tiepvupsu/tabml_data/master/titanic/"
)
df_train_full = pd.read_csv(titanic_path + "train.csv")
df_test = pd.read_csv(titanic_path + "test.csv")

df_train_full.drop(columns=["Cabin"], inplace=True)
df_test.drop(columns="Cabin", inplace=True)

df_train, df_val = train_test_split(df_train_full, test_size=0.1)

X_train = df_train.copy()
y_train = X_train.pop("Survived")


X_val = df_val.copy()
y_val = X_val.pop("Survived")

# cat_transformer tren 3 dac trung categorical

cat_cols = ["Embarked", "Sex", "Pclass"]
cat_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse=False)),
    ]
)

# ap dung num_transformer len 2 dac trung numeric

num_cols = ["Age", "Fare"]
num_transformer = Pipeline(
    steps=[("imputer", KNNImputer(n_neighbors=5)), ("scaler", RobustScaler())]
)


preprocessor = ColumnTransformer(
    transformers=[
        ("num", num_transformer, num_cols),
        ("cat", cat_transformer, cat_cols),
    ]
)


# ket hop bo xu ly preprocessor voi bo phan loai RandomForestClassifier
full_pp = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", RandomForestClassifier())]
)

full_pp.fit(X_train, y_train)


y_train_predict = full_pp.predict(X_train)
print(f"Accuracy on train data: {accuracy_score(list(y_train),list(y_train_predict))}")


y_val_predict = full_pp.predict(X_val)
print(f"Accuracy on train data: {accuracy_score(list(y_val),list(y_val_predict))}")


preds = full_pp.predict(df_test)
sample_submission = pd.read_csv(titanic_path + "gender_submission.csv")
sample_submission["Survived"] = preds
sample_submission.to_csv("titanic_submission.csv", index=False)
