// NAV BAR
(function($) { "use strict";

	$(function() {
		var header = $(".start-style");
		$(window).scroll(function() {
			var scroll = $(window).scrollTop();

			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});

	//Animation

	$(document).ready(function() {
		$('body.hero-anime').removeClass('hero-anime');
	});

	//Menu On Hover

	$('body').on('mouseenter mouseleave','.nav-item',function(e){
			if ($(window).width() > 750) {
				var _d=$(e.target).closest('.nav-item');_d.addClass('show');
				setTimeout(function(){
				_d[_d.is(':hover')?'addClass':'removeClass']('show');
				},1);
			}
	});

	//Switch light/dark

	$("#switch").on('click', function () {
		if ($("body").hasClass("dark")) {
			$("body").removeClass("dark");
			$("#switch").removeClass("switched");
		}
		else {
			$("body").addClass("dark");
			$("#switch").addClass("switched");
		}
	});

  })(jQuery); 

// NAV BAR ENDED

//Timeline Started
$(document).ready(function() {

	// 	DELETE BUTTONS BUTTONS
	$(".close").click(function() {
		$(this)
			.parent()
			.hide();
	});

	// 	ON CLICKING EVENT
	$(".event").click(function() {
		$(".timeline")
			.find(".previous")
			.removeClass("previous");

		// IF ITS ALREADY ACTIVE, REMOVE IT
		if ($(this).hasClass("active")) {
			$(this).removeClass("active");
			$("#selected").text("");
			$(".timeline")
				.find(".previous")
				.removeClass("previous");

			$("#style").html(
				"<style>.timeline-wrapper::after {		width:calc(" +
					0 +
					"px);z-index:0;	}</style>"
			);
		} else {
			$(".timeline")
				.find(".active")
				.removeClass("active");
			$(this).addClass("active");

			$("#style").html(
				"<style>.timeline-wrapper::after {		width:calc(" +
					$(this).position().left +
					"px + 90px);z-index:0;	}</style>"
			);

			// MARK ALL PREVIOUS EVENTS
			$(this)
				.prevAll(".event")
				.addClass("previous");

			$("#selected").text(
				$(".timeline")
					.find(".active")
					.find("h2")
					.text()
			);
		}
	});
});

//timeline Ended