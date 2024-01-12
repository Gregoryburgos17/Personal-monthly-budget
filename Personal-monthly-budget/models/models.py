# -*- coding: utf-8 -*-

from odoo import models, fields

class Category(models.Model):
    _name = 'personal_monthly_budget.categorias'
    _description = 'categorias'

    name = fields.Char(string='Nombre de Categoria')
class Finanza(models.Model):
    _name = 'personal_monthly_budget.finanza'
    _description = 'Seguimiento Ingresos y Egresos'

    Descripcion = fields.Char(string='Descripcion', required=True)
    Monto = fields.Integer(string='Monto', required=True)
    Fecha = fields.Datetime()
    Categoria = fields.Many2one('personal_monthly_budget.categorias', string = 'Categoria')
    tipo = fields.Selection([('ingreso', 'Ingreso'), ('egreso', 'Egreso')], string='tipo', default='ingreso')
