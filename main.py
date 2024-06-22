import pandas as pd
from data_validator import is_phone_number, is_email, is_name, is_cuantia

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        return content

def filter_data(data):
    """
    
    - nombre / not null
    - numero de telefono / null
    - correo / null
    - cuantia / null
    
    si no tienen numero de telefono, no se incluyen
    """
    record = {}
    
    item = data.split("\n")
    for item_data in item:
        if is_name(item_data):
            record["nombre"] = item_data
        elif is_phone_number(item_data):
            record["telefono"] = item_data
        elif is_email(item_data):
            record["correo"] = item_data
        elif is_cuantia(item_data):
            #record["cuantia"] = item_data.replace("Income - ", "")
            record["cuantia"] = item_data
    if "telefono" not in record:
        record = {}
    return record

def extract_data(file_content):
    """
    This function extracts the data from the file .txt
    
    - separate the data by line
    - check record by record
    """
    data = file_content.split("\n\n")
    temp_record = []
    results = []
    
    for item in data:
        temp_record = filter_data(item)
        if temp_record == {}:
            continue
        results.append(temp_record)
        
    return results

def convert_to_dataframe(data):
    columns = ["nombre", "telefono", "correo", "cuantia"]
    df = pd.DataFrame(data, columns=columns)
    return df

def export_to_xlsx(df, file_name):
    df.to_excel(file_name, index=False)
    print("file exported to xlsx")
    
    
def main():
    file_name = "data.txt"
    file_content = read_file(file_name)
    data = extract_data(file_content)
    print("data extracted")
    #print(data)
    df = convert_to_dataframe(data)
    print("data converted to dataframe")
    #print(df)
    export_to_xlsx(df, "data.xlsx")
    
if __name__ == "__main__":
    main()