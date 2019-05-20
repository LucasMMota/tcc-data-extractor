import src.filters as filters
import src.datasus_downloader as datasus_downloader

# todo: mapear ranges e retornar msg quando nao tem
# todo nao baixar tudo de novo se para o extractor_script
def execution_by_cmd():
    system, date_range, file_types, states = filters.get_filters()
    datasus_downloader.download_and_convert(system, date_range, file_types, states)


# Let`s rock!
execution_by_cmd()
