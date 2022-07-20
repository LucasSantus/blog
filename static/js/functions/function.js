// Função para criar toast's
function generate_toast(type, title, message){
    if(type == 'error') type = "danger"

    $('#assembly').empty();

    $(`
        <div class="toast fade show">
            <div role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header text-${type}">
                    <strong class="me-auto">
                        ${title}
                    </strong>
                    <small class="text-muted">Agora</small>
                </div>
                <div class="toast-body text-${type}">
                    ${message}
                </div>
            </div>
        </div>
    `).appendTo("#assembly");

    setTimeout(function () {
        $('#assembly').empty();
    }, 2000);
}