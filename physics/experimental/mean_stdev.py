import numpy as np


def get_values_list():
    values_list = [float(x) for x in input().split()]

    return values_list


def mean(values_list):
    values_array = np.array(values_list)

    return np.mean(values_array, axis=0)


def stdev(values_list):
    values_array = np.array(values_list)

    return np.std(values_array, axis=0)


def variance(values_list):
    values_array = np.array(values_list)

    return np.var(values_array, axis=0)


def covariance(first_values_list, second_values_list):
    first_values_array = np.array(first_values_list)
    second_values_array = np.array(second_values_list)

    return np.cov(first_values_array, second_values_array)
