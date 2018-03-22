(function() {
  'use strict';

  angular
    .module('users.portal')
    .controller('navBarController', navBarController)
    .controller('asideController', asideController);

  /* navBarController
   * @desc: This will display the navigation bar
   */
  function navBarController($scope, $rootScope, UserService) {
    var self = this;

    self.UserService = UserService;

    self.onProfileClick = function() {
      $rootScope.isProfileBarActive = true;
    };

  }; // end of NavBarCtrl

  /* aside Controller
   * @desc: This will display the user profile in sidebar
   */
  function asideController($scope, $rootScope, UserService) {
    var self = this;

    self.UserService = UserService;

    self.onProfileClose = function () {
      $rootScope.isProfileBarActive = false;
    }

  }; // end of aside Controller

})();
