(function () {
  'user strict';

  angular
    .module('users.portal')
    .config(routes)
  ;

  function routes ($stateProvider, TEMPLATE_URL) {
    $stateProvider
      .state('login', {
          url: '/login/',
          templateUrl: TEMPLATE_URL + 'login.html',
          controller: 'LoginController',
          controllerAs: 'ctrl',
          hideNavbar: true,
      })
      .state('signup', {
        url: '/signup/',
        templateUrl: TEMPLATE_URL + 'signup.html',
        controller: 'SignUpController',
        controllerAs: 'ctrl',
        hideNavbar: true,
      });
  };

})();
