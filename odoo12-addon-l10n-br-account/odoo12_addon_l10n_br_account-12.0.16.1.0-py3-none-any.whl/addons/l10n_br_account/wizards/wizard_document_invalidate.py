# Copyright (C) 2021  Luis Felipe Mileo - KMEE <mileo@kmee.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class InvalidateNumberWizard(models.TransientModel):
    _inherit = "l10n_br_fiscal.invalidate.number.wizard"

    def do_invalidate(self):
        super().do_invalidate()
        if self.invoice_id:
            self.invoice_id.action_cancel()
