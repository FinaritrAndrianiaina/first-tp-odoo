from odoo import models,fields

class Cours(models.Model):
    _name="cours.cours"
    #_inherits={"res.partner":"enseignant"}

    titre = fields.Char("titre")
    date_de_debut = fields.Date()
    date_de_fin = fields.Date()
    enseignant = fields.Many2one('res.partner',ondelete="cascade",string="Enseignant")