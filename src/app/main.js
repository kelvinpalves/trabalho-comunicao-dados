(function () {

    'use strict';

    angular
        .module('app')
        .controller('Principal', Principal);

    Principal.$inject = ['$scope', '$http', '$interval'];

    function Principal($scope, $http, $interval) {
        var vm = this;

        vm.imagens = [
            { titulo: 'NRZ-L', src: "backend/tmp/grafico-nrz.png?" + new Date().getTime()},
            { titulo: 'ASK', src: "backend/tmp/grafico-ask.png?" + new Date().getTime()},
            { titulo: 'Domínio da Frequência', src: "backend/tmp/grafico-fft.png?" + new Date().getTime()},
            { titulo: 'Demodulação', src: "backend/tmp/grafico-ifft.png?" + new Date().getTime()}
        ];
    }
})();