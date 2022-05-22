def save(data, filename):
    data.to_csv(f"csv/{filename}.csv", index=False)
    data.to_excel(f"excel/{filename}.xlsx",  sheet_name=filename, index=False)
    data.to_json(f"json/{filename}.json", orient='records')
