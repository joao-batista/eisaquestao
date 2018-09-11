function responder(id_pergunta) {
    var id = $("input[name=" + id_pergunta + "]:checked").val()
    var url = formatar_url('responder_ajax/')

    if(id){
        var retorno = post(url, id, '')
        retorno.done(function(data) {
            feedback(id_pergunta, data);
        })
    } else {
        $('#modal_selecionar').modal('show')
    }

}

function publicar(id) {
    var url = formatar_url('publicar_ajax/')
	var texto = $('#textarea_comentario_' + id).val()

    var retorno = post(url, id, texto)
    retorno.done(function(data) {
        $('#texto_comentario_' + id).html(data.resposta)
        editar(id);
    })
}

function formatar_url(url) {
    if (window.location.href.includes("filtrar")) 
        return '../' + url
    return url
}

function post(url, id, texto) {
    return $.ajax({
                headers     : { "X-CSRFToken": csrftoken },
                type        : 'POST', 
                url         : url,
                data        : { 'id': id, 'texto' : texto },
                dataType    : 'json'
            });
}

function feedback(id, results) {
    if (results.resposta) {
        $('#is_correta_'   + id).show();
        $('#is_incorreta_' + id).hide();
    }
    else {
        $('#is_correta_'   + id).hide();
        $('#is_incorreta_' + id).show();
    }
}

function editar(id) {
    $('#comentario_editar_'   + id).toggle();
    $('#comentario_publicar_' + id).toggle();
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$(document).ready(function() {
    $(".textarea-customizado").each(function(){
        $(this).css('height','auto');
        $(this).height(this.scrollHeight);
    });
});