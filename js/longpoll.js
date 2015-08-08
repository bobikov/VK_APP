$(document).ready(function(){
	var acc = '00af0cff7458595045e1893775acf9b561dad00d6df9de580f9839e2722d5090e3fbf819a471461094666',
		key,
		server,
		ts;
	$.ajax({
		url: "https://api.vk.com/method/messages.getLongPollServer?access_token=00af0cff7458595045e1893775acf9b561dad00d6df9de580f9839e2722d5090e3fbf819a471461094666",
		type: "GET",
		dataType:'jsonp',
		success:function(msg){
				key = msg.response.key;
				server = msg.response.server;
				ts = msg.response.ts;
				setInterval(function(){
					$.ajax({
						url: "http://"+server+"?act=a_check&key="+key+"&ts="+ts+"&wait=25&mode=2",
						type: "GET",
						crossDomain: true,
						dataType: "jsonp",
						success: function(msg){
							console.log(msg['ts']);
						}
					})
				},2000)
		}
	});


});