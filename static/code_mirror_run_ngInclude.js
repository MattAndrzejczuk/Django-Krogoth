window.onload = function () {

    console.log('CODEMIRROR INITIALIZING... ');

    var txt_html_main = document.getElementById('id_contents');


    var editor3 = CodeMirror.fromTextArea(txt_html_main, {
        lineNumbers: true,
        mode: "htmlmixed",
        theme: "dracula",
        indentUnit: 4,
        indentWithTabs: true
    });

    // iPad
    if (window.innerWidth <= 1124) {
        editor3.setSize('640px', '480px');
    } else {
        editor3.setSize('1000px', '1400px');
    }

};