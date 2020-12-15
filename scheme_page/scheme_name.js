var chit_key , amount , brnch_key;
$( document ).ready(function(){
   
    $.ajax({
        url : 'https://w298u9clrc.execute-api.ap-south-1.amazonaws.com/demo/details',
        type: 'get',
        success: function(data){
            chit_key = data['chit_key'];
            amount = data['amount'];
            brnch_key = data['brnch_key'];
            $('#scheme_name').html(data['scheme_name']);
            
            if(data["is_fixed_scheme"])
            {
                $('#Date_of_joining').html(data['date_of_joining']);
           
                document.getElementById("due_month").innerHTML += data['due_months'];
                document.getElementById("amount").innerHTML += data['amount']; 
            }
            



        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#content').html(errorMsg);
          }

     });
});
function pay(){
    $.ajax({
        url: 'https://z4j54197cb.execute-api.ap-south-1.amazonaws.com/demo/pay?chit_key=' + chit_key + '&amount=' + amount + '&brnch_key=' + brnch_key,
        type: 'get',
        success: function(data){
    
                alert("paid");
        },
        error: function (xhr, ajaxOptions, thrownError) {
            var errorMsg = 'Ajax request failed: ' + xhr;
            console.log(thrownError);
            $('#content').html(errorMsg);
          }

     });
}
