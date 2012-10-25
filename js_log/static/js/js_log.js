function logError(details) {
    $.ajax({
        type: 'POST',
        url: '/js_log/log_error/',
        data: {
            context: navigator.userAgent,
            details: details
        }
    });
}

window.onerror = function(message, file, line) {
    logError(file + ':' + line + '\n\n' + message);
};

