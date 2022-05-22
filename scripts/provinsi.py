import pandas as pd

from scripts.savefile import save

data_provinsi = pd.read_json(
    "https://sig.bps.go.id/rest-bridging/getwilayah?level=provinsi&parent=0")

# Save Data
save(data_provinsi, "provinsi")
