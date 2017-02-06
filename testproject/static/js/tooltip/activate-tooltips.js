require(["jquery", "bootstrap"], function($) {
    $(document).ready(function() {
        $('[data-toggle="tooltip"]').tooltip().click(function(event) {
            if ($(this).hasClass("js-simple-help")) {
                event.preventDefault();
            }
        });
    });
});