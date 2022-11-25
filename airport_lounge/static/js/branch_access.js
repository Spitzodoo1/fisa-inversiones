odoo.define('airport_lounge.access_branch', function(require){
    "use strict";
    console.log("hhhh");
    const dom = require('web.dom');
    var AbstractAction = require('web.AbstractAction');
    var ajax = require('web.ajax');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var QWeb = core.qweb;
    var ActionMenu = AbstractAction.extend({
        events: {
            'click #to_branch': '_show_mo_in_workcenter',
        },
        renderElement: function(ev){
                  console.log("hoooo");

            var self = this;

            $.when(this._super())
            .then(function(ev){

                rpc.query({
                    model: 'branch.access',
                    method: 'get_branch_access',
                    args: [,],

                }).then(function(result){
                    self.$el.empty();
                    console.log("hiiiiiiiiiiiiiiiiiii", result);
                    self.$el.append($(QWeb.render('branch_access', {branches: result})));
                })
            });
        },

        _show_mo_in_workcenter: function(ev){
            var self = this;
         this.do_action({
            type: 'ir.actions.act_window',
            res_model: 'passenger.registration',
            view_mode: 'form',
            views: [
                [false, 'list'],
                [false, 'form']
            ],
            target: 'current',
        });
        },
    });
    core.action_registry.add('access_branch', ActionMenu);
});