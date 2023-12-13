from odoo import models, fields, api, _
import json


class AccountMoveInherit(models.Model):

    _inherit = "account.move"

    def _get_data(self, data):
        return json.loads(data)

    def get_igst_amount(self):
        for rec in self:
            data = self._get_data(rec.tax_totals_json)
            for group in data.get("groups_by_subtotal", {}).get("Untaxed Amount", []):
                if group.get("tax_group_name") == "IGST":
                    return group.get("tax_group_amount")
            return 0

    def get_sgst_amount(self):
        for rec in self:
            data = self._get_data(rec.tax_totals_json)
            for group in data.get("groups_by_subtotal", {}).get("Untaxed Amount", []):
                if group.get("tax_group_name") == "SGST":
                    return group.get("tax_group_amount")
            return 0

    def get_cgst_amount(self):
        for rec in self:
            data = self._get_data(rec.tax_totals_json)
            for group in data.get("groups_by_subtotal", {}).get("Untaxed Amount", []):
                if group.get("tax_group_name") == "CGST":
                    return group.get("tax_group_amount")
            return 0
    
    def get_discount(self):
        disc=0
        for rec in self.line_ids:
            if rec.discount:
                disc += (rec.price_unit*rec.discount)/100
        return disc

            
    def get_sub_total_amount(self):
        for rec in self:
            data = self._get_data(rec.tax_totals_json)
            return data.get("amount_untaxed", 0)
        return 0
    
    def get_total_bill_amount(self):
        for rec in self:
            data = self._get_data(rec.tax_totals_json)
            return data.get("amount_total", 0)
        return 0
    
    def get_proforma_invoice(self):
        return self.env.ref('pakeeza.action_report_proforma_invoice').report_action(self.id)
    
    def get_tax_invoice(self):
        return self.env.ref('pakeeza.action_report_tax_invoice').report_action(self.id)