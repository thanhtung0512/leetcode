import pandas as pd
titanic_path = "https://media.githubusercontent.com/media/tiepvupsu/tabml_data/master/titanic/"

train_df = pd.read_csv(titanic_path + "train.csv")

train_df.head()
