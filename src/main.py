import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats
from scipy.stats import wilcoxon, shapiro, friedmanchisquare
from loaders import KeelDatasetLoader
import scikit_posthocs as sp    #



np.set_printoptions(suppress=True)

dataset_loader = KeelDatasetLoader()

theroid_dataset = dataset_loader.load('thyroid.dat')
print(theroid_dataset)

sample_1 = theroid_dataset.sample(n=100)


# * freidmanschi test
tsh_s1 = sample_1["TSH"].to_list()
t3_s1 = sample_1["T3"].to_list()
tt4_s1 = sample_1["TT4"].to_list()
# tsh_c2 = sample_1[attribute].to_list()

shapiro_test_tsh_s1 = stats.shapiro(tsh_s1)
shapiro_test_t3_s1 = stats.shapiro(t3_s1)
shapiro_test_tt4_s1 = stats.shapiro(tt4_s1)
# shapiro_test_tsh_c2 = stats.shapiro(tsh_c2)

print(shapiro_test_tsh_s1)
print(shapiro_test_t3_s1)
print(shapiro_test_tt4_s1)
# print(shapiro_test_tsh_c2)

freidman_outcome = friedmanchisquare(tsh_s1, t3_s1, tt4_s1)
print(freidman_outcome)

# sp.posthoc_conover(theroid_dataset, val_col='Sepal.Width', group_col='Species', p_adjust = 'holm')
pc = sp.posthoc_conover(theroid_dataset, val_col='TSH', group_col='Class')
heatmap_args = {'linewidths': 0.25, 'linecolor': '0.5', 'clip_on': False, 'square': True, 'cbar_ax_bbox': [0.80, 0.35, 0.04, 0.3]}
plot = sp.sign_plot(pc, **heatmap_args)
print(plot)
print(type(plot))
plt.savefig('foo.png')


# print(samples)

# * Test Friedmana rank
# freidman_outcome = friedmanchisquare(*samples)
# print(freidman_outcome)

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

# dataset = pd.read_csv(
#     file_path_survey,
#     names=headers_survey,
#     index_col=None,
#     delimiter=';'
# )

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

# print(dataset)
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

# class_1_df = dataset[dataset['Gender'] == 'M']
# class_2_df = dataset[dataset['Gender'] == 'F']

# attribute = "KmAfter"
# attr_list_c1 = class_1_df[attribute].to_list()
# print(np.var(attr_list_c1))

# attr_list_c2 = class_2_df[attribute].to_list()
# print(np.var(attr_list_c2))

# shapiro_attr_list_c1 = stats.shapiro(attr_list_c1) # rozkład  jest normany
# shapiro_attr_list_c2 = stats.shapiro(attr_list_c2) # rozkład  jest normany
# # shapiro_age_c3 = stats.shapiro(age_c3) # rozkład nie jest normany

# print(shapiro_attr_list_c1)
# print(shapiro_attr_list_c2)

# print(stats.ttest_ind(shapiro_attr_list_c1, shapiro_attr_list_c2, equal_var=True))


# print(shapiro_age_c3)

# kruskal_test = stats.kruskal(shapiro_age_c1, shapiro_age_c2, shapiro_age_c3)
# print(kruskal_test)

