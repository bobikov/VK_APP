$(document).ready(function(){
	me='179349317';
	accToken="access_token=12190cdc5c7c2de92e1f892153e6ec3af558d98afc124f1a2534fae400ec277f8807264ff980f4c403de4"
	burl="https://api.vk.com/method/"
	$.ajax({
		url: burl+"users.get?user_ids=179349317&fields=city&v=5.34",
		type:"GET",
		dataType:"jsonp",
		success:function(msg){
			var resp = msg.response[0];
			$('.status1').html("<a href='https:/vk.com/id"+me+"''>"+resp['first_name']+' '+resp['last_name']+'</a> – Город: '+resp['city']['title']);
			console.log(msg.response[0]);
		}
	})
	$(".make_post").click(function(){
	 var message=$('.status4 textarea').val()
		$.ajax({
			url: "https://api.vk.com/method/wall.post?owner_id=179349317&message="+message+"&v=5.34&"+accToken,
			type: 'GET',
			dataType: 'jsonp',
			success:function(msg){
				console.log(msg.response);
			}
		})
	})
	
$('h1').click(function(){
	$(this).next().toggle(200);
})
});