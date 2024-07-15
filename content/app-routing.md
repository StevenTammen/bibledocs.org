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

    // ms-settings:bluetooth
    if(app == "ms-settings") {
        var page = getQueryVariable("page");
        window.location.href = "ms-settings:" + page;
        window.close();
    }

    // logosres:esv;ref=BibleESV.Is45.22
    else if(app == "logos") {
        var resource = getQueryVariable("resource");
        var ref = getQueryVariable("ref");
        window.location.href = "logosres:" + resource + ";ref=" + ref;
        window.close();
    }

    // olivetree://bible/romans.8.28
    else if (app == "olivetree") {
        var ref = getQueryVariable("ref");
        window.location.href = "olivetree://bible/" + ref;
        window.close();
    }

    // pycharm://open?file=/absolute/path/to/file.md
    else if (app == "pycharm") {
        var file = getQueryVariable("file");
        window.location.href = "pycharm://open?file=" + file;
        window.close();
    }
</script>
