$(document).ready(function () {
    $("a[delete-link='true']").on('click', function () {
        if (!confirm("Do you really want to delete")) {
            return false;
        }
    });
});