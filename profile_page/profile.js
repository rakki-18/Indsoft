
/* displays the details of the all the schemes that are registered with the particular username by sending ajax request to the API */
$( document ).ready(function(){
  
   const urlParams = new URLSearchParams(window.location.search);
   const username = urlParams.get('username');

   var codeblock1 = '<a href= "/password_change/change_password.htm?username=' + username+'">Change Password</a>';
   document.getElementById("change_password").innerHTML += codeblock1;
   
   
   
    $.ajax({
       
        url: 'https://iyp7kair9b.execute-api.ap-south-1.amazonaws.com/demo/profile' + '?username='+ username,
        type: 'get',
        success: function(data){
            
            
            $('#Name').html(data["name"][0]);
            $('#Branch').html(data["branch"][0]);
            for(i = 0; i < data["name"].length;i++)
            {
               
                var codeblock = '<a href = "/scheme_page/scheme_name.htm?chit_key='+ data['chit_key'][i] + '">' +
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

