
// Função para criar toast's
function generate_toast(type, title, message){
    let time = 3000;
    $(`
    <div class="position-fixed bottom-0 top-2 right-5 p-3" style="z-index: 5; right: 0; bottom: 0; top: 0">
        <div id="toast" class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-delay="${time}">
            <div class="toast-header">
                <strong class="me-auto text-${type}">${title}</strong>
                <small>Agora</small>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body text-${type} px-3">
                ${message}
            </div>
        </div>
    </div>
    `).appendTo("#montagem");

    $("#toast").toast('show');

    setTimeout(function(){
        $('#montagem').empty();
    },time+1);
}