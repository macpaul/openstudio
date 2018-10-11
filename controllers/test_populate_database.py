

from openstudio.os_populate_demo_data import PopulateDemoData


@auth.requires(auth.user.id==1)
def index():
    response.title = T("TEST SERVER")
    response.subtitle = T("populate database")
    response.view = 'general/only_content.html'

    PDD = PopulateDemoData()

    content= PDD.get_buttons()

    return dict(content = content)