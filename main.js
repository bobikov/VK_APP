$(document).ready(function(){
	$(".login_button").click(function(){VK.Auth.login(authInfo);});
	  VK.init({
	    apiId: 4964195

	  });

function authInfo(response) {
	  if (response.session) {
	    $(".status1").text('user: '+response.session.mid + " session.");
	  } else {
	    alert('not auth');
	  }
	}
VK.Auth.getLoginStatus(authInfo);

// Click button events

	$(".getperm").click(function(){
			getAccPerm("179349317");
	});
	$(".post").click(function(){
			postToVk("Hello");

	});
	$(".getph").click(function(){
			var uaid = $("#uaid").val();
			// GetPhotos("-44426090");
		
			$(".status3").html('');
			GetPhotos(uaid);
	});

// Wall post
	function postToVk(msg){ 
			VK.Api.call( 'wall.post',
			{
				owner_id: '179349317',
				message: msg
			},
				function(response) {
				console.log(response);
				}
			);

	}
//Get Permissions
	function getAccPerm(id){
			VK.Api.call("account.getAppPermissions, ", {
				user_id: id
			},
				function(data){
				console.log(data.response);
				}
			);
	}
//Get Albums
	function GetPhotos(id){
		VK.Api.call("photos.getAlbums", {
			owner_id: id
		}, 
			function(data){
			if(data.response){
				var obj = data.response;

				$.each(obj, function(key, element){
					$("<table style='float:left' border='1' cellpadding='6' cellspacing='0'><tr><td>Title</td><td>"+element.title+"<tr><td>AlbumID</td><td><a href='#'>" + element.aid + "</a></td></tr><tr><td>Size</td><td>" + element.size + "</td></tr></table>").appendTo($(".status3"));
				});


				// Get list of photos
					var owner = $("#uaid").val();
					$("a").click(function(){
							$(".status3").html('');
								var album = $(this).html();

								VK.Api.call("photos.get", {
								owner_id: owner, 
								album_id: album
								}, 

								function(data){
									if (data.response){
										var obj = data.response;
										$.each(obj, function(key, element){
										
											$("<table border='0' cellpadding='5' cellspacing='0'><tr><td><a href='"+element.src_big+"'>"+element.src_big+"</a></td></tr></table>").appendTo($(".status3"));
										// console.log(element.src_big);
										});
										
									}
									else{
										alert("something wrong");
										console.log(data.response);

									}
					});
					});

					

					console.log(data.response);
			}
			else {
					console.log(data);
			}
			});
	}

// Toggler on H1
		$("h1").click(function(){
			$(this).next().toggle("fast");
			
		});
});