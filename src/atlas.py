import csv
import json
from pathlib import Path

import numpy as np
import pandas as pd


class NamedEntityCollectionExtractor:
    """
    Extracts an ATLAS named entity collection
    """

    def extract(self):
        input_path = Path("data/output/phi0474.phi056.perseus-lat1/sorted_locs.csv")
        names = [r[0] for r in csv.reader(input_path.open())]
        df = pd.read_csv("data/pleiades/pleiades-names.csv")
        namesTransliterated = np.array(df["nameTransliterated"], dtype=str)
        names_to_pids = {}
        for name in names:
            index_list = np.where(name == namesTransliterated)[0]
            if len(index_list) > 0:
                hits = df[["pid", "title", "reprLat", "reprLong"]].iloc[index_list]
                for pos, _ in enumerate(index_list):
                    hit = hits.iloc[pos]
                    if not pd.isna(hit["reprLat"]):
                        names_to_pids[name] = hit["pid"]
                        break
                else:
                    names_to_pids[name] = hit["pid"]

        with open("data/output/phi0474.phi056.perseus-lat1/pids.json", "w") as f:
            json.dump(
                names_to_pids,
                f,
                sort_keys=True,
                ensure_ascii=False,
                indent=2,
            )

class TextExtractor:
    """
    Extracts an ATLAS text
    """
