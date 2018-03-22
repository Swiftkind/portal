(function() {
    'use strict';

    angular
        .module('users.portal')
        .service('UserService', UserService);

    /* User Services
     * @desc: A function that gets the user data from the endpoint
     */
    function UserService($http, API_URL) {
        var service = {
            user: null,
        };
        usersDetail();
        return service;

        // Returns a users detail data from the API
        function usersDetail() {
            return $http.get(API_URL + 'users/auth/')
            .then(function (resp) {
                service.user = resp.data;
            });
        };
    };

})();
