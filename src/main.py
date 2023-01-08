import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import wilcoxon, shapiro

file_path_heart = "./datasets/heart.dat"
file_path_thyroid = "./datasets/thyroid.csv"
file_path_survey = "./datasets/survey.csv"

np.set_printoptions(suppress=True)

headers_heart = [
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

headers_thyroid = [
    "Age",
    "Sex",
    "On_thyroxine",
    "Query_on_thyroxine",
    "On_antithyroid_medication",
    "Sick",
    "Pregnant",
    "Thyroid_surgery",
    "I131_treatment",
    "Query_hypothyroid",
    "Query_hyperthyroid",
    "Lithium",
    "Goitre",
    "Tumor",
    "Hypopituitary",
    "Psych",
    "TSH",
    "T3",
    "TT4",
    "T4U",
    "FTI",
    "Class"
]

headers_survey = [
    "Gender",
    "Age",
    "KmBefore",
    "KgBefore",
    "TimeBefore",
    "Medicine1",
    "Medicine2",
    "Medicine3",
    "KmAfter",
    "KgAfter",
    "TimeAfter",
    "SideEffects"
]

# dataset = pd.read_csv(
#     file_path_heart,
#     skiprows=18,
#     names=headers_heart,
#     index_col=None,
# )

# dataset = pd.read_csv(
#     file_path_thyroid,
#     names=headers_thyroid,
#     index_col=None,
# )

dataset = pd.read_csv(
    file_path_survey,
    names=headers_survey,
    index_col=None,
    delimiter=';'
)

# description = stats.describe(dataset)
# print(description)
# print(description.mean)
# print(type(description.mean))

# def print_stat_from_description(np_arr_stat, stat_name):
#     df = pd.DataFrame(np_arr_stat, columns=[stat_name], index=headers_survey)
#     df.index.name = "Attributes"
#     print(f"--------- METRICS: {stat_name} ------------\n")
#     print(df.style.format(precision=2).to_latex(column_format="|c|S|", hrules=True, siunitx=True))


# print(dataset)

# * Mean
# print_stat_from_description(description.mean, stat_name="Mean")

# * Variance
# print_stat_from_description(description.variance, stat_name="Variance")

# # * Standard deviation
# std = np.std(dataset)
# print_stat_from_description(pd.Series.to_numpy(std), stat_name="Standard deviation")

# # # * Skewness
# print_stat_from_description(description.skewness, stat_name="Skewness")

# # * Kurtosis
# print_stat_from_description(description.kurtosis, stat_name="Kurtosis")

print(dataset)
# print(type(dataset))

# stat, p = wilcoxon(age, sex)
# print('Statistics=%.3f, p=%.3f' % (stat, p))

# ! ------------------------- TEST shapiro + mann whitney U -----------------------------

# class_1_df = dataset[dataset['Class'] == 1]
# class_2_df = dataset[dataset['Class'] == 2]

# rest_blood_pressure_c1 = class_1_df["RestBloodPressure"].to_list()
# rest_blood_pressure_c2 = class_2_df["RestBloodPressure"].to_list()

# shapiro_test_blood_pressure_c1 = stats.shapiro(rest_blood_pressure_c1) # rozkład nie jest normany
# shapiro_test_blood_pressure_c2 = stats.shapiro(rest_blood_pressure_c2) # rozkład nie jest normany

# print(stats.mannwhitneyu(rest_blood_pressure_c1, rest_blood_pressure_c2))

# print(shapiro_test_blood_pressure_c1)
# print(shapiro_test_blood_pressure_c2)

# ! ------------------------- TEST shapiro + Kruskal-Wallis -----------------------------

# class_1_df = dataset[dataset['Class'] == 1]
# class_2_df = dataset[dataset['Class'] == 2]
# class_3_df = dataset[dataset['Class'] == 3]

# attribute = "Age"
# age_c1 = class_1_df[attribute].to_list()
# age_c2 = class_2_df[attribute].to_list()
# age_c3 = class_3_df[attribute].to_list()

# shapiro_age_c1 = stats.shapiro(age_c1) # rozkład nie jest normany
# shapiro_age_c2 = stats.shapiro(age_c2) # rozkład nie jest normany
# shapiro_age_c3 = stats.shapiro(age_c3) # rozkład nie jest normany

# # print(stats.mannwhitneyu(rest_blood_pressure_c1, rest_blood_pressure_c2))

# print(shapiro_age_c1)
# print(shapiro_age_c2)
# print(shapiro_age_c3)

# kruskal_test = stats.kruskal(shapiro_age_c1, shapiro_age_c2, shapiro_age_c3)
# print(kruskal_test)

# ! ------------------------- TEST shapiro + Paired t-test  -----------------------------

class_1_df = dataset[dataset['Gender'] == 'M']
class_2_df = dataset[dataset['Gender'] == 'F']

attribute = "KmAfter"
attr_list_c1 = class_1_df[attribute].to_list()
print(np.var(attr_list_c1))

attr_list_c2 = class_2_df[attribute].to_list()
print(np.var(attr_list_c2))

shapiro_attr_list_c1 = stats.shapiro(attr_list_c1) # rozkład  jest normany
shapiro_attr_list_c2 = stats.shapiro(attr_list_c2) # rozkład  jest normany
# shapiro_age_c3 = stats.shapiro(age_c3) # rozkład nie jest normany

print(shapiro_attr_list_c1)
print(shapiro_attr_list_c2)

print(stats.ttest_ind(shapiro_attr_list_c1, shapiro_attr_list_c2, equal_var=True))


# print(shapiro_age_c3)

# kruskal_test = stats.kruskal(shapiro_age_c1, shapiro_age_c2, shapiro_age_c3)
# print(kruskal_test)

