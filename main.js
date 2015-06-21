$(document).ready(function(){
	$(".login_button").click(function(){VK.Auth.login(authInfo);});
	  VK.init({
	    apiId: 4964195

	  });
function authInfo(response) {
	  if (response.session) {
	  	$(".status1").html('<span id="statwrap"> User: '+response.session.mid + " session.</span>");
	  } else {
	    alert('not auth');
	  }
	}

// $.removeCookie("album_id", {path: "/"});
$.each($.cookie(), function(data){
	console.log(data);

});
var arrp =[];


var album_from_cookie = $("#uaid").val($.cookie('album_id'));
	if(album_from_cookie){
		$(".status3").html('');
			GetPhotos($.cookie('album_id'));
	}


VK.Auth.getLoginStatus(authInfo);
// VK.UI.button('login_button');
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
			GetPhotos(uaid);
			$(".status3").html('');
			
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
							
							var album_name = ($(event.target.parentNode.parentNode.childNodes[2]).html());
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
										$("<a class='back_main' href='#'>Back to albums</a>").insertBefore(".carousel");
										$('<a class="prev" href="#">Prev</a>').insertBefore(".carousel");
										$('<a class="next" href="#">Next</a>').insertBefore(".carousel");
										$("<span id='albumname'>"+album_name+"</span>").insertBefore($(".back_main"));
										$(".back_main").click(function(){
												location.reload(true);
										});


										$.each(obj, function(key, element){ 

											arrp.push(element.src_big);
											

											console.log(element.src_big);
											
										});
										listPhotos();
										
									}
									else{
										// alert("something wrong");
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
				$("<div><a href='"+arrp[i]+"' class='download_photo' target='_blank'> <img src='"+arrp[i]+"'></a></div>").appendTo($('.carousel'));
				// $('.download_photo').click(function(){return false;});
						// $('.download_photo').click(function(){return false;});						
				
			}
					
		// $(".carousel a").click(function(){alert($(this).attr("href"));});
		$('.carousel').slick({
			    autoplay: true,
			    accessibility: true,
			    dots: true,
			    // fade: true,
			    arrows: true,
			    prevArrow: $(".prev"),
			    nextArrow: $(".next"),
			    // centerMode: true
			    // // centerPadding: '10px',
			    // focusOnSelect: true,
			    // // adaptiveHeight: true
			    	 infinite: true,
					  slidesToShow: 3,
					  slidesToScroll: 3	
		// 		centerMode: true,

			  });
				
		}
			// Toggler on H1
		$("h1").click(function(){
			$(this).next().toggle("fast");
			
		});
		
				// $("#download_all").click(function(){

				// 		$(".download_photo").attr("download", "");
				// 		$(".download_photo > img").trigger("click");
				// 		$(".download_photo").removeAttr("download");
				// 		$('.download_photo').click(function(){return false;});

				// 		return false;
				// 		// 
				// 	});
				// 	
// $("#download_all").click(function(){
// 	$.fileDownload('https://pp.vk.me/c7011/v7011325/31e1/MnBJpHyFWfU.jpg');
//  });

		function Download(url) {
   				 document.getElementById('my_iframe').src = url;
		}
		// Download("http://www.vancouverobserver.com/sites/vancouverobserver.com/files/imagecache/vo_scale_w850/images/article/body/bigstock-No-Pets-Allowed-Sign-Showing-U-32860325.jpg");
		
});
