$(document).ready(function(){
    $("#h").click(function() {
        if ($("#f:first").is(":hidden")) {
            $("#f").show()("slow")
        }else {
            $("#f").toggle();
        }
    });
});