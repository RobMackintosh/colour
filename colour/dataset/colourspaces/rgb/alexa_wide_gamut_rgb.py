# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**alexa_wide_gamut_rgb.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines **Colour** package *ALEXA Wide Gamut RGB* colourspace.

**Others:**

"""

from __future__ import unicode_literals

import math

import numpy

import colour.computation.colourspaces.rgb.derivation
import colour.dataset.illuminants.chromaticity_coordinates
from colour.computation.colourspaces.rgb.colourspace import Colourspace


__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["ALEXA_LOG_C_CURVE_BCL_DATA",
           "ALEXA_LOG_C_CURVE_CONVERSION_DATA",
           "ALEXA_WIDE_GAMUT_RGB_PRIMARIES",
           "ALEXA_WIDE_GAMUT_RGB_WHITEPOINT",
           "ALEXA_WIDE_GAMUT_RGB_TO_XYZ_MATRIX",
           "XYZ_TO_ALEXA_WIDE_GAMUT_RGB_MATRIX",
           "ALEXA_WIDE_GAMUT_RGB_TRANSFER_FUNCTION",
           "ALEXA_WIDE_GAMUT_RGB_INVERSE_TRANSFER_FUNCTION",
           "ALEXA_WIDE_GAMUT_RGB_COLOURSPACE"]


# http://www.arri.com/?eID=registration&file_uid=8026
ALEXA_LOG_C_CURVE_BCL_DATA = {"SUP 3.x": {160: (0.0928, 0.8128),
                                          200: (0.0928, 0.8341),
                                          250: (0.0928, 0.8549),
                                          320: (0.0928, 0.8773),
                                          400: (0.0928, 0.8968),
                                          500: (0.0928, 0.9158),
                                          640: (0.0928, 0.9362),
                                          800: (0.0928, 0.9539),
                                          1000: (0.0928, 0.9711),
                                          1280: (0.0928, 0.9895),
                                          1600: (0.0928, 1.0000),
                                          2000: (0.0928, 1.0000),
                                          2560: (0.0928, 1.0000),
                                          3200: (0.0928, 1.0000)},
                              "SUP 2.x": {160: (0.1083, 0.8110),
                                          200: (0.1115, 0.8320),
                                          250: (0.1146, 0.8524),
                                          320: (0.1181, 0.8743),
                                          400: (0.1213, 0.8935),
                                          500: (0.1245, 0.9121),
                                          640: (0.1280, 0.9320),
                                          800: (0.1311, 0.9494),
                                          1000: (0.1343, 0.9662),
                                          1280: (0.1378, 0.9841),
                                          1600: (0.1409, 0.9997)}}

ALEXA_LOG_C_CURVE_CONVERSION_DATA = {"SUP 3.x": {"Normalised Sensor Signal": {
    160: (0.004680, 40.0, -0.076072, 0.269036, 0.381991, 42.062665, -0.071569, 0.125266),
    200: (0.004597, 50.0, -0.118740, 0.266007, 0.382478, 51.986387, -0.110339, 0.128643),
    250: (0.004518, 62.5, -0.171260, 0.262978, 0.382966, 64.243053, -0.158224, 0.132021),
    320: (0.004436, 80.0, -0.243808, 0.259627, 0.383508, 81.183335, -0.224409, 0.135761),
    400: (0.004369, 100.0, -0.325820, 0.256598, 0.383999, 100.295280, -0.299079, 0.139142),
    500: (0.004309, 125.0, -0.427461, 0.253569, 0.384493, 123.889239, -0.391261, 0.142526),
    640: (0.004249, 160.0, -0.568709, 0.250219, 0.385040, 156.482680, -0.518605, 0.146271),
    800: (0.004201, 200.0, -0.729169, 0.247190, 0.385537, 193.235573, -0.662201, 0.149658),
    1000: (0.004160, 250.0, -0.928805, 0.244161, 0.386036, 238.584745, -0.839385, 0.153047),
    1280: (0.004120, 320.0, -1.207168, 0.240810, 0.386590, 301.197380, -1.084020, 0.156799),
    1600: (0.004088, 400.0, -1.524256, 0.237781, 0.387093, 371.761171, -1.359723, 0.160192)},
                                                 "Linear Scene Exposure Factor": {
                                                     160: (0.005561, 5.555556, 0.080216, 0.269036, 0.381991, 5.842037,
                                                           0.092778, 0.125266),
                                                     200: (0.006208, 5.555556, 0.076621, 0.266007, 0.382478, 5.776265,
                                                           0.092782, 0.128643),
                                                     250: (0.006871, 5.555556, 0.072941, 0.262978, 0.382966, 5.710494,
                                                           0.092786, 0.132021),
                                                     320: (0.007622, 5.555556, 0.068768, 0.259627, 0.383508, 5.637732,
                                                           0.092791, 0.135761),
                                                     400: (0.008318, 5.555556, 0.064901, 0.256598, 0.383999, 5.571960,
                                                           0.092795, 0.139142),
                                                     500: (0.009031, 5.555556, 0.060939, 0.253569, 0.384493, 5.506188,
                                                           0.092800, 0.142526),
                                                     640: (0.009840, 5.555556, 0.056443, 0.250219, 0.385040, 5.433426,
                                                           0.092805, 0.146271),
                                                     800: (0.010591, 5.555556, 0.052272, 0.247190, 0.385537, 5.367655,
                                                           0.092809, 0.149658),
                                                     1000: (0.011361, 5.555556, 0.047996, 0.244161, 0.386036, 5.301883,
                                                            0.092814, 0.153047),
                                                     1280: (0.012235, 5.555556, 0.043137, 0.240810, 0.386590, 5.229121,
                                                            0.092819, 0.156799),
                                                     1600: (0.013047, 5.555556, 0.038625, 0.237781, 0.387093, 5.163350,
                                                            0.092824, 0.16019)}},
                                     "SUP 3.x": {"Normalised Sensor Signal": {
                                         160: (0.003907, 36.439829, -0.053366, 0.269035, 0.391007, 45.593473, -0.069772,
                                               0.10836),
                                         200: (0.003907, 45.549786, -0.088959, 0.266007, 0.391007, 55.709581, -0.106114,
                                               0.11154),
                                         250: (0.003907, 56.937232, -0.133449, 0.262978, 0.391007, 67.887153, -0.150510,
                                               0.11472),
                                         320: (0.003907, 72.879657, -0.195737, 0.259627, 0.391007, 84.167616, -0.210597,
                                               0.11824),
                                         400: (
                                             0.003907, 91.099572, -0.266922, 0.256598, 0.391007, 101.811426, -0.276349,
                                             0.12142),
                                         500: (
                                             0.003907, 113.874465, -0.355903, 0.253569, 0.391007, 122.608379, -0.354421,
                                             0.12461),
                                         640: (
                                             0.003907, 145.759315, -0.480477, 0.250218, 0.391007, 149.703304, -0.456760,
                                             0.12813),
                                         800: (
                                             0.003907, 182.199144, -0.622848, 0.247189, 0.391007, 178.216873, -0.564981,
                                             0.13131),
                                         1000: (
                                             0.003907, 227.748930, -0.800811, 0.244161, 0.391007, 210.785040, -0.689043,
                                             0.13449),
                                         1280: (
                                             0.003907, 291.518630, -1.049959, 0.240810, 0.391007, 251.689459, -0.845336,
                                             0.13801),
                                         1600: (
                                             0.003907, 364.398287, -1.334700, 0.237781, 0.391007, 293.073575, -1.003841,
                                             0.14119)},
                                                 "Linear Scene Exposure Factor": {
                                                     160: (0.000000, 5.061087, 0.089004, 0.269035, 0.391007, 6.332427,
                                                           0.108361, 0.108361),
                                                     200: (0.000000, 5.061087, 0.089004, 0.266007, 0.391007, 6.189953,
                                                           0.111543, 0.111543),
                                                     250: (0.000000, 5.061087, 0.089004, 0.262978, 0.391007, 6.034414,
                                                           0.114725, 0.114725),
                                                     320: (0.000000, 5.061087, 0.089004, 0.259627, 0.391007, 5.844973,
                                                           0.118246, 0.118246),
                                                     400: (0.000000, 5.061087, 0.089004, 0.256598, 0.391007, 5.656190,
                                                           0.121428, 0.121428),
                                                     500: (0.000000, 5.061087, 0.089004, 0.253569, 0.391007, 5.449261,
                                                           0.124610, 0.124610),
                                                     640: (0.000000, 5.061087, 0.089004, 0.250218, 0.391007, 5.198031,
                                                           0.128130, 0.128130),
                                                     800: (0.000000, 5.061087, 0.089004, 0.247189, 0.391007, 4.950469,
                                                           0.131313, 0.131313),
                                                     1000: (0.000000, 5.061087, 0.089004, 0.244161, 0.391007, 4.684112,
                                                            0.134495, 0.134495),
                                                     1280: (0.000000, 5.061087, 0.089004, 0.240810, 0.391007, 4.369609,
                                                            0.138015, 0.138015),
                                                     1600: (0.000000, 5.061087, 0.089004, 0.237781, 0.391007, 4.070466,
                                                            0.141197, 0.14119)}}}

ALEXA_WIDE_GAMUT_RGB_PRIMARIES = numpy.matrix([0.6840, 0.3130,
                                               0.2210, 0.8480,
                                               0.0861, -0.1020]).reshape((3, 2))

ALEXA_WIDE_GAMUT_RGB_WHITEPOINT = colour.dataset.illuminants.chromaticity_coordinates.ILLUMINANTS.get(
    "CIE 1931 2 Degree Standard Observer").get("D65")

ALEXA_WIDE_GAMUT_RGB_TO_XYZ_MATRIX = numpy.matrix([0.638008, 0.214704, 0.097744,
                                                   0.291954, 0.823841, -0.115795,
                                                   0.002798, -0.067034, 1.153294]).reshape((3, 3))

XYZ_TO_ALEXA_WIDE_GAMUT_RGB_MATRIX = ALEXA_WIDE_GAMUT_RGB_TO_XYZ_MATRIX.getI()


def __alexa_wide_gamut_rgb_transfer_function(value, firmware="SUP 3.x", method="Linear Scene Exposure Factor", EI=800):
    """
    Defines the *ALEXA Wide Gamut value* colourspace transfer function.

    :param value: value.
    :type value: float
    :param firmware: Alexa firmware version.
    :type firmware: unicode ("SUP 2.x", "SUP 3.x")
    :param method: Conversion method.
    :type method: unicode ("Linear Scene Exposure Factor", "Normalised Sensor Signal")
    :param EI: Ei.
    :type EI: int
    :return: Companded value.
    :rtype: float
    """

    cut, a, b, c, d, e, f, ecutf = ALEXA_LOG_C_CURVE_CONVERSION_DATA.get(firmware).get(method).get(EI)

    return c * math.log10(a * value + b) + d if value > cut else ecutf


def __alexa_wide_gamut_rgb_inverse_transfer_function(value, firmware="SUP 3.x", method="Linear Scene Exposure Factor",
                                                     EI=800):
    """
    Defines the *ALEXA Wide Gamut value* colourspace inverse transfer function.

    :param value: value.
    :type value: float
    :param firmware: Alexa firmware version.
    :type firmware: unicode ("SUP 2.x", "SUP 3.x")
    :param method: Conversion method.
    :type method: unicode ("Linear Scene Exposure Factor", "Normalised Sensor Signal")
    :param EI: Ei.
    :type EI: int
    :return: Companded value.
    :rtype: float
    """

    cut, a, b, c, d, e, f, ecutf = ALEXA_LOG_C_CURVE_CONVERSION_DATA.get(firmware).get(method).get(EI)

    return (math.pow(10, (value - d) / c) - b) / a if value > ecutf else (value - f) / e


ALEXA_WIDE_GAMUT_RGB_TRANSFER_FUNCTION = __alexa_wide_gamut_rgb_transfer_function

ALEXA_WIDE_GAMUT_RGB_INVERSE_TRANSFER_FUNCTION = __alexa_wide_gamut_rgb_inverse_transfer_function

ALEXA_WIDE_GAMUT_RGB_COLOURSPACE = Colourspace("ALEXA Wide Gamut RGB",
                                             ALEXA_WIDE_GAMUT_RGB_PRIMARIES,
                                             ALEXA_WIDE_GAMUT_RGB_WHITEPOINT,
                                             ALEXA_WIDE_GAMUT_RGB_TO_XYZ_MATRIX,
                                             XYZ_TO_ALEXA_WIDE_GAMUT_RGB_MATRIX,
                                             ALEXA_WIDE_GAMUT_RGB_TRANSFER_FUNCTION,
                                             ALEXA_WIDE_GAMUT_RGB_INVERSE_TRANSFER_FUNCTION)
