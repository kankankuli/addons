odoo.define("pos_search_limit.db", function(require) {
    "use strict";
    var PosDB = require("point_of_sale.DB");
    PosDB.include({
        limit: 8, // The maximum number of results returned by a search
    });
});
