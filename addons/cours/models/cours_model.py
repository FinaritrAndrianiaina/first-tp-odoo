from odoo import models,fields

class Cours(models.Model):
    _name="cours.cours"
    #_inherits={"res.partner":"enseignant"}

    titre = fields.Char("titre")
    date_de_debut = fields.Date()
    date_de_fin = fields.Date()
    enseignant = fields.Many2one('res.partner',ondelete="cascade",string="Enseignant")
    tags = fields.Many2many("category.category","tags_to_category","cours_id","category_id","Tags")

class Category(models.Model):
    _name="category.category"

    name = fields.Char("Category")
    tags = fields.Many2many("cours.cours","tags_to_category","category_id","cours_id","Cours")
