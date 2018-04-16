(function() {
  'use strict';

  angular
    .module('dashboard.portal')
    .directive('sideBar', sideBar)
  ;

  /* side bar directive
   * @desc: directive for invoice sidebar
   */
  function sideBar(TEMPLATE_URL) {
    var directive = {
      restrict: 'EA',
      scope: {
        active: '='
      },
      templateUrl: TEMPLATE_URL + '/dashboard/sidebar.html',
      controller: 'asideInvoiceController',
      controllerAs: 'ctrl',
      bindToController: true
    };
    return directive;
  }; // end of sideBar

})();
