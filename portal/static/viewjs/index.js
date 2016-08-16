$(document).ready(function(){

	$('#slideMain').owlCarousel({
		singleItem:true,
		responsive:true,
		pavigation:true,
		navigation:true,
		navigationText:['anterior','siguiente'],
		autoPlay:true,
		lazyLoad:true
	});

	$('#slideClientes').owlCarousel({
		items:3,
		singleItem:false,
		responsive:true,
		pavigation:true,
		navigation:true,
		navigationText:['anterior','siguiente'],
		autoPlay:true,
		lazyLoad:true
	});
	
});