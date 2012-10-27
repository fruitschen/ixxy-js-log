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
    logError(url, line, message);
};

