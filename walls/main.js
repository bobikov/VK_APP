$(document).ready(function(){
  	p=/\d+/
  	var elem;
  	var src;
  	posts=$('.post')
	// $('.image-link').magnificPopup({type:'image'})
	// $('img').click(function(){
	// 	src=$(event.target).attr('src');

	// });
  // $('.menu a').click(function(){
  //   // location($(this).attr("href"))
  //   location('walls/'+$(this).attr('href'))
  //   // alert($(this).attr('gogle.com'))

  // })
  	// $('a').magnificPopup({type:'image'});
  	$('a').parent().magnificPopup({
  		  gallery: {
		    // options for gallery
		    enabled: true
		  },
	  delegate: '.photos', // child items selector, by clicking on it popup will open
	  type: 'image'
	  // other options
	});
  	for (var i = 0; i<posts.length; i++){
  		// if ($(i).height>100){

  		// 	$(this).css('overflow', 'hidden')
  		// }
  		// console.log(i)
  		if($($('.post')[i]).next().next().children().children().length==1){
  			$($('.post')[i]).next().next().children().children().css('max-width', '100%')
  			$($('.post')[i]).next().next().children().children().css('max-height', '100%')
  		}
  		else if($($('.post')[i]).next().next().children().children().length==3){
  			$($('.post')[i]).next().next().children().children().css('max-width', '40%')
  			$($('.post')[i]).next().next().children().children().css('max-height', '40%')
  		}
  		else if($($('.post')[i]).next().next().children().children().length==2){
  			$($('.post')[i]).next().next().children().children().css('max-width', '60%')
  			$($('.post')[i]).next().next().children().children().css('max-height', '60%')
  		}
  		else if($($('.post')[i]).next().next().children().children().length==6){
  			$($('.post')[i]).next().next().children().children().css('max-width', '40%')
  			$($('.post')[i]).next().next().children().children().css('max-height', '40%')
  		}
  		else if($($('.post')[i]).next().next().children().children().length==8){
  			$($('.post')[i]).next().next().children().children().css('max-width', '30%')
  			$($('.post')[i]).next().next().children().children().css('max-height', '30%')
  		}
  		else if($($('.post')[i]).next().next().children().children().length==9){
  			$($('.post')[i]).next().next().children().children().css('max-width', '30%')
  			$($('.post')[i]).next().next().children().children().css('max-height', '30%')
  		}
      else if($($('.post')[i]).next().next().children().children().length==10){
        $($('.post')[i]).next().next().children().children().css('max-width', '25%')
        $($('.post')[i]).next().next().children().children().css('max-height', '25%')
      }
       else if($($('.post')[i]).next().next().children().children().length==7){
        $($('.post')[i]).next().next().children().children().css('max-width', '35%')
        $($('.post')[i]).next().next().children().children().css('max-height', '35%')
      }
      else if($($('.post')[i]).next().next().children().children().length==5){
        $($('.post')[i]).next().next().children().children().css('max-width', '40%')
        $($('.post')[i]).next().next().children().children().css('max-height', '40%')
      }
  		
  		


  		if (p.exec($($('.post')[i]).css('height'))>400){
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
					else if (p.exec($(event.target).prev().css('height'))>400){
						$(event.target).prev().css('height', '200px');
						$(this).text('Показать полностью');
					};
			});

					
		}

  	}
 })