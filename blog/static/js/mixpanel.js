$(document).ready(function() {
    $("#featuredBlog").click(function () {
        mixpanel.track("Blog Footer Clicked");
    });
     $("#tracktags").click(function () {
        mixpanel.track("Tags Clicked");
//         "tag name $(this)"
    });
});