/** @odoo-module **/

import {WebClient} from "@web/webclient/webclient"
const { patch } = require("@web/core/utils/patch");


patch(WebClient.prototype, "title patch", {
    setup() {
        this._super();
        this.title.setParts({ zopenerp: "LOKA" });
    },
});
