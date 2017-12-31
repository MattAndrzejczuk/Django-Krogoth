(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController() {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.posts = [{
            "user": {
                "name": "Andrew Green",
                "avatar": "/static/assets/images/avatars/andrew.jpg"
            },
            "message": "Hey, man! Check this, it’s pretty awesome!",
            "time": "June 12, 2015",
            "type": "article",
            "like": 98,
            "share": 6,
            "article": {
                "title": "The Fallout 4 Pip-Boy Edition Is Back In Stock Now",
                "subtitle": "Kotaku",
                "excerpt": "The Fallout 4 Pip-Boy edition is back in stock at Gamestop, for all 3 platforms. Additionally, Walmart also has it in stock for the PS4 and Xbox One as of this writing, as does Best Buy.",
                "media": {
                    "type": "image",
                    "preview": "/static/assets/images/etc/fallout.jpg"
                }
            },
            "comments": [
                {
                    "user": {
                        "name": "Alice Freeman",
                        "avatar": "/static/assets/images/avatars/alice.jpg"
                    },
                    "time": "June 10, 2015",
                    "message": "That’s a wonderful place. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et eleifend ligula. Fusce posuere in sapien ac facilisis. Etiam sit amet justo non felis ornare feugiat."
                }
            ]
        }];
    }
})();