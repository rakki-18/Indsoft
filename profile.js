

$( document ).ready(function(){
    
    $.ajax({
        url: 'https://em7ialrwbi.execute-api.ap-south-1.amazonaws.com/demo',
        type: 'get',
        success: function(data){
            
            
            $('#Name').html(data["name"][0]);
            $('#Branch').html(data["branch"][0]);
            for(i = 0; i < data["name"].length;i++)
            {
                var codeblock = '<div class = "scheme_name" >' + 
                '<span class="left">' + 
                  data["scheme"][i] +
                '</span>' +
                '<br><br>' +
                 '<span class="left">' + 
                   data["amount"][i] +
                 '</span>' + 
                '<br><br>' + 
                '<span class="left">' + 
                data["date"][i] +
              '</span>' + 
                '<br><br>' +
             '</div>' ;
             
             document.getElementById("display_schemes").innerHTML += codeblock;
            }
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#content').html(errorMsg);
          }
    });
});

