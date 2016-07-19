function getXmlHttp(){
    var xmlhttp;
    try {
        xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
        try {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (E) {
            xmlhttp = false;
        }
    }
    if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
        xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
}


function get_log() {
    var req = getXmlHttp();
    req.open('GET', '/log');
    req.send();
    var statusElem = document.getElementById('log')
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            statusElem.innerHTML = req.statusText
            if(req.status == 200) {
                statusElem.innerHTML = JSON.parse(req.responseText).join('<br>');
                document.body.scrollTop = document.body.scrollHeight;
                if (req.responseText.indexOf("WINS") > -1) {
                    clearInterval(interval)
                }
            }
        }
    }

}

var interval = setInterval(get_log, 500);