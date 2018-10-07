vm.socketMsgs = [];

vm.sendWSMessageWithAction = sendWSMessageWithAction;
vm.getWebSocketEditMessage = getWebSocketEditMessage;
vm.getWebSocketSaveMessage = getWebSocketSaveMessage;

function sendWSMessageWithAction(action) {
    const wsMsg = {
        action: action,
        info: {
            parentIndex: vm.loadedParentIndex,
            nodeIndex: vm.loadedIndex,
            mvcName: vm.masterName,
            title: vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].title
        }
    }
    EditorWebSocket.sendMsg(wsMsg);
}


/// - - - - - - <   DELEGATED FROM SERVICE   > - - - - - - - - 
EditorWebSocket.registerObserver_Save_Callback(getWebSocketSaveMessage);
EditorWebSocket.registerObserverCallback(getWebSocketEditMessage);
////getWebSocketEditMessage is called from: service.notifyObservers();
/// - - - - - - < / DELEGATED FROM SERVICE   > - - - - - - - - 


function getWebSocketEditMessage(parentIndex, nodeIndex) {
    $log.info(" 🍁 🍁 🍁 🍁 🍁 SERVICE DELEGATION WORKS ! ! !   ");
    $log.log(parentIndex, nodeIndex);
    vm.treeData[parentIndex].nodes[nodeIndex].openInOtherBrowser = true;
    
    
}


function getWebSocketSaveMessage(parentIndex, nodeIndex) {
    $log.info(" 🌐 🌐 🌐 🌐 🌐 SERVICE DELEGATION WORKS ! ! !   ");
    $log.log(parentIndex, nodeIndex);
    vm.treeData[parentIndex].nodes[nodeIndex].openInOtherBrowser = false;
    vm.treeData[parentIndex].nodes[nodeIndex].wasSavedInOtherBrowser = true;
    //var audio = new Audio('/static/gui_sfx/beep_surrender.wav');
    //audio.play();
}

vm.clearWebSocketConsole = clearWebSocketConsole;
vm.reloadWebSocketConsole = reloadWebSocketConsole;

function clearWebSocketConsole() {
	$('#renderedConsole').html('');
    EditorWebSocket.messagesTracked = [];
}


function reloadWebSocketConsole() {
	angular.forEach(EditorWebSocket.messagesTracked, function(val, key){
    	$('<p style="color:white">' + JSON.stringify(val) + '</p>').appendTo('#renderedConsole');
    });
	
}