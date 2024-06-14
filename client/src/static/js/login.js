function togglePassword(){
    if($("#password").attr("type") == "text") {
        $("#password").attr("type","password")
    } else {
        $("#password").attr("type","text")
    }
}

$('a').tooltip();
$('input').tooltip();
$('#form').submit(function () { showWait(); return true;});
