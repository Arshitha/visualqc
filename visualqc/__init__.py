# -*- coding: utf-8 -*-

"""Top-level package for visualqc."""

__all__ = ['outlier_advisory',
           'gather_freesurfer_data',
           'read_aparc_stats_in_hemi',
           'read_aseg_stats',
           'read_aparc_stats_wholebrain',
           ]

__author__ = """Pradeep Reddy Raamana"""
__email__ = 'raamana@gmail.com'

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

from visualqc.readers import (gather_freesurfer_data, read_aparc_stats_in_hemi,
                              read_aseg_stats, read_aparc_stats_wholebrain)
from visualqc.outliers import outlier_advisory

# dealing with matplotlib backend
import os
import matplotlib


def set_agg():
    """set agg as backend"""

    matplotlib.use('Agg')
    matplotlib.interactive(False)


if 'DISPLAY' in os.environ:
    display = os.environ['DISPLAY']
    display_name, display_num = display.split(':')
    display_num = int(float(display_num))
    if display_num != 0:
        set_agg()
else:
    set_agg()
    display = None
