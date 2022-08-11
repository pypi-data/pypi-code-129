import logging
import warnings

import cv2
import numpy as np
from scipy.optimize import curve_fit

log = logging.getLogger(__name__)


def calc_all(data):
    """
    Calculates all QA indexes for OCT data.
    Args:
        - Data: 3d numpy array. OCT volume in format Number of slices x Height x Width
    Returns:
        - qa_index: dict. Keys:
            - Sharpness slope: array. Mean slope in transition between extra-retinal and intra-retinal regions of the OCT data.
            - Variance extraretinal: array. Mean variance of extra-retinal region of the OCT data.
            - Variance intraretinal: array. Mean variance of intra-retinal region of the OCT data.
            - Dynamic range: array. Mean Dynamic Range (ratio of brightest and darkest pixels) of OCT data
            - Outliers Slope: slice index of slices that have a slope above or below 1.5 times the Interquartile Range
            - Outliers Variance Extraretinal: slice index of slices that have a extraretinal variance above or below 1.5 times the Interquartile Range
            - Outliers Variance Intraretinal: slice index of slices that have a intraaretinal variance above or below 1.5 times the Interquartile Range
            - Outliers Dynamic range: slice index of slices that have a dynamic range above or below 1.5 times the Interquartile Range
    """
    log.info("Calculating slope....")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        slopes = calc_mean_slope(data)
    log.info("Calculating noise and signal variance....")
    variance_extraretinal, variance_intraretinal = calc_mean_variance(data)
    log.info("Calculating dynamic range...")
    dynamic_range = calc_dynamic_range(data)

    outliers_slope = find_outliers(slopes)
    outliers_variance_extraretinal = find_outliers(variance_extraretinal)
    outliers_variance_intraretinal = find_outliers(variance_intraretinal)
    outliers_dynamic_range = find_outliers(dynamic_range)

    qa_index = {
        "Dynamic range": dynamic_range,
        "Outliers Dynamic range": outliers_dynamic_range,
        "Sharpness slope": slopes,
        "Outliers Sharpness slope": outliers_slope,
        "Variance extraretinal": variance_extraretinal,
        "Outliers Variance Extraretinal": outliers_variance_extraretinal,
        "Variance intraretinal": variance_intraretinal,
        "Outliers Variance Intraretinal": outliers_variance_intraretinal,
    }

    log.debug("Calculated QA index: %s" % qa_index)

    return qa_index


def find_outliers(data):
    data_array = np.array(data)
    Q1 = np.quantile(data_array, 0.25)
    Q3 = np.quantile(data_array, 0.75)
    IQR = Q3 - Q1
    found_outliers = np.where(
        (data_array < (Q1 - 1.5 * IQR)) | (data_array > (Q3) + 1.5 * IQR)
    )
    found_outliers = found_outliers[0] + 1
    outliers = list(found_outliers)
    return outliers


def calc_mean_slope(data):
    """
    Calculates slope  in transition between extra-retinal and intra-retinal regions of each OCT slice.
    Args:
        - data: 3d numpy array. OCT volume in format Number of slices x Height x Width
    Returns:
        - slope_slice_mean: array. Mean slope in transition between extra-retinal and intra-retinal regions of eac OCT slice.
    """

    # loop across slice:
    slope_slices_mean = []
    for slice_idx in range(data.shape[0]):
        # threshold image:
        data_slice = data[slice_idx]
        thresholded_slice = threshold_image(data_slice)

        # loop across columns:
        slopes_columns_mean = []
        for column in range(data_slice.shape[1]):
            original_array = data_slice[:, column]
            thresholded_array = thresholded_slice[:, column]

            # get index of edges
            up_indexes, down_indexes = find_up_down_index(thresholded_array)

            # calculate slopes in edges
            slope_column = slope_calculation(original_array, up_indexes, down_indexes)
            # slope_column contains mean slope for that column
            slopes_columns_mean.append(np.nanmean(slope_column))

        # slope_columns_mean contains the mean slope for each column in a slice
        if slopes_columns_mean:
            slopes_columns_mean = np.nanmean(slopes_columns_mean)
            # we perform nanmean because some slopes may not be calculated based on the confidence of the fit.
        # slope slices contains
        slope_slices_mean.append(round(slopes_columns_mean, 3))
    return slope_slices_mean


