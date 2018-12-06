# -*- coding: utf-8 -*-

from openstudio.os_scheduler_tasks import OsSchedulerTasks


@auth.requires(auth.user_id == 1)
def index():
    """
    Function to expose class & method used by scheduler task
    to create monthly invoices
    """
    if ( not web2pytest.is_running_under_test(request, request.application)
         and not auth.has_membership(group_id='Admins') ):
        redirect(URL('default', 'user', args=['not_authorized']))


    ost = OsSchedulerTasks()
    #
    # year = request.vars['year']
    # month = request.vars['month']

    ost.teachers_reminder_sub_request()
    # scheduler.queue_task(
    #     'teachers_reminder_sub_request',
    #     pvars={},
    #     stop_time=datetime.datetime.now() + datetime.timedelta(hours=1),
    #     last_run_time=datetime.datetime(1963, 8, 28, 14, 30),
    #     timeout=1800,  # run for max. half an hour.
    # )
    #
    # session.flash = SPAN(
    #     T("Started renewing customer memberships... "),
    #     T("please refresh this page in a few minutes."), BR(),
    #     T(
    #         "Please note that you can continue to work on other things in the meantime and you don't have to wait on this page.")
    # )
    # redirect(URL('index'))
