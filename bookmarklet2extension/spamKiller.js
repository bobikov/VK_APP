// Bookmarklet for chat groups vk hiding any spam.
if (!document.getElementById('spam_killer')){
	// $(showCookie).click(function(){alert($.cookie('ids'));});
	var div1 = document.createElement('div'),
	logo = document.createElement('div'),
	bar = document.createElement('div'),
	logoText = document.createTextNode('spam killer'),
	delCookie = document.createElement('input'),
	showCookie = document.createElement('input'),
	banlist = document.createElement('div'),
	kill = document.createElement('input'),
	arr =[],
	barText = document.createTextNode('Banned: 0');

	showCookie.addEventListener('click', function(){
		alert(JSON.parse($.cookie('ids')));
	});
	delCookie.addEventListener('clic', function(){
		$.removeCookie('ids');
	});

	$.get(chrome.extension.getURL('banlist.json'), function(data){

		var parsed = $.parseJSON(data);
		userid = parsed[0].items;
		for (var i = 0; i < userid.length; i++){
			// banlist.value+=userid[i]+'\n';
			banlist.innerHTML+="<a href='https://vk.com"+ userid[i]+"'>"+userid[i]+"</a><br>";
		}
		
	});


	var userid = [];
	var cookieBigBans;
	var cookieBanIds = [];
	var cookieUnbanIds=[];

	var getCookieToArray = JSON.parse($.cookie('ids'));
	cookieBigBans = getCookieToArray;
	
	
							
	// banlist = document.createElement('textarea'),
	
	kill.type='button';
	kill.value='Hide';
	showCookie.type='button';
	showCookie.value='Show';
	delCookie.type='button';
	delCookie.value='Clean';
	
	div1.id='spam_killer';
	logo.id='logo';
	kill.id='kill';
	banlist.id='banlist';
	bar.id='bar';
	div1.className='spam_killer';
	logo.className='logo';
	banlist.className='banlist';
	bar.className='bar';
	kill.className='kill';
	showCookie.className='kill';
	delCookie.className='kill';
	banlist.setAttribute('placeholder','user id');
	document.body.insertBefore(div1, document.body.childNodes[0]);
	div1.appendChild(banlist);
	div1.appendChild(kill);
	div1.insertBefore(logo, banlist);
	div1.appendChild(delCookie);
	div1.appendChild(showCookie);
	logo.appendChild(logoText);
	div1.insertBefore(bar, banlist);
	bar.appendChild(barText);
	kill.addEventListener('click', hider, false);

	hider();

	function hider() {	
		// if (!banlist.value){
		// 	for (var i = 0; i < userid.length; i++){
		// 		// banlist.value+=userid[i]+'\n';
		// 		banlist.innerHTML+="<a href='https://vk.com"+ userid[i]+"'>"+userid[i]+"</a><br>";
		// 	}
		// }
		var select = document.querySelectorAll('.wall_post_text, .wall_reply_text, .bp_text');
		// for (var i = 0; i<select.length; i++){
		
		// }
		
		if (userid){

		setInterval(function(){

			if (location.href==='https://vk.com/chat_official'){
				$(banlist).show();
				// $(banlist).slideDown('slow');
				$(div1).css('z-index', 9999);
				// return false;
			}
			else { 
				$(banlist).hide();
				$(div1).css('z-index', 1);
				// $(banlist).slideUp('slow');
			}
				var tagA = document.getElementsByTagName('a');
				// var element2 = document.getElementsByTagName('div');
				var wallText = document.querySelectorAll('.wall_post_text, .wall_reply_text, .bp_text');
				// var userid = banlist.value.split(',');
				bar.innerHTML='Banned: ' + userid.length;
				cross( tagA, userid.concat(cookieBigBans), wallText);
				function cross(Arr1, Arr2, Arr3){
					for ( i=0; i < Arr1.length; i++ ){
						if ( Arr1[i].className == 'author' ){
							if (Arr1[i].parentNode.childNodes.length<2){
								var addToBan = document.createElement('input');
									addToBan.className='AddToBan';
									addToBan.type = 'button';
									addToBan.value="Add To Ban";
									addToBan.id = "Add";
									Arr1[i].parentNode.appendChild(addToBan);
									addToBan.addEventListener('click', banOne);

							}
							
							for( a=0; a<Arr2.length; a++){
								if (  Arr1[i].getAttribute('href') == Arr2[a] ){
									Arr1[i].parentNode.parentNode.parentNode.parentNode.parentNode.style.display='none';
								}	
							}
						}		
					}

					for ( i = 0; i < Arr3.length; i++ ){
						Arr3[i].innerHTML = Arr3[i].textContent
						.replace(/пздц|пиздец|пизда|хуй|блядь|нахуй|сука|пидорас|пидор|хуета|чмошник|б\*\*|^го|куй|куй|сладкие|анал|марамойка| девочки|хауню|хуйня|пздц|накуй|придурок|придурог|блядский|блядство|доебался|ебало|ебанул|ебанулся|[её]бнутый|[её]бнутая|[её]бнутые|хуесос|хуесосы|шлюха|пиндуй|нах|пиздуй|ахуеть|ахуенный|ахуенно|[её]пт|пизда|пиздит|охуел|ахуел|спиздил|спизди|ебаный|пиздюк|пиздище|обосанная|обоссанная|обосанный|обоссанный|хохол|хохлушка|пиздюк|пиздюки|жополиз|шлюхи|бляди|пиздабол|бля|пиздишь|ебан|ебло|(Пообщаюсь с девушкой!)|(одни бляди)|(Хули ты палишь)|хер|(хер в рот)|далбаеб|заебал|ебать|(нихуя себе)|замутим|нихуя|вирт|шмара|замутить|засади|засадите|хуясе|ипать|попи..дим|попиздим|попездим|ебануться|(гоу замутим вирт)|сцучка|гоу|бог|боже/ig, "&#127856;&#127799; The good word could be there, but there's only emptiness.&#127856;&#127799;");
					
						if( Arr3[i].textContent.match ( /tipos\.at\.ua|Профсоюзная|метро|(для мужиков)|krof\.3dn\.ru|(хочу секса)|(в финaнcoвoм плaне)|(uщy прияmнoгo мoлoдого челoвeкa)|порно|порнуха|(член у себя в попке)|(в эскорте для женщин)|(обмeн uнmимнымu фomкaми)|(для дружбы, секса и общения)|(вы не xoтелu бы пошaлumь cо мной?)|(Качественный утренний минетик)|opik\.id\.vg|(Ищу уверенного в себе мужчину, для серьёзных отношений или не совсем серьёзных)|(Хочу предложить тебе попользоваться друг другом)|(ищу партнёра для шалостей в скайпе)|(покажу член)|(Бyдy радa нoвoмy знакoмcтву c мужчuной для дpужбы, oбщенuя uлu чeго-то бoльшего)|(Покaжу кискy пo вебке)|(Покажу киску по вебке)|(Покажу по вебке)|(Покажу по скайпу)|(Кuдaю инmuм фоmки. вoзможна сmpечa)|(В поискe сuмпaтuчнoгo мoлoдoго парня для всmречи сегодня вечеpoм)|(Стройная, свободная, страстная девушка)|(ecmь многo uнтимных фоmoгрaфuй и видeo)|futr\.pp\.ua|(Прuглашу нa чaшечкy кoфe c послeдyющим прoдолжениeм)|(страстная, стройная брюнеточка)|fVuxFsYUyj\.vn\.tn|(сучку со со своего района и приписюнить)|(ищу парня для секса в свободное время)|(Путаны из твоего города.)|(Жду тебя у себя! Приятно проведем время!)|(Хочешь окунуться в чарующий мир жаркой эротики?)|(Мальчики кто хочет секса пишите)|(Встречусь с хорошим, страсть гарантирована)|(я oчень cильнo люблю соcaть)|(юблю бpаmь в рom y паpнeй посmаpшe)|(Милая, сексуальная, красивая и очень обаятельная)|(Жду в гости Котики мой номерочек)|(925-324-17-61)|(открылась новая группа по продаже кодов)|(кто желает встреч, пишите, оплата наличными)|(Телки скучают без мужиков)|www\.youwentianxia\.cn|(Чувственная, яркая и темпераментная девушка пригласит в гости)|(Прuглашу к ceбе сегодня вeчером молoдогo и веселого парня)|(Красивая девушка с горячим темпераментом)|(Привет, кто хочет секса)|(Строго Москва и 18+)|(B таких грyппaх куча мошенников, эти бaбы все ненастоящие!)|(я сейчас свободна и могу пригласить в гости)|(Одинокие женщины в поиске)|(заходите на бесплатные сайтики знакомств)|(Москва, оплата при личной встрече)|(девушка с горячими желаниями, желает тигра)|(кто хочет секс с горячей блонди)|(жду в гости, оплата при встрече)|(работа для парней 18)|(красивого, страстного мужчину)|(удивлю техниками минета и просто помогу получить незабываемое удовольствие)/ig)){
							// Arr3[i].parentNode.parentNode.parentNode.parentNode.style.display="none";
							// Arr3[i].parentNode.parentNode.parentNode.parentNode.parentNode.style.display='none';
							// alert(Arr3[i].className);
							Arr3[i].parentNode.parentNode.parentNode.parentNode.parentNode.style.display='none';

						}
					}
				}
			}, 10);
		}
	}

	function banOne(){
			getCookieToArray = JSON.parse($.cookie('ids'));
			cookieBigBans = getCookieToArray;
			$.removeCookie('ids');
			cookieBanIds.push(event.target.parentNode.childNodes[0].getAttribute('href'));
			// event.target.parentNode.parentNode.parentNode.parentNode.parentNode.style.display='none';
			var readyToCookieArray=cookieBanIds.concat(getCookieToArray);
			
			$.cookie('ids', JSON.stringify(readyToCookieArray), {expires: 1000});
	}

	function unbunOne(){
		alert(userid.indexOf('/id143794885'));
	}
}






