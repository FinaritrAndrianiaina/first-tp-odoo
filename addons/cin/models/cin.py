from odoo import models,fields

class Cin(models.Model):
    _name="res.partner"
    _inherits="res.partner"

    cin = fields.Char("N° CIN")
