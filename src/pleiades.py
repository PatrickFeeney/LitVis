from pathlib import Path

import pandas as pd
import numpy as np


class PleiadesLookup:
    def __init__(self, pleiades_fpath) -> None:
        df = pd.read_csv(Path(pleiades_fpath))
        self.df_filtered = df[["nameAttested", "nameLanguage", "nameTransliterated", "reprLat",
                               "reprLong", "title", "uid"]]
        self.namesTransliterated = np.array(df["nameTransliterated"], dtype=str)

    def get_name_refs(self, names):
        """Get Pleiades indices for list of place names

        Args:
            names (np.array): 1D array of strings containing place names

        Returns:
            list: List of 1D np.array(dtype=int) of variable length.
                  Entries contain Pleiades indices referencing given name.
        """
        refs = []
        for name in names:
            index_list = np.where(name == self.namesTransliterated)[0]
            refs.append(index_list)
        return refs
