function search(jQuery) {
  $("#q").autocomplete({
    source: "search",
    minLength: 2,
    delay:500,
    select: function(event,ui){
        window.location.href = "/details/part/"+ui.item.value;
        }
    })
}


$( document ).ready(search);