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

    db.sys_email_templates.insert(
            Name='teacher_reminder_sub_request',
            Title='Reminder sub request',
            TemplateContent="""<p>Dear {teacher_name},</p>
            <p>We would like to remind you, that there is an open {class_type} class in {class_location} on the {class_date} 
            at {class_starttime} that needs substitution.</p>
            <p>&nbsp;</p>
            <p>We thank you for considering to sub this class.</p>
            <p>&nbsp;</p>
            <p>Best regards,</p>
            <p>The Office Team</p>"""

    )
    ost = OsSchedulerTasks()
    #
    # year = request.vars['year']
    # month = request.vars['month']

    ost.teachers_reminder_sub_requests()
