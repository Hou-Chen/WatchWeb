var act1 = 1;
var act3 = 1;
$('.ja2').attr("aftercontent", "+");
$(".before").click(function () {
	$(".before").toggleClass('after');
    if(act1 == 1) {
    	$('.nav').animate({left: '0'},600);                
    	act1 = 0;
    }
    else {
    	$('.nav').animate({left: '-100%'},1000);
        $('.ju2').slideUp(500);
        $('.ja2').attr("aftercontent", "+");
        act1 = 1;
        act3 = 1;
    }});
    $(".ja2").click(function() {
        $('.ju1').slideUp(500);
        if(act3 == 1) {
        	$('.ja2').attr("aftercontent", "-");
        	$('.ju2').slideDown(500);
            act3 = 0;
        }
        else {
        	$('.ja2').attr("aftercontent", "+");
        	$('.ju2').slideUp(500);
            act3 = 1;
        }});