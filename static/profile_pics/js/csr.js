import Cookies from 'js-cookie';

$.ajaxSetup({
    beforeSend: function (xhr, _settings) {
        if (!this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
        }
    }
});
