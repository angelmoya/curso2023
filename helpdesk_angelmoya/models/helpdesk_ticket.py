from odoo import fields, models

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Helpdesk Ticket'
    

    # Nombre
    name = fields.Char(
        required=True,
        help="Resume en procas palabras un titulo para la incidencia."
    )

    # Secuencia
    sequence = fields.Integer(
        default=10,
        help="Secuencia para el orden de las incidencias."
    )

    # Descripción
    description = fields.Text(
        help="Escribe detalladamente la incidencia y como replicarla.",
        default="""Version a la que afecta:
    Modulo:
    Pasos para replicar:
    Modulos personalizados:
        """
    )
    
    # Fecha
    date = fields.Date()
    
    # Fecha y hora limite
    date_limit = fields.Datetime(
        string='Limit Date & Time')
    
    # Asignado (Verdadero o Falso), que sea de solo lectura
    assigned = fields.Boolean(
        readonly=True,
    )

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assignet to')
    
    # Acciones a realizar (Html)
    actions_todo = fields.Html()
    
    # Añadir el campo Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('assigned', 'Assigned'),
            ('in_process', 'In Process'),
            ('pending', 'Pending'),
            ('resolved', 'Resolved'),
            ('canceled', 'Canceled'),
        ],
        default='new',
    )

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        # relation='helpdesk_ticket_tag_rel',
        # column1='ticket_id',
        # column2='tag_id',
        string='Tags')
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions')
    
    

    
    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()
    
    color = fields.Integer('Color Index', default=0)