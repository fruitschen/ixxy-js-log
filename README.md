ixxy-js-log
===========

A Django app that logs JavaScript errors

Usage
=====

pip install git+git://github.com/fruitschen/ixxy-js-log.git#egg=ixxy-js-log

Add 'js_log' into INSTALLED_APPS and syncdb or migrate, collectstatic. 

Modify urls.py and add: 

    url(r'^js_log/', include('js_log.urls')), 

Include the script in the pages you would like to log js errors. 

<script src="{{ settings.STATIC_URL }}js/js_log.js"></script>
