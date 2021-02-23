# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:03:02 2021

@author: Salomé
"""
import numpy as np

from SciDataTool import DataLinspace, DataTime, DataFreq, Data1D

from mosqito.functions.sharpness.sharpness_aures import comp_sharpness_aures
from mosqito.functions.sharpness.sharpness_din import comp_sharpness_din
from mosqito.functions.sharpness.sharpness_bismarck import comp_sharpness_bismarck
from mosqito.functions.sharpness.sharpness_fastl import comp_sharpness_fastl


def compute_sharpness(self, method="din", skip=0.2):
    """Method to cumpute the sharpness according to the given method

    Parameter
    ---------
    method: string
        'din' by default, 'aures', 'bismarck', 'fastl', 'all'
    skip : float
        number of second to be cut at the beginning of the analysis

    """
    # check the input parameters
    if (
        method != "din"
        and method != "aures"
        and method != "fastl"
        and method != "bismarck"
    ):
        raise ValueError("ERROR: method must be 'din', 'aures', 'bismarck' or 'fastl")

    if skip < 0 or skip > (len(self.signal / self.fs)):
        raise ValueError(
            "ERROR: skip must be positive and inferior to the signal duration"
        )

    # compute the loudness by zwicker if not already done
    if self.loudness_zwicker == None:
        self.compute_loudness()

    if method == "din" or method == "all":
        S = comp_sharpness_din(
            self.loudness_zwicker.values,
            self.loudness_zwicker_specific.values,
            self.is_stationary,
        )

        if self.is_stationary == True:
            self.sharpness["din"] = S

        elif self.is_stationary == False:
            # Get time axis
            time = Data1D(
                name="time", unit="s", values=self.loudness_zwicker.get_axes()[1].values
            )

            # Cut transient effect
            cut_index = np.argmin(np.abs(time - skip))
            S = S[cut_index:]

            time = Data1D(
                symbol="T",
                name="Time axis",
                unit="s",
                values=np.linspace(skip, len(self.signal.values) / self.fs, num=S.size),
            )

            self.sharpness["din"] = DataTime(
                symbol="S", axes=[time], values=S, name="Sharpness", unit="Acum"
            )

    elif method == "aures" or method == "all":
        S = comp_sharpness_aures(
            self.loudness_zwicker.values,
            self.loudness_zwicker_specific.values,
            self.is_stationary,
        )

        if self.is_stationary == True:
            self.sharpness["aures"] = S

        elif self.is_stationary == False:
            # Get time axis
            time = Data1D(
                name="time", unit="s", values=self.loudness_zwicker.get_axes()[1].values
            )

            # Cut transient effect
            cut_index = np.argmin(np.abs(time - skip))
            S = S[cut_index:]

            time = Data1D(
                symbol="T",
                name="Time axis",
                unit="s",
                values=np.linspace(skip, len(self.signal.values) / self.fs, num=S.size),
            )

            self.sharpness["aures"] = DataTime(
                symbol="S", axes=[time], values=S, name="Sharpness", unit="Acum"
            )

    elif method == "bismarck" or method == "all":
        S = comp_sharpness_bismarck(
            self.loudness_zwicker.values,
            self.loudness_zwicker_specific.values,
            self.is_stationary,
        )

        if self.is_stationary == True:
            self.sharpness["bismarck"] = S

        elif self.is_stationary == False:
            # Get time axis
            time = Data1D(
                name="time", unit="s", values=self.loudness_zwicker.get_axes()[1].values
            )

            # Cut transient effect
            cut_index = np.argmin(np.abs(time - skip))
            S = S[cut_index:]

            time = Data1D(
                symbol="T",
                name="Time axis",
                unit="s",
                values=np.linspace(skip, len(self.signal.values) / self.fs, num=S.size),
            )

            self.sharpness["bismarck"] = DataTime(
                symbol="S", axes=[time], values=S, name="Sharpness", unit="Acum"
            )

    elif method == "fastl" or method == "all":
        S = comp_sharpness_fastl(
            self.loudness_zwicker.values,
            self.loudness_zwicker_specific.values,
            self.is_stationary,
        )

        if self.is_stationary == True:
            self.sharpness["fastl"] = S

        elif self.is_stationary == False:
            # Get time axis
            time = Data1D(
                name="time", unit="s", values=self.loudness_zwicker.get_axes()[1].values
            )

            # Cut transient effect
            cut_index = np.argmin(np.abs(time - skip))
            S = S[cut_index:]

            time = Data1D(
                symbol="T",
                name="Time axis",
                unit="s",
                values=np.linspace(skip, len(self.signal.values) / self.fs, num=S.size),
            )

            self.sharpness["fastl"] = DataTime(
                symbol="S", axes=[time], values=S, name="Sharpness", unit="Acum"
            )