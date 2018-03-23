(function() {
  'use strict';

  angular
    .module('users.portal')
    .controller('navBarController', navBarController)
    .controller('asideController', asideController)
  ;

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
   * @desc: This will display the user profile detail in sidebar
   */
  function asideController($scope, $rootScope, UserService) {
    var self = this;
    var enableEdit = false;
    feather.replace();

    self.UserService = UserService;

    self.onProfileClose = function () {
      $rootScope.isProfileBarActive = false;
    };

    self.editProfile = function () {
      self.enableEdit = true;
    };

    self.saveUser = function () {
      self.enableEdit = false;

      UserService.updateProfile(UserService.user);
    };

  }; // end of aside Controller

})();
