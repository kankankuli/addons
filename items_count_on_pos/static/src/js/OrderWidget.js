odoo.define('items_count_on_pos.OrderWidget', function (require) {
    'use strict';

    var screens = require('point_of_sale.screens');

    screens.OrderWidget.include({
        update_summary: function(){
            this._super();
            var order = this.pos.get_order();
            if (!order.get_orderlines().length) {
                return;
            }

            var total_items = order ? order.getTotalItems() : 0;
            var total_qty = order ? order.getTotalQuantity() : 0;

            this.el.querySelector('.summary span.total_items').textContent = total_items;
            this.el.querySelector('.summary span.total_qty').textContent = total_qty;
        },
    });
});
