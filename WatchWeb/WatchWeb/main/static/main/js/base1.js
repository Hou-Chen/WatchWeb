var act1 = 1;
var act2 = 1;
var act3 = 1;
$('.ja1').attr("aftercontent", "+");
$('.ja2').attr("aftercontent", "+");
$(".before").click(function () {
	$(".before").toggleClass('after');
    if(act1 == 1) {
    	$('.nav').animate({left: '0'},600);                
    	act1 = 0;
    }
    else {
    	$('.nav').animate({left: '-100%'},1000);
        $('.ju1').slideUp(500);
        $('.ju2').slideUp(500);
        $('.ja1').attr("aftercontent", "+");
        $('.ja2').attr("aftercontent", "+");
        act1 = 1;
        act2 = 1;
        act3 = 1;
    }});
    $(".ja1").click(function() {
        $('.ju2').slideUp(500);
        if(act2 == 1) {
        	$('.ja1').attr("aftercontent", "-");
        	$('.ja2').attr("aftercontent", "+");
        	$('.ju1').slideDown(500);
            act3 = 1;
            act2 = 0;
        }
        else {
        	$('.ja1').attr("aftercontent", "+");
        	$('.ju1').slideUp(500);
            act2 = 1;
        }});
    $(".ja2").click(function() {
        $('.ju1').slideUp(500);
        if(act3 == 1) {
        	$('.ja2').attr("aftercontent", "-");
        	$('.ja1').attr("aftercontent", "+");
        	$('.ju2').slideDown(500);
            act2 = 1;
            act3 = 0;
        }
        else {
        	$('.ja2').attr("aftercontent", "+");
        	$('.ju2').slideUp(500);
            act3 = 1;
        }});