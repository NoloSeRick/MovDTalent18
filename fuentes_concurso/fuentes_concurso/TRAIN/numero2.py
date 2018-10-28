def parse_my_file("TRAIN_FUENTE_APLICACIONES"):
    with open("TRAIN_FUENTE_APLICACIONES") as f:
        for line in f:
            yield line.strip().split(' ', 1)

df = pd.DataFrame(parse_my_file('file1'))
print(df)
