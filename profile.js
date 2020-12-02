

$( document ).ready(function(){
    
    $.ajax({
        url: 'https://em7ialrwbi.execute-api.ap-south-1.amazonaws.com/demo',
        type: 'get',
        success: function(data){
            
            
            $('#Name').html(data["name"]);
            $('#Branch').html(data["branch"]);
            $('#scheme').html(data["scheme"]);
            $('#scheme_amount').html(data["amount"]);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#content').html(errorMsg);
          }
    });
});

