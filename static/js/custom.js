
// NAV BAR

(function($) { "use strict";

	$(function() {
		var header = $(".start-style");
		$(window).scroll(function() {
			var scroll = $(window).scrollTop();

			if (scroll >= 10) {
				console.log("YESS")
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				console.log("NO")
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

	var btns = $(".nav-item .nav-link");

	for (var i = 0; i < btns.length; i++) {
		console.log("btn"+i+"=>");
		btns[i].addEventListener("click",function () {
			var current = document
				.getElementsByClassName("active");
			console.log("called!!",event.target);
			current[0].className = current[0]
				.className.replace(" active", "");

			this.className += " active";
		});
	}

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

$(document).ready(function() {
    $('#ag').click(function() {
    	console.log("HELLOWW")
        $(this).toggleClass("down");
    })
});

function ci_dropdown() {
	arrow = $("#ci").toggleClass("down")
}
function ag_dropdown() {
	arrow = $("#ag").toggleClass("down")
}

//Fade animation
  
  $(document).ready(function() {
	  
	  /* Every time the window is scrolled ... */
	  $(window).scroll( function(){
	  
		  /* Check the location of each desired element */
		  $('.hideme').each( function(i){
			  
			  var bottom_of_object = $(this).position().top + $(this).outerHeight();
			  var bottom_of_window = $(window).scrollTop() + $(window).height();
			  
			  /* If the object is completely visible in the window, fade it it */
			  if( bottom_of_window > bottom_of_object ){
				  
				  $(this).animate({'opacity':'1'},4000);
					  
			  }
			  
		  }); 
	  
	  });
	  
  });
  
  $(document).ready(function() {
	  
	  /* Every time the window is scrolled ... */
	  $(window).scroll( function(){
	  
		  /* Check the location of each desired element */
		  $('.animate-text').each( function(i){
			  
			  var bottom_of_object = $(this).position().top + $(this).outerHeight();
			  var bottom_of_window = $(window).scrollTop() + $(window).height();

			  console.log(bottom_of_object+', '+ bottom_of_window);
			  
			  /* If the object is completely visible in the window, fade it it */
			  if( bottom_of_window > bottom_of_object ){
				  
				  $(this).animate({letterSpacing: "0"}, 1500);
					  
			  }
			  
		  }); 
	  
	  });
	  
  });

  