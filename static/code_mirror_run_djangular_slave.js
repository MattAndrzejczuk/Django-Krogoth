window.onload = function () {

    console.log('CODEMIRROR INITIALIZING... ');

    var txt_js_controller = document.getElementById('id_controller_js');
    var txt_html_main = document.getElementById('id_view_html');



    var editor3 = CodeMirror.fromTextArea(txt_html_main, {
        lineNumbers: true,
        mode: "javascript",
        theme: "colorforth",
        indentUnit: 4,
        indentWithTabs: true
    });


        var editor2 = CodeMirror.fromTextArea(txt_js_controller, {
        lineNumbers: true,
        mode: "javascript",
        theme: "colorforth",
        indentUnit: 4,
        indentWithTabs: true
    });

    // iPad
    if (window.innerWidth <= 1124) {
        editor3.setSize('640px', '480px');
        editor2.setSize('640px', '480px');
    } else {
        editor3.setSize('900px', '1000px');
        editor2.setSize('900px', '1000px');
    }

};


