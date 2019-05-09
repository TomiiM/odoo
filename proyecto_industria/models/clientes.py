from odoo import models,api,fields

class clientes(models.Model):
	_name="proyecto_industria.clientes"
	_descripcion = "Clientes"

	nombre = fields.Char('Nombre')
	apellido = fields.Char('Apellido')
	identidad = fields.Char('Numero de empleado')
	identidad = fields.Char('cargo')