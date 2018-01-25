(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            chats: {
                "name": "Alice Freeman",
                "avatar": "/static/assets/images/avatars/alice.jpg",
                "lastMessage": "Are you going to commit latest...",
                "status": "online",
                "dialog": [{
                    "who": "contact",
                    "message": "Quickly come to the meeting room 1B, we have a big server issue",
                    "time": "12 mins. ago"
                }, {
                    "who": "user",
                    "message": "I’m having breakfast right now, can’t you wait for 10 minutes?",
                    "time": "11 mins. ago"
                }, {
                    "who": "contact",


                    "message": "We are losing money! Quick!",
                    "time": "9 mins. ago"
                }, {
                    "who": "user",
                    "message": "It’s not my money, you know. I will eat my breakfast and then I will come to the meeting room.",
                    "time": "2 mins. ago"
                }, {
                    "who": "contact",
                    "message": "You are the worst!",
                    "time": "Just now"
                }, {
                    "who": "contact",
                    "message": "We are losing money! Quick!",
                    "time": "9 mins. ago"
                }, {
                    "who": "user",
                    "message": "It’s not my money, you know. I will eat my breakfast and then I will come to the meeting room.",
                    "time": "2 mins. ago"
                }, {
                    "who": "contact",
                    "message": "You are the worst!",
                    "time": "Just now"
                }, {
                    "who": "contact",
                    "message": "We are losing money! Quick!",
                    "time": "9 mins. ago"
                }, {
                    "who": "user",
                    "message": "It’s not my money, you know. I will eat my breakfast and then I will come to the meeting room.",
                    "time": "2 mins. ago"
                }, {
                    "who": "contact",
                    "message": "You are the worst!",
                    "time": "Just now"
                }, {
                    "who": "contact",
                    "message": "We are losing money! Quick!",
                    "time": "9 mins. ago"
                }, {
                    "who": "user",
                    "message": "It’s not my money, you know. I will eat my breakfast and then I will come to the meeting room.",
                    "time": "2 mins. ago"
                }, {
                    "who": "contact",
                    "message": "You are the worst!",
                    "time": "Just now"
                }]
            },
            contacts: [{
                "id": "5725a680b3249760ea21de52",
                "name": "Abbott",
                "avatar": "/static/assets/images/avatars/Abbott.jpg",
                "status": "online",
                "mood": "I never sign anything until I pretend to read it first..",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a680606588342058356d",
                "name": "Arnold",
                "avatar": "/static/assets/images/avatars/Arnold.jpg",
                "status": "do-not-disturb",
                "mood": "Looks like Andrew Jackson's been tossed to the back of the bus.",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a68009e20d0a9e9acf2a",
                "name": "Barrera",
                "avatar": "/static/assets/images/avatars/Barrera.jpg",
                "status": "do-not-disturb",
                "mood": "Love is going to bed early.Marriage is going to sleep early.",
                "unread": 4,
                "lastMessage": {
                    "who": "user",
                    "message": "pariatur commodo sunt nulla",
                    "time": "2016-03-18T12:30:18.931Z"
                }
            }, {
                "id": "5725a6809fdd915739187ed5",
                "name": "Blair",
                "avatar": "/static/assets/images/avatars/Blair.jpg",
                "status": "offline",
                "mood": "I would be unstoppable. If i could just get started.",
                "unread": 3,
                "lastMessage": {
                    "who": "user",
                    "message": "mollit excepteur sit",
                    "time": "2016-05-01T06:24:26.931Z"
                }
            }, {
                "id": "5725a68007920cf75051da64",
                "name": "Boyle",
                "avatar": "/static/assets/images/avatars/Boyle.jpg",
                "status": "offline",
                "mood": "'GOOD MORNING COFFEE'....Meet your maker!!!!",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a68031fdbb1db2c1af47",
                "name": "Christy",
                "avatar": "/static/assets/images/avatars/Christy.jpg",
                "status": "offline",
                "mood": "We always hold hands. If I let go, she shops.",
                "unread": null,
                "lastMessage": {
                    "who": "contact",
                    "message": "laboris ex",
                    "time": "2016-03-29T12:49:20.931Z"
                }
            }, {
                "id": "5725a680bc670af746c435e2",
                "name": "Copeland",
                "avatar": "/static/assets/images/avatars/Copeland.jpg",
                "status": "online",
                "mood": "I get enough exercise just pushing my luck.",
                "unread": null,
                "lastMessage": {
                    "who": "contact",
                    "message": "adipisicing sit",
                    "time": "2016-04-25T04:10:46.931Z"
                }
            }, {
                "id": "5725a680e7eb988a58ddf303",
                "name": "Estes",
                "avatar": "/static/assets/images/avatars/Estes.jpg",
                "status": "away",
                "mood": "What comes after the man bun hairstyle? The he-hive!",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a680dcb077889f758961",
                "name": "Harper",
                "avatar": "/static/assets/images/avatars/Harper.jpg",
                "status": "offline",
                "mood": "Always try to be modest and be proud of it!",
                "unread": null,
                "lastMessage": {
                    "who": "user",
                    "message": "non dolore Lorem",
                    "time": "2016-04-27T08:34:37.931Z"
                }
            }, {
                "id": "5725a6806acf030f9341e925",
                "name": "Helen",
                "avatar": "/static/assets/images/avatars/Helen.jpg",
                "status": "away",
                "mood": "Why are there stitch marks on zombies? Who's giving them medical attention?",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a680ae1ae9a3c960d487",
                "name": "Henderson",
                "avatar": "/static/assets/images/avatars/Henderson.jpg",
                "status": "offline",
                "mood": "I can't decide if people who wear pajamas in public have given up on life or are living it to the fullest.",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a680b8d240c011dd224b",
                "name": "Josefina",
                "avatar": "/static/assets/images/avatars/Josefina.jpg",
                "status": "online",
                "mood": "The fastest way to being happy is to make other people happy. You go first",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a68034cb3968e1f79eac",
                "name": "Katina",
                "avatar": "/static/assets/images/avatars/Katina.jpg",
                "status": "away",
                "mood": "If I was a rat,,, I wouldn't give anyone my ass.",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a6801146cce777df2a08",
                "name": "Lily",
                "avatar": "/static/assets/images/avatars/Lily.jpg",
                "status": "do-not-disturb",
                "mood": "A zip line but from the sofa to the fridge",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a6808a178bfd034d6ecf",
                "name": "Mai",
                "avatar": "/static/assets/images/avatars/Mai.jpg",
                "status": "away",
                "mood": "If a girl tells you she has a nipple ring, the only correct response is 'I don't believe you.'",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a680653c265f5c79b5a9",
                "name": "Nancy",
                "avatar": "/static/assets/images/avatars/Nancy.jpg",
                "status": "do-not-disturb",
                "mood": "Prison counts as a gated community, right?",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a680bbcec3cc32a8488a",
                "name": "Nora",
                "avatar": "/static/assets/images/avatars/Nora.jpg",
                "status": "do-not-disturb",
                "mood": "I never date left handed women. Righty tighty, lefty loosey.",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a6803d87f1b77e17b62b",
                "name": "Odessa",
                "avatar": "/static/assets/images/avatars/Odessa.jpg",
                "status": "away",
                "mood": "A day without sunshine is like, night.",
                "unread": null,
                "lastMessage": {
                    "who": "user",
                    "message": "aliqua officia esse commodo",
                    "time": "2016-04-28T16:11:54.931Z"
                }
            }, {
                "id": "5725a680e87cb319bd9bd673",
                "name": "Reyna",
                "avatar": "/static/assets/images/avatars/Reyna.jpg",
                "status": "offline",
                "mood": "I can't wait for summer in Canada...",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a6802d10e277a0f35775",
                "name": "Shauna",
                "avatar": "/static/assets/images/avatars/Shauna.jpg",
                "status": "online",
                "mood": "My take home pay doesn’t ven take me home.",
                "unread": null,
                "lastMessage": {
                    "who": "contact",
                    "message": "nulla sunt minim elit ullamco",
                    "time": "2016-05-01T09:17:47.931Z"
                }
            }, {
                "id": "5725a680aef1e5cf26dd3d1f",
                "name": "Shepard",
                "avatar": "/static/assets/images/avatars/Shepard.jpg",
                "status": "online",
                "mood": "I don't speak Spanish, but I'm pretty sure 'Dora' means 'annoying'",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a680cd7efa56a45aea5d",
                "name": "Tillman",
                "avatar": "/static/assets/images/avatars/Tillman.jpg",
                "status": "do-not-disturb",
                "mood": "",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a680fb65c91a82cb35e2",
                "name": "Trevino",
                "avatar": "/static/assets/images/avatars/Trevino.jpg",
                "status": "away",
                "mood": "Apparently, a rat and a plastic tube does not count as a DIY abortion kit.",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a68018c663044be49cbf",
                "name": "Tyson",
                "avatar": "/static/assets/images/avatars/Tyson.jpg",
                "status": "do-not-disturb",
                "mood": "I'm wondering why life keeps teaching me lessons I have no desire to learn...",
                "unread": null,
                "lastMessage": null
            }, {
                "id": "5725a6809413bf8a0a5272b1",
                "name": "Velazquez",
                "avatar": "/static/assets/images/avatars/Velazquez.jpg",
                "status": "online",
                "mood": "Modulation in all things.",
                "unread": null,
                "lastMessage": null
            }],
            getContactChat: getContactChat
        };


        /**
         * Get contact chat from the server
         *
         * @param contactId
         * @returns {*}
         */
        function getContactChat(contactId) {

            // Create a new deferred object
            var deferred = $q.defer();

            // If contact doesn't have lastMessage, create a new chat
            if (!service.contacts.getById(contactId).lastMessage) {
                service.chats[contactId] = [];

                deferred.resolve(service.chats[contactId]);
            }

            // If the chat exist in the service data, do not request
            if (service.chats[contactId]) {
                deferred.resolve(service.chats[contactId]);

                return deferred.promise;
            }


            deferred.resolve(service.chats[contactId]);


            return deferred.promise;
        }

        /**
         * Array prototype
         *
         * Get by id
         *
         * @param value
         * @returns {T}
         */
        Array.prototype.getById = function (value) {
            return this.filter(function (x) {
                return x.id === value;
            })[0];
        };


        return service;
    }
})();