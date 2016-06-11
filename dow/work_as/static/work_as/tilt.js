function tilt( jQuery ) {
    var max=3;
    var min=-3;
    var list=document.getElementsByTagName("blockquote");
    for(var i=0;i<list.length;i++){
        var random=Math.floor(Math.random() * (max - min + 1)) + min;
        list[i].style.transform= "rotate("+random+"deg)";
    }
}

$( document ).ready( tilt );