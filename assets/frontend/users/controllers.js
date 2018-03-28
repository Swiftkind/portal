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
  function navBarController($scope, $rootScope, UserService, InvoiceService,
    $state) {
    var self = this;

    self.UserService = UserService;

    self.onProfileClick = function() {
      $rootScope.isProfileBarActive = true;
    };

    /* Call create invoice service 
     */
     self.createInvoice = function(){
      var invoice = {};
      invoice.invoice_date = new Date();
      invoice.due_date = new Date();
      invoice.customer = 1;
      InvoiceService
        .create(invoice)
        .then(function (response) {
          InvoiceService.list.push(response.data);
          $state.go('invoiceDetail', {id: response.data.id});
        });
     }

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
