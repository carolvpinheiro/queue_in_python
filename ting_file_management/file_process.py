import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance.list_ting:
        instance.enqueue(path_file)
        return format_data(path_file)


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()
        return sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    if len(instance) < position:
        return sys.stderr.write("Posição inválida")
    else:
        return format_data(instance.list_ting[position])


def format_data(path_file):
    list_file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_file),
        "linhas_do_arquivo": list_file
    }
    sys.stdout.write(f"{data}")
