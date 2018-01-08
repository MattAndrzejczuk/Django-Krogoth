(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdToast, $timeout, $log, BreedList, DogAPI) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.toastMsg = '';
        vm.RESTfulJSONPayload = {};

        // vm.getObjectList = getObjectList;
        // vm.postNewObject = postNewObject;
        // vm.deleteObject = deleteObject;

        vm.$onInit = onInit;
        vm.$onDestroy = onDestroy;


        vm.selectedDogBreed = {};
        vm.newDogData = {img: '', breed: ''};
        vm.dogBreedSearchText = '';

        vm.breedSearchTextDidChange = breedSearchTextDidChange;
        vm.didSelectDogBreed = didSelectDogBreed;
        vm.filterThis = filterThis;

        vm.addRandomDogButtonClicked = addRandomDogButtonClicked;
        vm.getRandomElementFromArray = getRandomElementFromArray;
        vm.getImageForBreed = getImageForBreed;

        vm.userDogCards = [];

        vm.breedSelectionList = BreedList.message;
        $log.log('BREED SELECTION LIST');
        $log.log(vm.breedSelectionList);


        function onInit() {
            // vm.getObjectList();
        }

        function onDestroy() {
            alert('MVC did terminate.');
        }

        function didSelectDogBreed(strBreed) {
            if (strBreed) {
                $log.info('Dog breed selected: ' + strBreed);
                vm.newDogData.breed = strBreed;
                vm.getImageForBreed(strBreed);
            }
        }

        function breedSearchTextDidChange() {
            $log.info(vm.dogBreedSearchText);
        }

        /// search stringArray, return matching strings using the 'usingString' param.
        function filterThis(stringArray, usingString) {
            ///c1.innerHTML = 'searching: ' + stringArray;
            var matched = [];
            /// for str_ in strings
            for (var i = 0; i < stringArray.length; i++) {
                var str_ = stringArray[i];
                console.info(str_);
                console.info((str_.toUpperCase().indexOf(usingString.toUpperCase())));
                if (str_.toLowerCase().indexOf(usingString) !== -1) {
                    /// found a matching string.
                    matched.push(str_);
                }
            }
            return matched;
        }


        function getRandomElementFromArray(array_) {
            return array_[Math.floor(Math.random() * (array_.length - 0) + 0)];
        }

        function addRandomDogButtonClicked() {
            const breedName = vm.getRandomElementFromArray(vm.breedSelectionList);
            vm.newDogData.breed = breedName;
            vm.getImageForBreed(breedName);
        }

        function getImageForBreed(named) {
            DogAPI.getImageForSpecific(named)
                .then(function (response) {
                    vm.newDogData.img = vm.getRandomElementFromArray(response.message);
                    var dog = {
                        breed: vm.newDogData.breed,
                        img: vm.newDogData.img
                    };
                    $log.log(dog);
                    vm.userDogCards.push(dog);
                    $mdToast.show({
                        template: '<md-toast style="background-color: lawngreen">' +
                        named + ' Added.</md-toast>',
                        hideDelay: 3000,
                        position: 'bottom right'
                    });
                });
        }

        // function getObjectList() {
        //     $log.info('GET request initiating...');
        //     RESTfulModelI.getList().then(function (data) {
        //         $log.info('GET response from server: ');
        //         $log.log(data);
        //         vm.jsonResponse = data.results;
        //     });
        // }

        // function deleteObject(withId) {
        //     RESTfulModelI.deleteObject(withId).then(function (data) {
        //         vm.jsonResponse.pop(data);
        //     });
        // }

        // function postNewObject() {
        //     RESTfulModelI.postNewObject(vm.RESTfulJSONPayload).then(function (data) {
        //         $log.info('POST response from server: ');
        //         $log.log(data);
        //         vm.jsonResponse.push(data);
        //     });
        // }


    }
})();