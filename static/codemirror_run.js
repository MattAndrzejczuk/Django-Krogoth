window.onload = function () {

    console.log('CODEMIRROR INITIALIZING... ');

    var txt_js_module = document.getElementById('id_js_module');

    if (txt_js_module) {
        var editor1 = CodeMirror.fromTextArea(txt_js_module, {
            lineNumbers: true,
            mode: "javascript",
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        });
        editor1.setSize('1000px', '600px');
        console.log('EDITOR 1 INITIALIZED... javascript');
        console.log(editor1);
    }


    var txt_js_controller = document.getElementById('id_js_controller');

    if (txt_js_controller) {

        var editor2 = CodeMirror.fromTextArea(txt_js_controller, {
            lineNumbers: true,
            mode: "javascript",
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        });
        editor2.setSize('1000px', '600px');
        console.log('EDITOR 2 INITIALIZED... javascript');
        console.log(editor2);
    }


    var txt_html_main = document.getElementById('id_html_main');
    if (txt_html_main) {
        var editor3 = CodeMirror.fromTextArea(txt_html_main, {
            lineNumbers: true,
            mode: "htmlmixed",
            theme: "dracula",
            indentUnit: 4,
            indentWithTabs: true
        });
        editor3.setSize('1000px', '600px');
        console.log('EDITOR 3 INITIALIZED... htmlmixed');
        console.log(editor3);
    }


    var txt_html_code = document.getElementById('id_html_code');
    if (txt_html_code) {

        var editor3 = CodeMirror.fromTextArea(txt_html_code, {
            lineNumbers: true,
            mode: "htmlmixed",
            theme: "dracula",
            indentUnit: 4,
            indentWithTabs: true
        });
        editor3.setSize('1000px', '1400px');

        // var editor4 = CodeMirror.fromTextArea(txt_html_code, {
        //     lineNumbers: true,
        //     mode: 'xml',
        //     htmlMode: true,
        //     theme: "dracula",
        //     indentUnit: 4,
        //     indentWithTabs: true,
        //     matchClosing: true
        // });
        // console.log('EDITOR 4 INITIALIZED... htmlmixed');
        // console.log(editor4);
    }


};