def linear_fit(x, m, c):
    """
    Helper function for scipy.curve_fit.
    Args:
        - x: 2d array. Data to be fit.
        - m: float. Slope for curve fit.
        - c: float. Intercept for curve fit.
    Returns:
        - y values fitted.
    """
    return m * x + c


def slope_calculation(array, up_indexes, down_indexes):
    """
    Calculates slope for every transition region between intra-retinal and extra-retinal regions. The regions are
    flagged based on up_indexes and down_indexes.
    Args:
        - array: array. Array with column data from OCT slice.
        - up_indexes: indexes of regions of extra-retinal to intra-retinal boundary.
        - down_indexes: indexes of regions of intra-retinal to extra-retinal boundary.
    Returns:
        - slopes: list. Slope for every transition region between intra-retinal and extra-retinal regions for one column
        of one slice of OCT data.
    """
    slopes = []
    for up_index in up_indexes:
        ranges = range(up_index[0] - 1, up_index[1] + 1)
        params, _ = curve_fit(f=linear_fit, xdata=ranges, ydata=array[ranges])
        slopes.append(abs(params[0]))
    for down_index in down_indexes:
        ranges = range(down_index[0] - 1, down_index[1] + 1)

        params, _ = curve_fit(f=linear_fit, xdata=ranges, ydata=array[ranges])
        slopes.append(abs(params[0]))
    return slopes


def find_up_down_index(array, minimum_size_region=10):
    """
    Finds transition regions between intra-retinal and extra-retinal regions of one column of one slice of OCT data.
    Args:
        - array: array. Column of slice of OCT data.
    Returns:
        - up_index: list. Indexes of extra-retinal to intra-retinal regions.
        - down_index: list. Indexes of intra-retinal to extra-retinal regions.
    """
    # down_list --> intra-retinal to extra-retinal regions.
    # up_list --> extra-retinal to intra-retinal regions.
    down_list = [255, 0]
    up_list = [0, 255]
    list_array = list(array)

    # find indexes of transition regions.
    up_index = [
        (i, i + len(up_list))
        for i in range(len(list_array))
        if list_array[i : i + len(up_list)] == up_list
    ]
    down_index = [
        (i, i + len(down_list))
        for i in range(len(list_array))
        if list_array[i : i + len(down_list)] == down_list
    ]

    # find intra-retinal regions that are too small because they may be noise. If they're too small then
    # change those up_index and down_index regions to 0 in original array.
    for i in range(len(up_index)):
        size_box = len(array[range(up_index[i][0] + 1, down_index[i][1] - 1)])
        if size_box < minimum_size_region:
            array[range(up_index[i][0] + 1, down_index[i][1] - 1)] = 0

    # find indexes again now without small intra-retinal regions:
    list_array = list(array)
    up_index = [
        (i, i + len(up_list))
        for i in range(len(list_array))
        if list_array[i : i + len(up_list)] == up_list
    ]
    down_index = [
        (i, i + len(down_list))
        for i in range(len(list_array))
        if list_array[i : i + len(down_list)] == down_list
    ]

    return up_index, down_index


def calc_dynamic_range(data):
    """
    Calculate dynamic range for all slices of OCT data.
    Args:
        - data: 3d numpy array. OCT volume in format Number of slices x Height x Width.
    Returns:
        - all_drs: list. Dynamic ranges for each OCT slice..
    """
    all_drs = []
    for slice_idx in range(data.shape[0]):
        data_slice = data[slice_idx]
        dr = dynamic_range_calculation(data_slice)
        all_drs.append(round(dr, 3))
    return all_drs


def dynamic_range_calculation(image):
    """
    Calculate dynamic range of one slice in OCT data.
    Args:
        - image: 2d array. Slice of OCT data.
    Returns:
        - dr: dynamic range of OCT slice.
    """
    maxImage = np.percentile(image.flatten(), 99)
    minImage = np.percentile(image.flatten(), 1)

    if minImage == 0:
        minImage = 1

    dr = np.log10(maxImage) - np.log10(minImage)
    return dr


