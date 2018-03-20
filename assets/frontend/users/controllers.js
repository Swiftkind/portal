(function() {
  'use strict';

  angular
    .module('users.portal')
    .controller('navBarController', navBarController)
    .controller('asideController', asideController);

  /* navBarController
   * @desc:
   */
  function navBarController($scope, $rootScope, UserServices) {
    var self = this;

    self.UserServices = UserServices;

    self.onProfileClick = function() {
      $rootScope.isProfileBarActive = true;
    };

  }; // end of NavBarCtrl

  /* aside Controller
   * @desc:
   */
  function asideController($scope, $rootScope, UserServices) {
    var self = this;

    self.UserServices = UserServices

  }; // end of aside Controller

})();
