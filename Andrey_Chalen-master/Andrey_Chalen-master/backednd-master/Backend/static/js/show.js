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
     var a = Math.random()*10000000000
    $('#nb').click(function(){
        alert(+a.toFixed(0))
    })
    if($('#bd') == a){
        document.getElementById('button').readonly = false
    }else{
        document.getElementById('button').readonly = true
    }
});
