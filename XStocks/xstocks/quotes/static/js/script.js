$(function () {
    const spinnerBox = $("#spinner-box");
    const dataBox = $("#data-box");

    $.ajax({
        type: 'GET',
        url: 'add_stock',
        success: function(response) {
            setTimeout(()=>{
                spinnerBox.addClass("not-visible")
                dataBox.removeClass("d-none")
            }, 500)
        },
        error: function(error) {
            console.log(error)
        }
    });
});
