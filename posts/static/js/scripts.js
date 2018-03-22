// This function ensures that no matter the height of the header div
// the body div will always set to where the header div ends.
// Required because of the fixed position of the header so it sticks to
//the top of the page
// taken from https://stackoverflow.com/questions/7402635/css-make-content-appear-beneath-a-fixed-div-element
$(document).ready(function() {
    var contentPlacement = $('#header').position().top + $('#header').height();
    $('#content').css('margin-top',contentPlacement);
});

