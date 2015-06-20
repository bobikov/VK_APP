<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>VK APP</title>
	<link rel="stylesheet" href="main.css">
	<link rel="stylesheet" href="bower_components/slick.js/slick/slick.css">
	<link rel="stylesheet" href="bower_components/slick.js/slick/slick-theme.css">
		
	
	
	
</head>
<body>
	<div id="login_button" onclick="VK.Auth.login(authInfo);"></div>
	<button class="post">Post</button>
	<button class="logout">Logout</button>
	<button class="getperm">GetPermissons</button>
	<button class="getph">GetPhotos</button>
	<input type="text" id="uaid" autocomplete=true placeholder="user or group id">
	<h1>Status</h1>
	<div class="status1"></div>
	<h1>Permissions</h1>
	<div class="status2">not loaded</div>
	<h1>Albums</h1>
	<div class="status3" id="status3">not loaded</div>


<script src="bower_components/jquery/dist/jquery.js"></script>
	<script src="bower_components/jquery-cookie/jquery.cookie.js"></script>
	<script src="http://vkontakte.ru/js/api/openapi.js"></script>
	<script src="bower_components/slick.js/slick/slick.js"></script>
	<script src="main.js"></script>
</body>	
</html>





