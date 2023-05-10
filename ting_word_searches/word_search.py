def exists_word(word, instance):
    exit_structure = []

    for index in range(len(instance)):
        occurences = []
        dict_lines = instance.search(index)
        for i, line in enumerate(dict_lines["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurences.append({"linha": i + 1})
        if occurences:
            exit_structure.append({
                "palavra": word,
                "arquivo": dict_lines["nome_do_arquivo"],
                "ocorrencias": occurences
            })
    return exit_structure


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
