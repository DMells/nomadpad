$(document).ready(function() {
    var contentPlacement = $('#header').position().top + $('#header').height()
    $('#content').css('margin-top',contentPlacement);

// NOTE : adding ; at the end of the actual toggle line makes it
// not work! 
// Clicking toggle button will slide down menu bar
    $("#navbar").click( function(event){
        $("#mynavbar").toggleClass('responsive')
    });
// If user clicks anywhere that isnt the dropdown button or the actual 
// navbar, navbar will disappear
	$(document).click( function(event){
    	if($(event.target).is("#mynavbar, #navbar") === false) {
    		$("#mynavbar").removeClass('responsive')
    	}
    });
 
 });

