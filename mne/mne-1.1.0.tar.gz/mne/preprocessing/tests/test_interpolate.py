import os.path as op
import numpy as np

import pytest

from mne.preprocessing import equalize_bads, interpolate_bridged_electrodes
from mne import io, pick_types, read_events, Epochs

base_dir = op.join(op.dirname(__file__), '..', '..', 'io', 'tests', 'data')
raw_fname = op.join(base_dir, 'test_raw.fif')
event_name = op.join(base_dir, 'test-eve.fif')
raw_fname_ctf = op.join(base_dir, 'test_ctf_raw.fif')

event_id, tmin, tmax = 1, -0.2, 0.5
event_id_2 = 2


def _load_data():
    """Load data."""
    # It is more memory efficient to load data in a separate
    # function so it's loaded on-demand
    raw = io.read_raw_fif(raw_fname).pick(['eeg', 'stim'])
    events = read_events(event_name)
    # subselect channels for speed
    picks = pick_types(raw.info, meg=False, eeg=True, exclude=[])[:15]
    epochs = Epochs(raw, events, event_id, tmin, tmax, picks=picks,
                    preload=True, reject=dict(eeg=80e-6))
    evoked = epochs.average()
    return raw.load_data(), epochs.load_data(), evoked


@pytest.mark.parametrize('interp_thresh', [0., 0.5, 1.])
@pytest.mark.parametrize('inst_type', ['raw', 'epochs', 'evoked'])
def test_equalize_bads(interp_thresh, inst_type):
    """Test equalize_bads function."""
    raw, epochs, evoked = _load_data()

    if inst_type == 'raw':
        insts = [raw.copy().crop(0, 1), raw.copy().crop(0, 2)]
    elif inst_type == 'epochs':
        insts = [epochs.copy()[:1], epochs.copy()[:2]]
    else:
        insts = [evoked.copy().crop(0, 0.1), raw.copy().crop(0, 0.2)]

    with pytest.raises(ValueError, match='between 0'):
        equalize_bads(insts, interp_thresh=2.)

    bads = insts[0].copy().pick('eeg').ch_names[:3]
    insts[0].info['bads'] = bads[:2]
    insts[1].info['bads'] = bads[1:]

    insts_ok = equalize_bads(insts, interp_thresh=interp_thresh)
    if interp_thresh == 0:
        bads_ok = []
    elif interp_thresh == 1:
        bads_ok = bads
    else:  # interp_thresh == 0.5
        bads_ok = bads[1:]

    for inst in insts_ok:
        assert set(inst.info['bads']) == set(bads_ok)


def test_interpolate_bridged_electrodes():
    """Test interpolate_bridged_electrodes function."""
    raw, epochs, evoked = _load_data()
    for inst in (raw, epochs, evoked):
        idx0 = inst.ch_names.index('EEG 001')
        idx1 = inst.ch_names.index('EEG 002')
        ch_names_orig = inst.ch_names.copy()
        bads_orig = inst.info['bads'].copy()
        inst2 = inst.copy()
        inst2.info['bads'] = ['EEG 001', 'EEG 002']
        inst2.interpolate_bads()
        data_interp_reg = inst2.get_data(picks=['EEG 001', 'EEG 002'])
        inst = interpolate_bridged_electrodes(inst, [(idx0, idx1)])
        data_interp = inst.get_data(picks=['EEG 001', 'EEG 002'])
        assert not any(['virtual' in ch for ch in inst.ch_names])
        assert inst.ch_names == ch_names_orig
        assert inst.info['bads'] == bads_orig
        # check closer to regular interpolation than original data
        assert 1e-6 < np.mean(np.abs(data_interp - data_interp_reg)) < 5.4e-5
