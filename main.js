$(document).ready(function(){
	$(".login_button").click(function(){VK.Auth.login(authInfo);});
	  VK.init({
	    apiId: 4964195

	  });

// $.removeCookie("album_id", {path: "/"});
// alert($.cookie('album_id'));
var arrp =[];
var album_from_cookie = $("#uaid").val($.cookie('album_id'));
	if(album_from_cookie){
		$(".status3").html('');
			GetPhotos($.cookie('album_id'));
	}
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
// Cookies 
// function getCookie(name) {
//   var matches = document.cookie.match(new RegExp(
//     "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
//   ));
//   return matches ? decodeURIComponent(matches[1]) : undefined;
// }



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
		// var date = new Date(new Date().getTime()+60*60*60*1000);
		// document.cookie = "album_id="+ id +"; path=/; expires="+date.toUTCString();
		$.cookie('album_id', id, {expires: 7, path: "/"} );
		VK.Api.call("photos.getAlbums", {
			owner_id: id

		}, 
			function(data){
			if(data.response){
				var obj = data.response;
				$("<table id='albums' border='0'  cellpadding='6' cellspacing='0'><tr><td>AlbumID</td><td>Size</td><td>Tite</td></table>").appendTo($(".status3"));
				$.each(obj, function(key, element){
					$("<tr><td><a href='#'>" + element.aid + "</a></td><td>" + element.size + "</td><td>"+element.title+"</td></tr>").appendTo($("#albums"));
				});


				// Get list of photos
					var owner = $("#uaid").val();
					$("a").click(function(){
							

							var album = $(this).html();

								VK.Api.call("photos.get", {
								owner_id: owner, 
								album_id: album
								}, 

								function(data){
									if (data.response){
										var obj = data.response;
										
										$(".status3").html('');
										$(".status3").css("column-count", "1");
										$(".status3").html('<div class="carousel"></div>');
										$('<a class="prev" href="#">Prev</a>').insertBefore(".carousel");
										$('<a class="next" href="#">Next</a>').insertBefore(".carousel");
										


										$.each(obj, function(key, element){ 

											arrp.push(element.src_big);
											

											console.log(element.src_big);
											
										});
										listPhotos();
										
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




		function listPhotos () {
			for (var i =0; i < arrp.length; i++){
		// $(".jcarousel ul").html("<li><img src='"+arrp[i]+"'></li>");
					$("<div><img src='"+arrp[i]+"'></div>").appendTo($('.carousel'));
				
			}

			// $(".carousel img").click(function(){alert($(this).attr("src"));});

			 $('.carousel').slick({
			    autoplay: false,
			    // arrows: true,
			    prevArrow: $(".prev"),
			    nextArrow: $(".next"),
			    // centerMode: true
			    centerPadding: '10px'
			    // focusOnSelect: true
			    // adaptiveHeight: true
			  });
				
		}
			// Toggler on H1
		$("h1").click(function(){
			$(this).next().toggle("fast");
			
		});
});