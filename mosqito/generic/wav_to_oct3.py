# -*- coding: utf-8 -*-
"""
@date Created on Tue Mar 24 2020
@author martin_g for Eomys
"""

import numpy as np
from scipy.io import wavfile
from mosqito.generic.oct3spec import oct3spec


def wav_to_oct3(file, calib=1):
    """Load .wav signal and output its third-octave band spectrum

    TODO: Longer description

    Parameters
    ----------
    file : string
        full path to the signal file
    calib : float
        calibration factor for the signal to be in [pa]

    Outputs
    -------
    spec : numpy.ndarray
        Third octave band spectrum of signal sig [pa, rms]
    fpref : numpy.ndarray
        Corresponding preferred third octave band center frequencies
    """

    fs, sig = wavfile.read(file)
    if isinstance(sig[0], np.int16):
        sig = calib * sig / (2 ** 15 - 1)
    elif isinstance(sig[0], np.int32):
        sig = calib * sig / (2 ** 31 - 1)
    spec, freq = oct3spec(sig, fs, 25, 12500)
    return spec, freq
