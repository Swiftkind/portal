(function() {
  'use strict';

  angular
    .module('users.portal')
    .directive('navBar', navBar)
    .directive('profileBar', profileBar);

  /* Nav bar directive
   * @desc:
   */
  function navBar(TEMPLATE_URL) {
    var directive = {
      restrict: 'EA',
      templateUrl: TEMPLATE_URL + 'navbar.html',
      controller: 'navBarController',
      controllerAs: 'ctrl',
      bindToController: true
    };
    return directive;
  }; // end of NavBar

  function profileBar(TEMPLATE_URL) {
    var directive = {
      restrict: 'E',
      scope: {
        active: '='
      },
      templateUrl: TEMPLATE_URL + 'users/update_profile.html',
      controller: 'asideController',
      controllerAs: 'ctrl',
      bindToController: true
    };
    return directive;
  } // end of profieBar


})();
