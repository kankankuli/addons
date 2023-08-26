odoo.define('items_count_on_pos.models', function (require) {
    "use strict";
  
    const models = require("point_of_sale.models");

    models.load_fields("pos.order.line", "generated_gift_card_ids");
    models.load_fields("pos.order.line", "redeem_pos_order_line_ids");

    var _order_super = models.Order.prototype;
    models.Order = models.Order.extend({
	    getTotalQuantity() {
            var product_qty = 0;
            for (let line of this.orderlines.models) {
                if (line.quantity){
                    product_qty = product_qty + line.quantity;
                }
            }
            return product_qty;
        },

        getTotalItems() {
            var product_ids = [];
            for (let line of this.orderlines.models) {
                if(!product_ids.includes(line.product.id)){
                    product_ids.push(line.product.id);
                }                
            }
            return product_ids.length;
        },

        export_for_printing: function() {
            var json = _order_super.export_for_printing.apply(this,arguments);
            json.total_items = this.getTotalItems();
            json.total_qty = this.getTotalQuantity();
            return json;
        },
    });

  
});
  