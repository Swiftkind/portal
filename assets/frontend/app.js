(function() {
    'use strict';

    angular
        .module('portal', [
            'ui.router',
            'ngAnimate',
            'ngSanitize',
            'ngTouch',
            'ui.bootstrap',
            'invoices.portal',
            'users.portal',
            'dashboard.portal',
        ])
        .constant('TEMPLATE_URL', '/static/frontend/templates/')
    ;

})();
