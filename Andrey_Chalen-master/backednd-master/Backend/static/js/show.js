$(document).ready(function(){
    $("#h").click(function() {
        if ($("#f:first").is(":hidden")) {
            $("#f").show()("slow")
        }else {
            $("#f").toggle();
        }
    });
    $(".znak").click(function(){
        if ($('.h:first').is(':hidden')){
            $('.h').css({display: 'block'})
        }else{
            $('.h').css({display: 'none'})
        }
    })

});
