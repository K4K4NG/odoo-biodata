from odoo import models, fields, api
from datetime import date


class biodata(models.Model):
    _name = 'latihan.biodata'
    _description = 'Latihan Biodata'

    name = fields.Char(string='Nama', required=True)
    fullname = fields.Char(string='Nama Lengkap', required=True)
    birthdate = fields.Date(string='Tanggal Lahir')
    age = fields.Integer(string='Umur', compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Laki-laki'), ('female', 'Perempuan')],
                              string='Jenis Kelamin')
    children = fields.Integer(string='Anak')
    foto = fields.Binary(string='Foto')
    education_sd = fields.Boolean(string='SD')
    education_smp = fields.Boolean(string='SMP')
    education_sltp = fields.Boolean(string='SLTP')
    education_sma = fields.Boolean(string='SMA')
    education_smk = fields.Boolean(string='SMK')
    education_smu = fields.Boolean(string='SMU')
    education_slta = fields.Boolean(string='SLTA')
    education_college = fields.Boolean(string='Kuliah')

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = date.today()
                record.age = today.year - record.birthdate.year - (
                    (today.month, today.day)
                    < (record.birthdate.month, record.birthdate.day))
            else:
                record.age = 0
