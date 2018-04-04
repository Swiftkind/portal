(function() {
  'use strict';

  angular
      .module('portal')
      .config(routes);

  function routes($stateProvider, $urlRouterProvider, $locationProvider,
                  $httpProvider, $urlMatcherFactoryProvider, TEMPLATE_URL) {


    $urlRouterProvider.otherwise('/login/');
    $urlMatcherFactoryProvider.strictMode(false);
    $locationProvider.html5Mode(true);

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $stateProvider
      .state('legacy', {
          abstract: true,
      });
  };

})();
