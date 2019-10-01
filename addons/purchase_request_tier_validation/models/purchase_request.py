# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from flectra import api, models


class PurchaseRequest(models.Model):
    _name = "purchase.request"
    _inherit = ['purchase.request', 'tier.validation']
    _state_from = ['draft']
    _state_to = ['approved']

    @api.model
    def _get_under_validation_exceptions(self):
        res = super(PurchaseRequest, self)._get_under_validation_exceptions()
        res.append('route_id')
        return res
