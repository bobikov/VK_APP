$(document).ready(function(){
	OAuth.initialize('9KeYudtaIrqT2OfhiBaWG-xGERo');
	

		OAuth.redirect('vk', "https://localhost/");
		OAuth.callback('vk').done(function(vk) {

			console.log(vk.access_token);
			}).fail(function(err) {
			  //todo when the OAuth flow failed
			});

});   
