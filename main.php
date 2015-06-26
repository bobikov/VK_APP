<!DOCTYPE html>
<html lang="en">
<head>
	<meta Content-type: text/html; charset="UTF-8"  >
	<title>VK APP</title>
	<link rel="stylesheet" href="main.css">
	<link rel="stylesheet" href="bower_components/slick.js/slick/slick.css">
	<link rel="stylesheet" href="bower_components/slick.js/slick/slick-theme.css">

	<script src="bower_components/jquery/dist/jquery.js"></script>
	<script src="bower_components/oauth-js/dist/oauth.js"></script>
	<script src="bower_components/jquery-cookie/jquery.cookie.js"></script>
	<script src="bower_components/slick.js/slick/slick.js"></script>
	<script src="bower_components/autosize/dist/autosize.js"></script>
	<script src="//vk.com/js/api/openapi.js" type="text/javascript"></script>
	<script src="SDK.js"></script>

</head>
<body>
	<header>
		<div class="login_button">Login</div>
		<div class="post">Post</div>
		<div class="logout">Logout</div>
		<div class="getperm">GetPermissons</div>
		<div class="getph">GetPhotos</div>

	<input type="text" id="uaid" autocomplete=true placeholder="user or group id">
	</header>
	<main>
		<h1>Status</h1>
		<div class="status1"></div>
		<h1>Permissions</h1>
		<div class="status2"><!-- Put this div tag to the place, where the Comments block will be -->
			<!-- 	<div id="vk_comments"></div>
				<script type="text/javascript">
				VK.Widgets.Comments("vk_comments", {limit: 10, width: "665", attach: "*"});
				</script></div> -->
				<!-- <a href="fileList.php">Getdir</a> -->
			</div>
		<h1>Albums</h1>
		
		<div class="status3" id="status3">not loaded</div>
		<!-- <div id="download_all">Get album</div> -->
		<!-- <a id="downloadme"href="saveAs.php">Download</a> -->
		<!-- <a class="downloadme" type="application/octet-stream" href="http://www.vancouverobserver.com/sites/vancouverobserver.com/files/imagecache/vo_scale_w850/images/article/body/bigstock-No-Pets-Allowed-Sign-Showing-U-32860325.jpg" download>Download</a>
		<iframe id="my_iframe" style="display:none;"></iframe> -->
		<h1>Posts</h1>
		<div class="status4">
			<textarea name="" id="" cols="70" rows="4"></textarea>
			<div class="make_post">Post</div>
		</div>
	</main>	

			

				

	

	



</body>	
</html>





