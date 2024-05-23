def reescrevendo(seu_arquivo):
    with open(seu_arquivo, 'r') as infile:
        lines = infile.readlines()
    with open(seu_arquivo, 'w') as outfile:
        for idx, row in enumerate(lines):
            if (idx + 1) % 2 == 0:
                outfile.write(row)
    return seu_arquivo