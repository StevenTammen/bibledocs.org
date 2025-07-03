+++
title = "App Routing"
+++

<script>
    // https://css-tricks.com/snippets/javascript/get-url-variables/
    function getQueryVariable(variable)
    {
        var query = window.location.search.substring(1);
        var vars = query.split("&");
        for (var i=0;i<vars.length;i++) {
                var pair = vars[i].split("=");
                if(pair[0] == variable){return pair[1];}
        }
        return(false);
    }

    var app = getQueryVariable("app");

    // logosres:esv;ref=BibleESV.Is45.22
    if(app == "logos") {
        var resource = getQueryVariable("resource");
        var ref = getQueryVariable("ref");
        window.location.href = "logosres:" + resource + ";ref=" + ref;
        window.close();
    }

    // olivetree://bible/romans.8.28
    else if (app == "olive-tree") {
        var ref = getQueryVariable("ref");
        window.location.href = "olivetree://bible/" + ref;
        window.close();
    }

    // http://localhost:63342/api/file/relative-path-to-file-in-currently-open-project/myfile.md
    else if (app == "py-charm") {
        var relativeFilePath = getQueryVariable("relative-file-path");
        pyCharmApiPath = "http://localhost:63342/api/file/" + relativeFilePath;
        req = new XMLHttpRequest();
        req.onreadystatechange = function () {
            if (req.readyState == XMLHttpRequest.DONE) {
                window.close();
            }
        }
        req.open("GET", pyCharmApiPath);
        req.send();
    }



</script>
