window.addEventListener("load" , function (){
    console.log("load");
    $("#submit").on("click", function(e){ 
		console.log("submit");
        submit(e); 
    });
});

function submit(e){
    e.preventDefault();
    let form_elem   = "#form_area";
    let data    = new FormData( $(form_elem).get(0) );
    let url     = $(form_elem).prop("action");
    let method  = $(form_elem).prop("method");

    $.ajax({
        url: url,
        type: method,
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr ) { 

        if (data.error){
            console.log("ERROR");
        }
        else{
            $("#content_area").empty();
            $("#content_area").html(data.content);
            $("#form_area").val("");
        }

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    }); 
}
