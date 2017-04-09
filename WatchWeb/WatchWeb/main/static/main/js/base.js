var act1 = 1;
var act2 = 1;
var act3 = 1;
$(".before").click(function () {
	$(".before").toggleClass('after');
    if(act1 == 1) {
    	$('.nav').animate({left: '0'},600);                
    	act1 = 0;
    }
    else {
    	$('.nav').animate({left: '-100%'},1000);
        /*$('.ju1').slideUp(500);
        $('.ju2').slideUp(500);
        act1 = 1;
        act2 = 1;
        act3 = 1;*/
        act1 = 1;
    }});
    $(".ja1").click(function() {
    	$(".ja1").toggleClass('ja11');  
        /*$('.ju2').slideUp(500);*/
        if(act2 == 1) {
        	$('.ju1').slideDown(500);
            /*act3 = 1;*/
            act2 = 0;
        }
        else {
        	$('.ju1').slideUp(500);
            act2 = 1;
        }});
    $(".ja2").click(function() {
    	$(".ja2").toggleClass('ja22');
        /*$('.ju1').slideUp(500);*/
        if(act3 == 1) {
        	$('.ju2').slideDown(500);
            /*act2 = 1;*/
            act3 = 0;
        }
        else {
        	$('.ju2').slideUp(500);
            act3 = 1;
        }});