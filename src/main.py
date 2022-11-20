import numpy as np
import pandas as pd
from scipy import stats

file_path_heart = "./datasets/heart.dat"

np.set_printoptions(suppress=True)

headers = [
    "Age",
    "Sex",
    "ChestPainType",
    "RestBloodPressure",
    "SerumCholestoral",
    "FastingBloodSugar",
    "ResElectrocardiographic",
    "MaxHeartRate",
    "ExerciseInduced",
    "Oldpeak",
    "Slope",
    "MajorVessels",
    "Thal",
    "Class",
]

dataset = pd.read_csv(
    file_path_heart,
    skiprows=18,
    names=headers,
    index_col=None,
)
# print(dataset)

description = stats.describe(dataset)
print(description)
# print(description.mean)
# print(type(description.mean))

def print_stat_from_description(np_arr_stat, stat_name):
    df = pd.DataFrame(np_arr_stat, columns=[stat_name], index=headers)
    df.index.name = "Attributes"
    # print(df)
    print(f"--------- METRICS: {stat_name} ------------\n")
    print(df.style.format(precision=2).to_latex(column_format="|c|S|", hrules=True, siunitx=True))


# * Mean
print_stat_from_description(description.mean, stat_name="Mean")

# * Variance
print_stat_from_description(description.variance, stat_name="Variance")

# * Skewness
print_stat_from_description(description.skewness, stat_name="Skewness")
