$(document).ready(function(){
  	p=/\d+/
  	var elem;
  	var src;
  	posts=$('.post')
	$('.image-link').magnificPopup({type:'image'})
	// $('img').click(function(){
	// 	src=$(event.target).attr('src');

	// });

  	// $('a').magnificPopup({type:'image'});
  	$('a').parent().magnificPopup({
  		  gallery: {
		    // options for gallery
		    enabled: true
		  },
	  delegate: 'a', // child items selector, by clicking on it popup will open
	  type: 'image'
	  // other options
	});
  	for (var i = 0; i<posts.length; i++){
  		// if ($(i).height>100){

  		// 	$(this).css('overflow', 'hidden')
  		// }

  		if (p.exec($($('.post')[i]).css('height'))>500){
  			elem=$($('.post')[i]);
			$($('.post')[i]).css('height', '200px');
			$($('.post')[i]).css('overflow', 'hidden');
			$($('.post')[i]).next().css('display', 'block');
			$($('.post')[i]).next().click(
				function(){

					if ($(event.target).prev().css('height')=='200px'){
						$(event.target).prev().css('height', 'auto');
						$(this).text('Скрыть');
					}
					else if (p.exec($(event.target).prev().css('height'))>500){
						$(event.target).prev().css('height', '200px');
						$(this).text('Показать полностью');
					};
			});
					
		}
  	}
 })