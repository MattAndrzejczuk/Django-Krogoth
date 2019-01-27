window.onload = function () {

    console.log('CODEMIRROR INITIALIZING... ');

    let txt_html_main = document.getElementById('id_code');
    let txt_json = document.getElementById('id_custom_key_values');

    let editor3 = CodeMirror.fromTextArea(txt_html_main, {
        lineNumbers: true,
        mode: "javascript",
        theme: "colorforth",
        indentUnit: 4,
        indentWithTabs: true
    });

    let editor2 = CodeMirror.fromTextArea(txt_json, {
        lineNumbers: true,
        mode: "javascript",
        theme: "dracula",
        indentUnit: 4,
        indentWithTabs: true
    });
    
    // iPad
    if (window.innerWidth <= 1124) {
        editor3.setSize('640px', '480px');
        editor2.setSize('440px', '400px');
    } else {
        editor3.setSize('925px', '1000px');
        editor2.setSize('525px', '500px');
    }

};