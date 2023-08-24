window.addEventListener("load" , function (){
    $("#submit").on("click", function(){ 
        submit(); 
    });
});

function submit(e){
    e.preventDefault();

    let form_elem   = "#form_area";
    let data    = new FormData( $(form_elem).get(0) );
    let url     = $(form_elem).prop("action");
    let method  = $(form_elem).prop("method");

    //送信するデータの確認
    console.log("hello")
    for (let v of data ){ console.log(v); }
    for (let v of data.entries() ){ console.log(v); }

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
            // console.log("Received content: ", data.content);
            // print("-----\n")
            // print(data.content)
            // print("-----\n")
            // $("#content_area").empty();
            // $("#content_area").html(data.content);
            // $("#textarea").val("");
        }

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    }); 
}
