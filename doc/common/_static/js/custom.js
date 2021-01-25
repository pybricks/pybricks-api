// https://stackoverflow.com/a/62742435/1976323
$(document).ready(function () {
    $('a[href^="http://"], a[href^="https://"]').not('a[class*=internal]').attr('target', '_blank');
});
