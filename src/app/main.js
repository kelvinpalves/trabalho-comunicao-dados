(function () {

    'use strict';

    angular
        .module('app')
        .controller('Principal', Principal);

    Principal.$inject = ['$scope'];

    function Principal($scope) {
        var vm = this;

        vm.model = {};

        $scope.$watch('vm.model.mensagem', function () {
            if (angular.isDefined(vm.model) && angular.isDefined(vm.model.mensagem)) {
                vm.model.binario       = converterStringParaBinario(vm.model.mensagem);
                vm.model.mensagemSaida = gerarObjetoExibicao(vm.model.mensagem);
            } else {
                delete vm.model.binario;
                delete vm.model.mensagemSaida;
            }
        });

        function converterStringParaBinario(mensagem) {
            var saida = [];
            for (var i = 0; i < mensagem.length; i++) {
                saida.push(mensagem.charCodeAt(i).toString(2));
            }
            return saida;
        }

        function gerarObjetoExibicao (mensagem) {
            var saida = [];
            for (var i = 0; i < mensagem.length; i++) {
                saida.push({
                    letra: mensagem[i],
                    ascii: mensagem.charCodeAt(i),
                    binario: (mensagem.charCodeAt(i).toString(2)).padStart(8, '0')
                });
            }
            return saida;
        }
    }


})();