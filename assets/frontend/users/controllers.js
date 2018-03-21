(function () {
  'use strict';

  angular
    .module('users.portal')
    .controller('navBarController', navBarController)
    .controller('asideController', asideController)
    .controller('dashboardController', dashboardController)

  /* navBarController
   * @desc: This will display the navigation bar
   */
  function navBarController($scope, $rootScope, UserServices) {
    var self = this;

    self.UserServices = UserServices;

    self.onProfileClick = function() {
      $rootScope.isProfileBarActive = true;
    };

  }; // end of NavBarCtrl

  /* aside Controller
   * @desc: This will display the user profile in sidebar
   */
  function asideController($scope, $rootScope, UserServices) {
    var self = this;

    self.UserServices = UserServices;

    self.onProfileClose = function () {
      $rootScope.isProfileBarActive = false;
    }

  }; // end of aside Controller


  /* Dashboard Controller
  * @desc: This will display the paginated invoices
  */
  function dashboardController ($scope, InvoiceService) {
    this.InvoiceService = InvoiceService;
  };

})();

