function logError(url, line, message) {
    $.ajax({
        type: 'POST',
        url: '/js_log/log_error/',
        data: {
            user_agent: navigator.userAgent,
            url: url,
            line: line,
            message: message
        }
    });
}

window.onerror = function(message, url, line) {
    if(url.indexOf(location.hostname)){
        /* 
         * Ignore an error if it's not our script.
         * We get error reports like failed to load facebook script, etc
         * And errors in third party script or even browser plugins
         */
        logError(url, line, message);
    }
};

