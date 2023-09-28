def Data_data_types(data_list):
    int_data = []
    float_data = ()
    str_data = []

    for item in data_list:
        if isinstance(item, int):
            int_data.append(item)
        elif isinstance(item, float):
            float_data += (item,)
        elif isinstance(item, str):
            str_data.append(item)

    return int_data, float_data, str_data

# Contoh data list
data_list = [105, 3.1, 'Hello', 737, 'Python', 2.7 ,'World', 412 , 5.5 , 'AI']

int_data, float_data, str_data = Data_data_types(data_list)

print("Data Integer:")
print(int_data)

print("\nData Float:")
print(float_data)

print("\nData String:")
print(str_data)
