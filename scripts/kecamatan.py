import pandas as pd
from scripts.savefile import save

list_kabkota = pd.read_csv("csv/kabkota.csv")

data_kecamatan = pd.DataFrame()

for index, row in list_kabkota.iterrows():
    print(f"Get {index}/{len(list_kabkota)}")
    url = "https://sig.bps.go.id/rest-bridging/getwilayah?level=kecamatan&parent=" + \
        str(row["kode_bps"])
    temp = pd.read_json(url)
    data_kecamatan = pd.concat([data_kecamatan, temp])

# Save Data
save(data_kecamatan, "kecamatan")