def calc_mean_variance(data):
    """
    Calculate variance in extra-retinal and intra-retinal regions of all slices of OCT data.
    Args:
        - data: 3d numpy array. OCT volume in format Number of slices x Height x Width.
    Returns:
        - variance_slices_mean_extraretinal: list. Mean variance of extra-retinal region of each slice in OCT volume.
        - variance_slices_mean_intraretinal: list. Mean variance of intra-retinal region of each slice in OCT volume.
    """
    # loop across slice:
    variance_slices_mean_extraretinal = []
    variance_slices_mean_intraretinal = []

    for slice_idx in range(data.shape[0]):
        # threshold image:
        data_slice = data[slice_idx]
        thresholded_slice = threshold_image(data_slice)

        # loop across columns:
        variance_columns_mean_extraretinal = []
        variance_columns_mean_intraretinal = []

        for column in range(data_slice.shape[1]):
            original_array = data_slice[:, column]
            thresholded_array = thresholded_slice[:, column]
            # remove regions that are too small because they could be noise.
            thresholded_array = filter_thresholded_image(thresholded_array)

            # calculate variance in extra-retinal and intra-retinal regions
            (
                variance_column_extraretinal,
                variance_column_intraretinal,
            ) = variance_calculation(original_array, thresholded_array)
            variance_columns_mean_extraretinal.append(
                np.nanmean(variance_column_extraretinal)
            )
            variance_columns_mean_intraretinal.append(
                np.nanmean(variance_column_intraretinal)
            )

        # slope_columns_mean contains the mean slope for each column in a slice
        variance_columns_mean_extraretinal = np.nanmean(
            variance_columns_mean_extraretinal
        )
        variance_columns_mean_intraretinal = np.nanmean(
            variance_columns_mean_intraretinal
        )

        # slope slices contains
        variance_slices_mean_extraretinal.append(
            round(variance_columns_mean_extraretinal, 3)
        )
        variance_slices_mean_intraretinal.append(
            round(variance_columns_mean_intraretinal, 3)
        )

    return variance_slices_mean_extraretinal, variance_slices_mean_intraretinal


def filter_thresholded_image(array, minimum_size_region=10):
    """
    Filter regions in thresholded image that are too small. They could be noisy areas or non-informative.
    Args:
        - array: array. Column data in OCT slice.
        - minimum_size_region: integer. Minimum size that a region needs to have. Optional argument, default 10.
    Returns:
        - array. array. Column data in OCT slice with small regions removed.

    """
    down_list = [255, 0]
    up_list = [0, 255]
    list_array = list(array)
    up_index = [
        (i, i + len(up_list))
        for i in range(len(list_array))
        if list_array[i : i + len(up_list)] == up_list
    ]
    down_index = [
        (i, i + len(down_list))
        for i in range(len(list_array))
        if list_array[i : i + len(down_list)] == down_list
    ]
    for i in range(len(up_index)):
        size_box = len(array[range(up_index[i][0] + 1, down_index[i][1] - 1)])
        if size_box < minimum_size_region:
            array[range(up_index[i][0] + 1, down_index[i][1] - 1)] = 0
    return array


def variance_calculation(array, thresholded_array):
    """
    Calculate variance in extra-retinal and intra-retinal regions of column in OCT slice.
    Args:
        - array: array. Column data in OCT slice.
        - thresholded_array: array. Thresholded column data in OCT slice.
    Returns:
        - variance_extraretinal: list. Variance of extra-retinal region of a column of a OCT slice.
        - variance_intraretinal: list. Variance of intra-retinal region of a column of a OCT slice.
    """
    variance_extraretinal = np.var(array[np.where(thresholded_array == 0)])
    variance_intraretinal = np.var(array[np.where(thresholded_array == 255)])
    return variance_extraretinal, variance_intraretinal


def threshold_image(image):
    """
    Threshold image with OTSU thresholding.
    Args:
        - image: 2d array. Slice of OCT data.
    Returns:
        - thresholded_image: 2d array. Thresholded slice of OCT data.
    """
    blur = cv2.GaussianBlur(image.astype(np.uint8), (5, 5), 0)
    _, thresholded_image = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return thresholded_image
