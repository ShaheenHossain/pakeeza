from odoo import models, fields, api, _
import json

class ResGrade(models.Model):
    _name = "res.grade"

    name = fields.Char()

class ResFirm(models.Model):
    _name = "res.firm"

    name = fields.Char()
    
class ResTaste(models.Model):
    _name = "res.taste"

    name = fields.Char()

class ResSis(models.Model):
    _name = "res.sis"

    name = fields.Char()

class ResTCS(models.Model):
    _name = "res.tcs"

    name = fields.Char()

class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    grades = fields.Many2one("res.grade")
    firm_type = fields.Many2one("res.firm")
    area_taste = fields.Many2one("res.taste")
    concern = fields.Many2one("res.sis")
    pan_card_number = fields.Char(string="Pan Card Number")
    aadhar_card_number = fields.Char(string="Aadhar Card Number")
    district = fields.Char(string="District")
    firm_turn_over = fields.Float(string="Firm Turn Over")
    tcs = fields.Many2one("res.tcs")
    maximum_credit_days = fields.Float(string="Maximum Credit Days")
    maximum_credit_limit = fields.Float(string="Maximum Credit Limit")
    transport_name = fields.Char(string="Transport Name")
    goods_booking_place = fields.Char(string="Goods Booking Place")
    birth_date = fields.Date(string="Birth Date")
    marriage_date = fields.Date(string="Marriage Date")

        