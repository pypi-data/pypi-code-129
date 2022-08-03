
from dbm_test123.opendbm.model import AudioModel 
from dbm_test123.dbm_lib.dbm_features.raw_features.audio.gne import run_gne
import pandas as pd

class GlottalNoiseRatio(AudioModel):
    def __init__(self):
        super().__init__()
        self._params = ['aco_gne']
        
    @AudioModel.prep_func 
    def _fit_transform(self, path, **kwargs):
        return run_gne(path, '.', self.r_config, save=False, ff_df=kwargs['ff_df'])
