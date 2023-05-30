lower_casing_index = []


def get_lower_case(word: str):
    for i in range(len(word)):
        if word[i] == word[i].lower():
            lower_casing_index.append(i)
    return lower_casing_index


print(get_lower_case("EsTheR"))
