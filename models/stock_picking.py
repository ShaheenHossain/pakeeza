from odoo import models, fields, api
import json

class StockPickingInherit(models.Model):
    _inherit = "stock.picking"

    def sale_order_date(self, origin):
        orders = self.env['sale.order'].search([('name', '=', origin)])
        return orders

    def _get_data(self, data):
        return json.loads(data)

    def get_igst_amount(self):
        for rec in self:
            order_id = self.sale_order_date(rec.origin)
            for order in order_id:
                data = self._get_data(order.tax_totals_json)
                for group in data.get("groups_by_subtotal", {}).get("Untaxed Amount", []):
                    if group.get("tax_group_name") == "IGST":
                        return group.get("tax_group_amount")
            return 0

    def get_sgst_amount(self):
        for rec in self:
            order_id = self.sale_order_date(rec.origin)
            for order in order_id:
                data = self._get_data(order.tax_totals_json)
                for group in data.get("groups_by_subtotal", {}).get("Untaxed Amount", []):
                    if group.get("tax_group_name") == "SGST":
                        return group.get("tax_group_amount")
            return 0

    def get_cgst_amount(self):
        for rec in self:
            order_id = self.sale_order_date(rec.origin)
            for order in order_id:
                data = self._get_data(order.tax_totals_json)
                for group in data.get("groups_by_subtotal", {}).get("Untaxed Amount", []):
                    if group.get("tax_group_name") == "CGST":
                        return group.get("tax_group_amount")
            return 0
        
    def get_total_bill_amount(self):
        for rec in self:
            order_id = self.sale_order_date(rec.origin)
            for order in order_id:
                data = self._get_data(order.tax_totals_json)
                return data.get("amount_total", None)
            return 0