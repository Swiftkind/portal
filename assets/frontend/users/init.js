(function() {
    'use strict';

    angular
        .module('users.portal', [])
        .constant('TEMPLATE_URL', '/static/frontend/templates/users/')
        .constant('API_URL', '/api/users/auth/')
    ;

})();
