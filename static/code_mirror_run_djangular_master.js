window.onload = function () {

    console.log('CODEMIRROR INITIALIZING... ');

    let txt_js_module = document.getElementById('id_module_js');
    let txt_js_controller = document.getElementById('id_controller_js');
    let txt_html_main = document.getElementById('id_view_html');
    let txt_style_main = document.getElementById('id_style_css');


    let txt_style_themestyle = document.getElementById('id_themestyle');

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

    let editor4 = CodeMirror.fromTextArea(txt_style_main, {
        lineNumbers: true,
        mode: "css",
        theme: "colorforth",
        indentUnit: 4,
        indentWithTabs: true
    });

    let editor5 = CodeMirror.fromTextArea(txt_style_themestyle, {
        lineNumbers: true,
        mode: "css",
        theme: "dracula",
        indentUnit: 4,
        indentWithTabs: true
    });

    // iPad
    if (window.innerWidth <= 1124) {
        editor1.setSize('640px', '480px');
        editor2.setSize('640px', '480px');
        editor3.setSize('640px', '480px');
        editor4.setSize('640px', '480px');
    } else {
        editor1.setSize('900px', '800px');
        editor2.setSize('900px', '1000px');
        editor3.setSize('900px', '1000px');
        editor4.setSize('900px', '1000px');
    }

};
