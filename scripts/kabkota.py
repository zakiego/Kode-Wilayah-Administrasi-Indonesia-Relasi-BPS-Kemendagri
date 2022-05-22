
import pandas as pd
from scripts.savefile import save


list_provinsi = pd.read_csv("csv/provinsi.csv")

data_kabkota = pd.DataFrame()

for index, row in list_provinsi.iterrows():
    url = "https://sig.bps.go.id/rest-bridging/getwilayah?level=kabupaten&parent=" + \
        str(row["kode_bps"])
    temp = pd.read_json(
        url, dtype={'kode_bps': 'str', 'nama_bps': 'str', 'kode_dagri': 'str', 'nama_dagri': 'str', })
    data_kabkota = pd.concat([data_kabkota, temp])


data_kabkota['kode_dagri'] = data_kabkota['kode_dagri'].str.replace(".", "")

# Save Data
save(data_kabkota, "kabkota")
