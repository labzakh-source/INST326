with open("names_raw.txt") as f:
    names = [line.strip().lower() for line in f]
    filtered_list = [name for name in names if len(name) > 3]
    print(len(filtered_list))