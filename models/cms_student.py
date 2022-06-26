# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date
from odoo.exceptions import UserError, ValidationError


class CMSDepartment(models.Model):
    _name = 'cms.department'
    _description = 'Department Information'

    name = fields.Char('Department Name', required=True)
    student_ids = fields.One2many('cms.student', 'department_id', string='Students')


class CMSStudent(models.Model):
    _name = 'cms.student'
    _description = 'Student Information'

    name = fields.Char('Student Name', required=True)
    father_name = fields.Char('Father Name', required=True)
    registration_no = fields.Char(string='Registration No.', required=True)
    department_id = fields.Many2one('cms.department', string='Department')
    cnic = fields.Char(string='Student CNIC')
    contact_phone = fields.Char('Phone no.')
    contact_mobile = fields.Char('Mobile no')
    image = fields.Binary('image')
    admission_date = fields.Date('Admission Date', default=date.today())
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Gender', states={'done': [('readonly', True)]}, required=True)

    user_id = fields.Many2one('res.users', string='Responsible', readonly=True, default=lambda self: self.env.user)
    date_of_birth = fields.Date('Date of Birth')
    age = fields.Integer(compute='_compute_student_age', string='Age', readonly=True)
    admission_no = fields.Char(string='Admission No.', readonly=True)
    grad_date = fields.Integer(compute= '_compute_grad_date', string='Graduation Date', readonly=True)

    remark = fields.Text('Remark', states={'done': [('readonly', True)]})

    state = fields.Selection([('draft', 'Draft'), ('verified', 'Verified'), ('approved', 'Approved'),
                              ('cancelled', 'Cancelled')], 'Status', readonly=True, default="draft")

    active = fields.Boolean(default=True)

    employee_ids = fields.Many2many('cms.employee', 'cms_student_employee_rel',
        'student_id', 'employee_id', string='Employees')

    @api.depends('date_of_birth')
    def _compute_student_age(self):
        '''Method to calculate student age'''
        current_date = date.today()
        for rec in self:
            if rec.date_of_birth:
                start = rec.date_of_birth
                age = (current_date - start).days / 365
                # Age should be greater than 0
                if age > 0.0:
                    rec.age = age
                else:
                    rec.age = 0
            else:
                rec.age = 0

    @api.depends('admission_date')
    def _compute_grad_date(self):
        '''Method to calculate expected graduation date'''
        for rec in self:
            if rec.admission_date:
                rec.grad_date = (rec.admission_date).year + 4


    def set_to_draft(self):
        '''Method to change state to draft'''
        self.state = 'draft'

    def set_to_verified(self):
        '''Method to change state to verified'''
        self.state = 'verified'

    def set_to_approved(self):
        '''Method to change state to approved'''

        if self.admission_date:
            year = self.admission_date.year
            self.admission_no  = str(year) + "-" + self.env['ir.sequence'].next_by_code('cms.student.code')
        else:
            raise ValidationError(_('Please enter admission date for student %s)', self.name))

        self.state = 'approved'

    def set_to_cancelled(self):
        '''Set the state to cancelled'''
        self.state = 'cancelled'



###########################################################################


class CMSClearance(models.Model):
    _name = 'cms.clearance'
    _description = 'Clearance Information'

    name = fields.Char('Student Name', required=True)
    registration_no = fields.Char('Registration No.', required=True)
    is_cleared = fields.Char(string="Status" , readonly=True, default='Not Cleared', required=True)


    is_cleared_from_academics = fields.Boolean(string='Academics?')
    is_cleared_from_transport = fields.Boolean(string='Transport?')
    is_cleared_from_hostel = fields.Boolean(string='Hostel?')
    is_cleared_from_accounts = fields.Boolean(string='Accounts?')


    remark = fields.Text('Remark', states={'done': [('readonly', True)]})


    active = fields.Boolean(default=True)

    state = fields.Selection([('draft', 'Draft'), ('academics', 'Academics'), ('transport', 'Transport'),
                              ('hostel', 'Hostel'),('accounts', 'Accounts'), ('approved', 'Approved'),
                              ('cancelled', 'Cancelled')], 'Status', readonly=True, default="draft")




    def set_to_draft(self):
        '''Method to change state to draft'''
        self.state = 'draft'

    def set_to_verified(self):
        '''Method to change state to verified'''
        self.state = 'verified'

    # def set_to_approved(self):
    #     '''Method to change state to approved'''
    #
    #
    #     self.state = 'approved'

    def set_to_cancelled(self):
        '''Set the state to cancelled'''
        self.state = 'cancelled'

    def set_to_academics(self):
        '''Set the state to cancelled'''


        self.state = 'academics'

    def set_to_hostel(self):
        '''Set the state to cancelled'''
        if self.is_cleared_from_transport:
            self.state = 'hostel'


        else:
            raise ValidationError('Please Check the related box')
        # self.state = 'hostel'
    def set_to_accounts(self):
        '''Set the state to cancelled'''
        if self.is_cleared_from_hostel:
            self.state = 'accounts'


        else:
            raise ValidationError('Please Check the related box')
    def set_to_transport(self):
        if self.is_cleared_from_academics:
            self.state = 'transport'


        else:
            raise ValidationError('Please Check the related box')
        # self.state = 'transport'

    def set_to_approved(self):
        '''Method to change state to approved'''

        if self.is_cleared_from_accounts:
            if self.is_cleared:
                self.is_cleared = "Cleared"

            self.state = 'approved'


        else:
            raise ValidationError('Please Check the related box')


