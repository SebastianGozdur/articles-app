def normalizeNames(names):
    i = 0
    while i < len(names):
        names[i] = names[i].replace(".pdf", "")
        i += 1
    return names