import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    data = txt_importer(path_file)
    exit_structure = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }

    instance.enqueue(exit_structure)
    sys.stdout.write(str(exit_structure))
    return exit_structure


def remove(instance):
    if instance.__len__() < 1:
        return print("Não há elementos")

    delete = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    return print(f"Arquivo {delete} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= instance.__len__():
        sys.stderr.write("Posição inválida")
    else:
        data = instance.search(position)
        print(data)
