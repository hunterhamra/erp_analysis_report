from mini_mne import SimpleRaw


def preprocess(raw: SimpleRaw, reref_params: list | None, filter_low_cutoff: float | None = None, filter_high_cutoff: float | None = None):
    """
    Preprocess EEG data using the mini_mne package.

    Apply a custom reference to re-reference the data and apply a bandpass filter as specified.

    Parameters
    ----------
    raw: SimpleRaw
        A mini_mne SimpleRaw object.
    reref_params: list or None
        Parameters for rereferencing: either a list of electrodes (typically mastoids or proxies for mastoids) or None to calculate an average reference.
    filter_low_cutoff: float, optional
        The low cutoff for bandpass filtering. Optional; defaults to None (no low cutoff).
    filter_high_cutoff: float
        The high cutoff for bandpass filtering. Optional; defaults to None (no high cutoff).
    """

    # re-reference
    raw_reref = raw.re_reference(reref_params)

    # filter
    raw_filtered = raw_reref.filter(
        l_freq = filter_low_cutoff,
        h_freq = filter_high_cutoff
    )

    return raw_filtered
