window.onload = function () {

    console.log('CODEMIRROR INITIALIZING... ');

    let txt_html_main = document.getElementById('id_contents');


    let editor3 = CodeMirror.fromTextArea(txt_html_main, {
        lineNumbers: true,
        mode: "javascript",
        theme: "colorforth",
        indentUnit: 4,
        indentWithTabs: true
    });

    // iPad
    if (window.innerWidth <= 1124) {
        editor3.setSize('640px', '480px');
    } else {
        editor3.setSize('1000px', '1200px');
    }

};