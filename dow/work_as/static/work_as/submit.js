function success( jQuery ) {
     $("#message").html('<p>Success!  <span class="glyphicon glyphicon-ok-circle" style="color:green"</span></p>')
     $("#message").hide(0).fadeIn("slow").delay(1000).fadeOut("slow");
}

function clearForm(jQuery){
    $(':input').not(':button, :submit, :reset, :hidden, :checkbox, :radio').val('');
    $(':checkbox, :radio').prop('checked', false);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function clickHandler(){
$('#submit-form').submit(function(e){
        e.preventDefault();
        console.log($("#id_storage").val().toString());
        //return;
        if($("#id_storage option:selected").length<1){
            return;
        }

        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.post($('#submit-form').prop('action'),{
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
            code:$("input[name=code]").val(),
            description:$("input[name=description]").val(),
            price:$("input[name=price]").val(),
            quantity:$("input[name=quantity]").val(),
            storage:eval($("#id_storage").val())
        })
        .done(function(data){
            console.log(data);
            success();
            clearForm();
            $(".text-danger").html("");
        })
        .fail(function(data){
            $("#form-content").html(data.responseText);
        })
    });
}

$(document).ready(clickHandler);