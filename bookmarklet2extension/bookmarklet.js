// Bookmarklet for chat groups vk hiding any spam.
var div1 = document.createElement('div'),
	logo = document.createElement('div'),
	logoText = document.createTextNode('spam killer'),
	input1 = document.createElement('textarea'),
	button = document.createElement('input'),
	arr =[];
	button.setAttribute('type', 'button');
	button.setAttribute('value', 'Hide');

input1.setAttribute('placeholder', 'user id');
div1.style.cssText="background-color: #fff; z-index: 9999; width:180px; height:auto; position: fixed; right: 10px; border-radius: 3px";
logo.style.cssText="width:100%; background: #7F93A6; height: 20px; position: realitve; font-family: sans-serif; font-size: 18px; color: #fff; text-align: center; text-transform: uppercase";
button.style.cssText="display: block";
input1.style.cssText="width: 95%; outline:none; border-bottom-left-radius: 4px; border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; resize:vertical; height: auto";
div1.appendChild(input1);
div1.appendChild(button);
div1.insertBefore(logo, input1);
logo.appendChild(logoText);
document.body.insertBefore(div1, document.body.childNodes[0]);
button.addEventListener('click', hider, false);

function hider() {
setInterval(function(){
var element = document.getElementsByTagName('a');
// var userid = input1.value.split(',');
var userid = ['/id304808089', '/id312006414', '/id39820454', '/id312594203', '/id273573063', '/id62882989', '/id90831498', '/id136818024', '/id305164035', '/id76246987', '/id36933801', '/id100140735', '/id283493274', '/id125811388', '/omov73', '/id195552903', '/id171775759', '/id218901240','/id309868965', '/id308847968', '/fr0sti_manzzz', '/id305705976', '/id282031697', '/id311264806', '/id305029070', '/id82052637', '/id244046086', '/id309007690', '/m.kolesnikova2015', '/id305892010', '/id309986973', '/id64391322'];

cross( element, userid );
	function cross(Arr1, Arr2){
		for ( i=0; i<Arr1.length; i++ ){
			if ( Arr1[i].className == 'author' ){
			for( a=0; a<Arr2.length; a++) {
					if (  Arr1[i].getAttribute('href') == Arr2[a] ){
						Arr1[i].parentNode.parentNode.parentNode.parentNode.parentNode.style.display='none';
						// var alink = document.createElement('a');
						// alink.setAttribute('href', 'https://vk.com'+Arr1[a].getAttribute('href'));

						// alink.insertAfter(button);
						// alert(Arr1[i].getAttribute('href'));
					}	
				}
			}		
		}
	}

	}, 200);
}
void 0;
