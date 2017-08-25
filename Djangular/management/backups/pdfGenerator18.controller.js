(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $mdDialog, $scope) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';
        vm.downloadPDF = downloadPDF;
        vm.samplePDF = samplePDF;
        vm.canvasTest = canvasTest;
        vm.generateAllImagesToPDF = generateAllImagesToPDF;
        vm.getInnerText = getInnerText;
        vm.showDialog = showDialog;
        vm.getInnerText = getInnerText;

        /// REPLACE ALL STRINGS WITH STRING FLOW:______________________________________
        var uncut = 'Holy fuck, I hope this motherfucking fuck will censor this profane fucking string.';
        var censored = uncut.replace(/fuck/g, "#$%@!");
        //censored = Holy #$%@!, I hope this mother#$%@!ing #$%@! will censor this profane #$%@!ing string.
        ///____________________________________________________________________________



        $scope.videoElem = document.getElementById("videoPlayOnHover");
        $scope.videoCanPlay = false;
        $scope.isPlaying = false;

        if (document.getElementById("videoPlayOnHover").canPlayType === false)
            console.error('This browser does not support HTML5 video.');

        $scope.hoverOnVideo = function() {
            console.log('mouse did hover autovideo');
            if ($scope.videoCanPlay === true) {
                $scope.videoElem.play();
                $scope.videoElem.muted = false;
                $scope.isPlaying = true;
            } else {
                console.error('HTML5 Video appears to not exist ! !');
            }
        };

        $scope.unhoverOnVideo = function() {
            console.log('the mouse left the hover autovideo');
            if ($scope.videoCanPlay === true) {
                $scope.videoElem.pause();
                $scope.videoElem.muted = true;
                $scope.isPlaying = false;
            } else {
                console.error('HTML5 Video appears to not exist ! !');
            }
        };

        var vid = document.getElementById("videoPlayOnHover");
        vid.onloadstart = function() {
            console.log("1. Starting to load video");
        };
        vid.ondurationchange = function() {
            console.log("2. The video duration has changed");
            $scope.videoCanPlay = true;
        };
        vid.onloadedmetadata = function() {
            console.log("3. Meta data for video loaded");
        };
        vid.onloadeddata = function() {
            console.log("4. Browser has loaded the current frame");
        };
        vid.onprogress = function() {
            console.log("5. Downloading video");
            $scope.videoCanPlay = true;
        };
        vid.oncanplay = function() {
            console.log("6. Can start playing video");
        };
        vid.oncanplaythrough = function() {
            console.log("7. Can play through video without stopping");
        };



        function img_find() {
            var imgs = document.getElementsByTagName("img");
            var imgSrcs = [];
            for (var i = 0; i < imgs.length; i++) {
                imgSrcs.push(imgs[i]);
            }
            return imgSrcs;
        }

        function generateAllImagesToPDF() {
            var doc = new jsPDF();
            var imgs = document.getElementsByName("gallery");
            for (var i = 0; i < imgs.length; i++) {
                var x = 0;
                var y = (i * 50);

                if (i % 2 === 0) {
                    x = 10;
                    y = (i * 50);
                } else {
                    x = 110;
                    y = (i * 50) - 50;
                }
                y += 3;

                var callbackFinal = function(image) {
                    var canvas = document.createElement("canvas");
                    var ctx = canvas.getContext("2d");
                    if (!image) image = this;
                    canvas.width = image.width;
                    canvas.height = image.height;
                    ctx.drawImage(image, 0, 0);
                    var imgData = canvas.toDataURL("image/jpg");
                    doc.addImage(imgData, 'JPEG', x, y + 150, 85, 85);
                    doc.save();
                    $log.log('finished image list');
                }
                var callback = function(image) {
                    var canvas = document.createElement("canvas");
                    var ctx = canvas.getContext("2d");
                    if (!image) image = this;
                    canvas.width = image.width;
                    canvas.height = image.height;
                    ctx.drawImage(image, 0, 0);
                    var imgData = canvas.toDataURL("image/jpg");
                    doc.addImage(imgData, 'JPEG', x, y, 85, 85);
                    $log.log('image did load! with y at:');
                    $log.info(y);
                }

                $log.debug(i);
                if (i === imgs.length - 2) {
                    if (imgs[i].complete) { //check if image was already loaded by the browser
                        callbackFinal(imgs[i]);
                    } else {
                        imgs[i].onload = callbackFinal;
                    }
                } else {
                    if (imgs[i].complete) { //check if image was already loaded by the browser
                        callback(imgs[i]);
                    } else {
                        imgs[i].onload = callback;
                    }
                }
            }
        }

        function canvasTest() {
            var img = document.getElementById('img11');
            var canvas = document.createElement("canvas");
            var ctx = canvas.getContext("2d");
            var doc = new jsPDF();
            var callback = function(image) {
                if (!image) image = this;
                canvas.width = img.width;
                canvas.height = img.height;
                ctx.drawImage(image, 0, 0);
                var imgData = canvas.toDataURL("image/jpg");
                doc.addImage(imgData, 'JPEG', 15, 40, 100, 100);
                doc.save();
                $log.log(img_find());
            }

            if (img.complete) { //check if image was already loaded by the browser
                callback(img);
            } else {
                img.onload = callback;
            }
        }

        function samplePDF() {
            var doc = new jsPDF();
            doc.text('Column, Row', 10, 10);
            doc.text('50, 10', 50, 10);
            doc.text('100, 10', 100, 10);
            doc.text('150, 10', 150, 10);
            doc.text('200, 10', 200, 10);

            doc.text('10, 50', 10, 50);
            doc.text('10, 100', 10, 100);
            doc.text('10, 150', 10, 150);
            doc.text('10, 200', 10, 200);
            doc.text('10, 250', 10, 250);
            doc.text('10, 300', 10, 300);

            doc.text('50, 50', 50, 50);
            doc.text('100, 100', 100, 100);
            doc.text('150, 150', 150, 150);
            doc.text('200, 200', 200, 200);

            var base_image = new Image();
            base_image.src = '/static/upwork/10-schoolLogo.png';
            $log.debug('base_image.src');
            $log.log(base_image.src);
            base_image.onload = function() {
                var canvas = document.getElementById("myCanvas");
                canvas.width = 100;
                canvas.height = 100;
                var ctx = canvas.getContext("2d");
                ctx.drawImage(base_image, 100, 100);
                var imgData = canvas.toDataURL("image/jpg");
                $log.debug('imgData');
                $log.log(imgData);
                doc.addImage(imgData, 'JPEG', 15, 40, 180, 160);
                doc.save();
            }
        }


        function downloadPDF() {
            $log.log('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -');
            var pdf = new jsPDF('p', 'pt', 'letter');
            $log.info('pdf');
            $log.debug(pdf);
            $log.log('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -');
            var source = $('#posts-landing')[0];
            $log.info('source');
            $log.debug(source);
            $log.log('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -');
            var specialElementHandlers = {
                '#bypassme': function(element, renderer) {
                    return true
                }
            };
            $log.info('specialElementHandlers');
            $log.debug(specialElementHandlers);
            $log.log('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -');
            var margins = {
                top: 30,
                bottom: 30,
                left: 20,
                width: '50%'
            };
            $log.info('margins');
            $log.debug(margins);
            $log.log('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -');
            var options = {
                format: 'JPEG',
                "background": '#000'
            };
            $log.info('options');
            $log.debug(options);
            $log.log('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -');
            pdf.fromHTML(
                source, margins.left, margins.top, {
                    'width': margins.width,
                    'elementHandlers': specialElementHandlers
                },
                function(dispose) {
                    var d = new Date().toISOString().slice(0, 19).replace(/-/g, "");
                    pdf.save('Report_' + d + '.pdf');

                    $log.info('dispose');
                    $log.debug(dispose);
                    $log.log('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -');
                    //pdf.save('Report.pdf');
                }, margins)
        }


        function showDialog($event) {
            $mdDialog.show({
                targetEvent: $event,
                template: '<md-dialog>' +
                    '  <md-dialog-content> {{ titleFromOutside }} ' +
                    '<br>' +
                    '<textarea>{{ termsAndConditions }}</textarea>' +
                    '</md-dialog-content>' +
                    '  <md-dialog-actions>' +
                    '    <md-button ng-click="closeDialog()" class="md-primary">' +
                    '      close' +
                    '    </md-button>' +
                    '  </md-dialog-actions>' +
                    '</md-dialog>',
                controller: EULAController,
                onComplete: afterShowAnimation,
                locals: {
                    eulaTitle: 'Terms and Conditions',
                    termsAndConditions: vm.getInnerText()
                }
            });

            function afterShowAnimation(scope, element, options) {
                /// Dialog finished appearing, do something here...
            }
        }

        function EULAController($scope, $mdDialog, eulaTitle, termsAndConditions) {
            $scope.titleFromOutside = eulaTitle;
            $scope.termsAndConditions = termsAndConditions;
            $scope.closeDialog = function() {
                $mdDialog.hide();
            };
        }

        function getInnerText() {
            var el = document.getElementById('scrapeThis');
            var sel, range, innerText = "";
            if (typeof document.selection != "undefined" && typeof document.body.createTextRange != "undefined") {
                range = document.body.createTextRange();
                range.moveToElementText(el);
                innerText = range.text;
            } else if (typeof window.getSelection != "undefined" && typeof document.createRange != "undefined") {
                sel = window.getSelection();
                sel.selectAllChildren(el);
                innerText = '' + sel;
                $log.log(innerText);
                //sel.removeAllRanges();
            }
            var step = 0;
            var n = innerText.indexOf('Program high lights', 0);
            $log.log('PROGRAM HIGHLIGHTS: ');
            $log.debug(innerText.substring(n, 0));
            step = n + 'Program high lights'.length();
            n = innerText.indexOf('Gallery', step);
            $log.log('GALLERY: ');
            $log.debug(innerText.substring(n, step));
            return innerText;
        }








        /* - - - - - - - - - - - - - - - - */
    }
})();