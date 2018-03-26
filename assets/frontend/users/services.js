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
            updateProfile: updateProfile,
        };
        usersDetail();
        return service;

        // Returns a users detail data from the API
        function usersDetail() {
            return $http.get(API_URL)
            .then(function (resp) {
                service.user = resp.data;
            });
        }; // end of function userDetail

        // Update the user data from the API
        function updateProfile(data) {
            return $http.post(API_URL, data)
            .then(function (resp) {
                service.updateProfile = resp.data;
            }).catch(function(error){
                console.log(error);
            });
        }; // end of function updateProfile

    }; // End of UserServices

})();
