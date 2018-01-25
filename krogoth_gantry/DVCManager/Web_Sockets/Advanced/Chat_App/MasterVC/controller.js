(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($websocket, $mdToast, $location, $timeout, ChatsService, $document, $mdMedia, $mdSidenav) {
        /* jshint validthis: true */
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        // Data
        vm.contacts = ChatsService.contacts;
        vm.chats = ChatsService.chats;
        vm.user = {}; //User.data;
        vm.leftSidenavView = false;
        vm.chat = undefined;

        // Methods
        vm.getChat = getChat;
        vm.toggleSidenav = toggleSidenav;
        vm.toggleLeftSidenavView = toggleLeftSidenavView;
        vm.reply = reply;
        vm.setUserStatus = setUserStatus;
        vm.clearMessages = clearMessages;

        //////////

        /**
         * Get Chat by Contact id
         * @param contactId
         */
        function getChat(contactId) {
            ChatsService.getContactChat(contactId).then(function (response) {
                vm.chatContactId = contactId;
                vm.chat = [{
                    "who": "contact",
                    "message": "Quickly come to the meeting room 1B, we have a big server issue",
                    "time": "2016-03-20T15:14:59.931Z"
                }, {
                    "who": "user",
                    "message": "I’m having breakfast right now, can’t you wait for 10 minutes?",
                    "time": "2016-04-20T15:14:59.931Z"
                }, {
                    "who": "contact",
                    "message": "We are losing money! Quick!",
                    "time": "2016-05-01T15:14:59.931Z"
                }, {
                    "who": "user",
                    "message": "It’s not my money, you know. I will eat my breakfast and then I will come to the meeting room.",
                    "time": "2016-05-01T15:20:59.931Z"
                }, {
                    "who": "contact",
                    "message": "You are the worst!",
                    "time": "2016-05-01T15:30:59.931Z"
                }, {
                    "who": "contact",
                    "message": "We are losing money! Quick!",
                    "time": "2016-05-01T16:30:59.931Z"
                }, {
                    "who": "user",
                    "message": "It’s not my money, you know. I will eat my breakfast and then I will come to the meeting room.",
                    "time": "2016-05-01T16:34:59.931Z"
                }, {
                    "who": "contact",
                    "message": "You are the worst!",
                    "time": "2016-05-01T16:39:59.931Z"
                }, {
                    "who": "contact",
                    "message": "We are losing money! Quick!",
                    "time": "2016-05-01T16:49:59.931Z"
                }, {
                    "who": "user",
                    "message": "It’s not my money, you know. I will eat my breakfast and then I will come to the meeting room.",
                    "time": "2016-05-02T14:49:59.931Z"
                }, {
                    "who": "contact",
                    "message": "You are the worst!",
                    "time": "2016-05-02T15:49:59.931Z"
                }, {
                    "who": "contact",
                    "message": "We are losing money! Quick!",
                    "time": "2016-05-02T16:30:59.931Z"
                }, {
                    "who": "user",
                    "message": "It’s not my money, you know. I will eat my breakfast and then I will come to the meeting room.",
                    "time": "2016-05-02T16:40:59.931Z"
                }, {
                    "who": "floop",
                    "message": "AHHHAHHAHAHHAHAHAHHHHHHHH!!!!!!!!!!!!.",
                    "time": "2016-05-02T16:40:59.931Z"
                }, {
                    "who": "contact",
                    "message": "You are the worst!",
                    "time": "2016-05-02T16:49:59.931Z"
                }];

                // Reset the reply textarea
                resetReplyTextarea();

                // Scroll to the last message
                scrollToBottomOfChat();

                if (!$mdMedia('gt-md')) {
                    $mdSidenav('left-sidenav').close();
                }

                // Reset Left Sidenav View
                vm.toggleLeftSidenavView(false);

            });
        }

        /**
         * Reply
         */
        function reply($event) {
            // If "shift + enter" pressed, grow the reply textarea
            if ($event && $event.keyCode === 13 && $event.shiftKey) {
                vm.textareaGrow = true;
                return;
            }

            // Prevent the reply() for key presses rather than the"enter" key.
            if ($event && $event.keyCode !== 13) {
                return;
            }

            // Check for empty messages
            if (vm.replyMessage === '') {
                resetReplyTextarea();
                return;
            }

            // Message
            var message = {
                who: 'user',
                message: vm.replyMessage,
                time: new Date().toISOString()
            };

            // Add the message to the chat
            vm.chat.push(message);

            // Update Contact's lastMessage
            vm.contacts.getById(vm.chatContactId).lastMessage = message;

            // Reset the reply textarea
            resetReplyTextarea();

            // Scroll to the new message
            scrollToBottomOfChat();

        }

        /**
         * Clear Chat Messages
         */
        function clearMessages() {
            vm.chats[vm.chatContactId] = vm.chat = [];
            vm.contacts.getById(vm.chatContactId).lastMessage = null;
        }

        /**
         * Reset reply textarea
         */
        function resetReplyTextarea() {
            vm.replyMessage = '';
            vm.textareaGrow = false;
        }

        /**
         * Scroll Chat Content to the bottom
         * @param speed
         */
        function scrollToBottomOfChat() {
            $timeout(function () {
                var chatContent = angular.element($document.find('#chat-content'));

                PerfectScrollbar.update(chatContent[0]);

                chatContent.animate({
                    scrollTop: chatContent[0].scrollHeight
                }, 400);
            }, 0);

        }

        /**
         * Set User Status
         */
        function setUserStatus(status) {
            vm.user.status = status;
        }

        /**
         * Toggle sidenav
         *
         * @param sidenavId
         */
        function toggleSidenav(sidenavId) {
            $mdSidenav(sidenavId).toggle();
        }

        /**
         * Toggle Left Sidenav View
         *
         * @param view id
         */
        function toggleLeftSidenavView(id) {
            vm.leftSidenavView = id;
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


    }
})();