# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Category(models.Model):
    _name = 'personal_monthly_budget.categorias'
    _description = 'categorias'

    name = fields.Char(string='Nombre de Categoria')
class Finanza(models.Model):
    _name = 'personal_monthly_budget.finanza'
    _description = 'Seguimiento Ingresos y Egresos'

    Descripcion = fields.Char(string='Descripcion', required=True)
    Monto = fields.Float(string='Monto', required=True)
    Fecha = fields.Date(required=True)
    Categoria = fields.Many2one('personal_monthly_budget.categorias', string = 'Categoria')
    tipo = fields.Selection([('ingreso', 'Ingreso'), ('egreso', 'Egreso')], string='tipo', default='Ingreso')
    display_monto = fields.Float(string='Monto', compute='_compute_display_monto', store=True, invisible=True)

@api.depends('Monto', 'tipo')
def _compute_display_monto(self):
    for record in self:
        # If tipo is 'egreso', make Monto negative; otherwise, keep it as is
        record.display_monto = -record.Monto if record.tipo == 'Egreso' else record.Monto