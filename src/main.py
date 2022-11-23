import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import wilcoxon, shapiro
import matplotlib.pyplot as plt

file_path_heart = "../datasets/hepatitis.dat"

np.set_printoptions(suppress=True)

headers_hepatitis = [
    "Age",
    "Sex",
    "Steroid",
    "Antivirals",
    "Fatigue",
    "Malaise",
    "Anorexia",
    "LiverBig",
    "LiverFirm",
    "SpleenPalpable",
    "Spiders",
    "Ascites",
    "Varices",
    "Bilirubin",
    "AlkPhosphate",
    "Sgot",
    "AlbuMin",
    "ProTime",
    "Histology",
    "Class"
]

dataset = pd.read_csv(
    file_path_heart,
    skiprows=24,
    names=headers_hepatitis,
    index_col=None,
)
# print(dataset)

description = stats.describe(dataset)
print(description)


# print(description.mean)
# print(type(description.mean))

def print_stat_from_description(np_arr_stat, stat_name):
    df = pd.DataFrame(np_arr_stat, columns=[stat_name], index=headers_hepatitis)
    df.index.name = "Attributes"
    print(f"--------- METRICS: {stat_name} ------------\n")
    print(df.style.format(precision=2).to_latex(column_format="|c|S|", hrules=True, siunitx=True))


# print(dataset)

# * Mean
# print_stat_from_description(description.mean, stat_name="Mean")

# # * Variance
# print_stat_from_description(description.variance, stat_name="Variance")

# # * Standard deviation
# std = np.std(dataset)
# print_stat_from_description(pd.Series.to_numpy(std), stat_name="Standard deviation")

# # # * Skewness
# print_stat_from_description(description.skewness, stat_name="Skewness")

# # * Kurtosis
# print_stat_from_description(description.kurtosis, stat_name="Kurtosis")

print(dataset)
print(type(dataset))

# stat, p = wilcoxon(age, sex)
# print('Statistics=%.3f, p=%.3f' % (stat, p))

sex_1_df = dataset[dataset["Sex"] == 1]
sex_2_df = dataset[dataset["Sex"] == 2]

die_or_survive_sex_1_df = sex_1_df["Age"].to_list()
die_or_survive_sex_2_df = sex_2_df["Age"].to_list()

die_or_survive_sex_1_shapiro = stats.shapiro(die_or_survive_sex_1_df)
die_or_survive_sex_2_shapiro = stats.shapiro(die_or_survive_sex_2_df)

print(die_or_survive_sex_1_shapiro)
print(die_or_survive_sex_2_shapiro)

var1 = stats.variation(die_or_survive_sex_1_df)
var2 = stats.variation(die_or_survive_sex_2_df)
print(var1)
print(var2)
hepatitis_welch_t_test = stats.ttest_ind(die_or_survive_sex_1_df, die_or_survive_sex_2_df, equal_var=False)
print(hepatitis_welch_t_test)

fig, ax = plt.subplots(2, 1)
ax[0].boxplot([die_or_survive_sex_1_shapiro, die_or_survive_sex_2_shapiro])
ax[0].set_xticklabels({"die_or_survive_sex_1_shapiro", "die_or_survive_sex_2_shapiro"})
ax[1].boxplot(hepatitis_welch_t_test)
ax[1].set_xticklabels({"hepatitis_welch_t_test"})
plt.savefig("hepatitis_welch_t_test.jpg")
plt.show()
