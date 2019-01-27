window.onload = function () {

    console.log('CODEMIRROR INITIALIZING... ');

    let txt_js_module = document.getElementById('id_js_module');
    let txt_js_controller = document.getElementById('id_js_controller');
    let txt_html_main = document.getElementById('id_html_main');

    let editor1 = CodeMirror.fromTextArea(txt_js_module, {
        lineNumbers: true,
        mode: "javascript",
        theme: "colorforth",
        indentUnit: 4,
        indentWithTabs: true
    });


    let editor2 = CodeMirror.fromTextArea(txt_js_controller, {
        lineNumbers: true,
        mode: "javascript",
        theme: "colorforth",
        indentUnit: 4,
        indentWithTabs: true
    });


    let editor3 = CodeMirror.fromTextArea(txt_html_main, {
        lineNumbers: true,
        mode: "htmlmixed",
        theme: "dracula",
        indentUnit: 4,
        indentWithTabs: true
    });



    // iPad
    if (window.innerWidth <= 1124) {
        editor1.setSize('640px', '480px');
        editor2.setSize('640px', '480px');
        editor3.setSize('640px', '480px');
    } else {
        editor1.setSize('1000px', '800px');
        editor2.setSize('1000px', '1400px');
        editor3.setSize('1000px', '1400px');
    }

};
