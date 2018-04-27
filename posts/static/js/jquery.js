$(document).ready(function() {
    var contentPlacement = $('#header').position().top + $('#header').height()
    $('#content').css('margin-top',contentPlacement);


// Clicking toggle button will slide down menu bar
    $("#navbartoggler").click( function(event){
        $("#navbaractual").slideToggle()
    });

// // If user clicks anywhere that isnt the dropdown button or the actual 
// // navbar, navbar will disappear
     $(document).click( function(event)
        {
         if($("#navbaractual").is(':visible'))
            {
            if($(event.target).is("#navbaractual,  #navbartoggler") === false) 
                {
                $("#navbaractual").slideToggle()
                }
            }
        });
    





    });

