import pandas as pd
from scripts.savefile import save

list_kabkota = pd.read_csv("csv/kabkota.csv")

data_kecamatan = pd.DataFrame()

for index, row in list_kabkota.iterrows():
    print(f"Get {index}/{len(list_kabkota)}")
    url = "https://sig.bps.go.id/rest-bridging/getwilayah?level=kecamatan&parent=" + \
        str(row["kode_bps"])
    temp = pd.read_json(
        url, dtype={'kode_bps': 'str', 'nama_bps': 'str', 'kode_dagri': 'str', 'nama_dagri': 'str', })
    data_kecamatan = pd.concat([data_kecamatan, temp])

data_kecamatan['kode_dagri'] = data_kecamatan['kode_dagri'].str.replace(
    ".", "")

# Save Data
save(data_kecamatan, "kecamatan")
