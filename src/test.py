import pandas as pd
from src.training import model_trainer

if __name__ == '__main__':
    df = pd.read_csv("../data/fake_or_real_news.csv")
    print(df["label"].value_counts())