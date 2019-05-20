import src.filters as filters
import src.utils as utils
import src.datasus_downloader as datasus_downloader

# todo: mapear ranges e retornar msg quando nao tem
# todo nao baixar tudo de novo se para o extractor_script
def execution_by_cmd():
    system, from_filter, to_filter, file_types, states = filters.get_filters()
    date_range = utils.get_date_range(from_filter, to_filter)
    datasus_downloader.download_and_convert(system, date_range, file_types, states)
    #
    # date_range = utils.get_date_range('02/2017', '02/2017')
    # datasus_downloader.download_and_convert("SIASUS", date_range, ["AB"], ["SP"])

# Let`s rock!
execution_by_cmd()
