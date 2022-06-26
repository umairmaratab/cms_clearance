{
    'name': 'Student Clearance',
    'version': '15.0.1.0.0',
    'author': 'Umair',
    'website': 'http://www.edu.pk',
    'category': 'Student Management System',
    'license': "AGPL-3",
    'Summary': 'A Module For Student Management System',
    'images': ['static/description/icon.jpg'],
    'depends': ['base'],
    'data': ['security/cms_student_security.xml',
             'security/ir.model.access.csv',
             'data/cms_student_sequences.xml',
             'wizard/wizard_report_3_view.xml',
             # 'views/cms_courses.xml',
             # 'views/cms_block.xml',
             # 'views/cms_room.xml',
             # 'views/cms_timeslot.xml',
             # 'views/cms_schedule.xml',
             # 'views/cms_schedulerline.xml',
             # 'views/cms_prerequisite.xml',
             # 'views/cms_passed_courses.xml',
             # 'views/cms_offered_courses.xml',
             'views/cms_department_view.xml',

             'views/cms_student_view.xml',
             # 'views/cms_section_groups.xml',
             # 'views/cms_sections.xml',

             # 'views/cms_sections.xml',
             'views/cms_clearance.xml',
             # 'report/report_1_view.xml',
             # 'report/report_2_view.xml',
             'report/report_3_view.xml',
             'report/report.xml',
             'views/cms_student_menu.xml'],
            
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_method_run_before_installation',
}
