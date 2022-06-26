# See LICENSE file for full copyright and licensing details.

from datetime import datetime, date
from odoo import models, api

class StudentReport2(models.AbstractModel):
    _name = 'report.cms_student.report_template_2_id'
    _description = "Report Template 2"
    
    def get_month(self, indate):
        new_date = datetime.strptime(str(indate), '%Y-%m-%d')
        out_date = new_date.strftime('%B') + '-' + new_date.strftime('%Y')
        return out_date

    def get_company_name(self):
        company = self.env.company
        company_str = ""
        
        if company.street:
            company_str += " " + company.street + ", "
        
        if company.city:
            company_str += " " + company.city + ", "
        
        if company.country_id:
            company_str += " " + company.country_id.name + ". "
        
        if company.phone:
            company_str += " Ph: " + company.phone
            
        company_str = "National University of Computer and Emerging Sciences"
        return company_str.upper()
    
    @api.model
    def _get_report_values(self, docids, data=None):
        print("_____________________________********************")
        company = self.env.company
        data['company_name'] = company.name
        data['company_logo'] = company.logo
        data['company_lang'] = company.partner_id.lang
        
        #report_model = self.env['ir.actions.report']._get_report_from_name('cms_student.report_template_2_id')

        print(data)
        print("+______________________________+")
        print(docids)
        
        return {
            'doc_ids' : docids,
            #'doc_model': report_model.model,
            'doc_model' : self.env['cms.student'],
            'data' : data,
            'docs' : self.env['cms.student'].browse(docids),
            'get_month': self.get_month,
            'get_company_name': self.get_company_name,
        }
