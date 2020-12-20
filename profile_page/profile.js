

$( document ).ready(function(){
  
   const urlParams = new URLSearchParams(window.location.search);
   const username = urlParams.get('username');
   
   
    $.ajax({
       
        url: 'https://em7ialrwbi.execute-api.ap-south-1.amazonaws.com/demo' + '?username='+ username,
        type: 'get',
        success: function(data){
            
            
            $('#Name').html(data["name"][0]);
            $('#Branch').html(data["branch"][0]);
            for(i = 0; i < data["name"].length;i++)
            {
               
                var codeblock = '<a href = "/scheme_page/scheme_name.htm?chit_key='+ data['chit_key'][i] + '>' +
                '<div class = "scheme_name" >' + 
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
             '</div>' + '</a>' ;
             
            
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

