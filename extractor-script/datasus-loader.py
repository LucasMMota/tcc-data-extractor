import src.filters as filters
import src.datasus_downloader as datasus_downloader
from src.utils import build_file_path, get_downloaded_size
from src.converter import dbc2csv


# todo: mapear ranges e retornar msg quando nao tem
# todo nao baixar tudo de novo se para o extractor-script
def main():
    print('Iniciando carga de dados...')

    for date in filters.getDateRange():
        for file_type in filters.get_types():
            for state in filters.states():
                print('Data: ' + date)
                print('Tipo de arquivos: ' + file_type)
                print('UF: ' + state)

                # Todo add limit de dados....
                # downloaded_size = get_downloaded_size()
                # if downloaded_size >= filters.getDownloadLimit():
                #     print("Download limit reached: " + str(downloaded_size))
                #     print("Stopping...")
                #     exit(1)

                path_file, filename = build_file_path(filters.system(), file_type, date, state)

                # Downloads files into raw-files
                datasus_downloader.download(path_file, filename)

                # Converts files and sabe on converted-files
                dbc2csv(filename)

                # Todo load into db
                # Todo apagar arquivos

# Let`s rock!
main()
