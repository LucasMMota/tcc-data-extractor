def build_file_path(system, file_type, date, state):
    filename = file_type + state + date + '.dbc'
    # todo verificar os paths dos sistemas
    # se o sistema e X pegar path Yx
    path = '/dissemin/publicos/'+system+'/200801_/Dados/'

    return path, filename


def get_downloaded_size():
    return 50