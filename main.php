<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>VK APP</title>
	<link rel="stylesheet" href="main.css">
	<script src="http://vkontakte.ru/js/api/openapi.js"></script>	
	<script src="bower_components/jquery/dist/jquery.js"></script>
	
	<script src="main.js"></script>
	
	
</head>
<body>
	<button class="login_button">LOGIN VK</button>
	<button class="post">Post</button>
	<button class="logout">Logout</button>
	<button class="getperm">GetPermissons</button>
	<button class="getph">GetPhotos</button>
	<input type="text" id="uaid" placeholder="user or group id">
	<h1>Status</h1>
	<div class="status1"></div>
	<h1>Permissions</h1>
	<div class="status2">not loaded</div>
	<h1>Albums</h1>
	<div class="status3" id="status3">not loaded</div>


</html>





