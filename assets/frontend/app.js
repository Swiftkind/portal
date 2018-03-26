(function() {
    'use strict';

    angular
        .module('portal', [
            'ui.router',
            'invoices.portal',
            'users.portal',
        ])
        .constant('TEMPLATE_URL', '/static/frontend/templates/')
    ;

})();
