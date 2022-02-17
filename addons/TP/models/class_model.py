from odoo import models,fields

class StudentStudent(models.Model):
    _name = 'student.student'

    matricule = fields.Char('N° Matricule',required=True)
    name = fields.Char(srting='Nom',required=True)
    fname = fields.Char(srting='Prenom',required=True)
    gender = fields.Selection([('male','Homme'),('female','Femme')])
    student_dob = fields.Date(string="Date de naissance")
    classroom_id = fields.Many2one('classroom.classroom',ondelete="cascade",string="Classroom")

class ClassroomClassroom(models.Model):
    _name = 'classroom.classroom'

    name = fields.Char(string="Classroom name",required=True)
    students_id = fields.One2many("student.student","classroom_id",string="Students")

class ProfProf(models.Model):
    _name = 'prof.prof'

    matricule = fields.Char('N° Matricule',required=True)    
    name = fields.Char(string='Nom',required=True)
    fname = fields.Char(string='Prenom',required=True)

class ServiceService(models.Model):
    _name = 'service.service'

    name = fields.Char("Nom du service",required=True)
    professeur_id = fields.Many2one("prof.prof",ondelete="cascade",string="Professeur")
    classroom_id = fields.Many2one("classroom.classroom",ondelete="cascade",string="Classroom")
    nombredheures = fields.Integer("Nombres d'heures")