

from os_populate_database_data import PopulateDatabaseData


@auth.requires(auth.has_membership(group_id='Admins'))
def index():
    response.title = T("TEST SERVER")
    response.subtitle = T("populate database")
    response.view = 'general/only_content.html'

    PDD = PopulateDatabaseData()

    content= PDD.get_buttons()

    return dict(content = content)