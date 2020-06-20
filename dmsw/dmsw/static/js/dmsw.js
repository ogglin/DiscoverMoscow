counter = 1
$(document).ready(function () {
    $('#owl-carousel-1').owlCarousel({
        items: 1,
        loop: true,
        nav: true,
        navText: [
          '<i class="fas fa-arrow-left" aria-hidden="true"></i>',
          '<i class="fas fa-arrow-right" aria-hidden="true"></i>'
        ],
        // Автоматическое проигрывание
        autoplay: true,
        autoplayTimeout: 5500,
        autoplaySpeed: 1000,
        slideTransition: 'linear',
        autoplayHoverPause: true
    });
    $('.owl-dot').click(function () {
        clear_interval()
    })
    $('.owl-next').click(function () {
        clear_interval()
    })
});

function clear_interval() {
    clearInterval(switchInterval_right);
    switchInterval_right = setInterval(nextSlideRight, slideInterval_right);
    if (counter < 2) {
        counter++
    } else {
        counter--
        // nextSlideRight()
    }
    console.log(counter)
}

//Slider aditional
var slideNow_right = 1;
var slideCount_right = $('#slidewrapper-right').children().length;
var slideInterval_right = 11000;
var navBtnId_right = 0;
var translateWidth_right = 0;
var switchInterval_right = setInterval(nextSlideRight, slideInterval_right);
slideNavs_right = $('.slide-nav-btn-right')
setActive();
$(document).ready(function () {
    setActive();
    $('#viewport-right').hover(function () {
        clearInterval(switchInterval_right);
    }, function () {
        switchInterval_right = setInterval(nextSlideRight, slideInterval_right);
    });

    $('#next-btn-right').click(function () {
        nextSlideRight();
    });

    $('#prev-btn-right').click(function () {
        prevSlideRight();
    });

    $('.slide-nav-btn-right').click(function () {
        $('.slide-nav-btn-right').removeClass('active')
        $(this).addClass('active')
        navBtnId_right = $(this).index();

        if (navBtnId_right + 1 != slideNow_right) {
            translateWidth_right = -$('#viewport-right').width() * (navBtnId_right);
            $('#slidewrapper-right').css({
                'transform': 'translate(' + translateWidth_right + 'px, 0)',
                '-webkit-transform': 'translate(' + translateWidth_right + 'px, 0)',
                '-ms-transform': 'translate(' + translateWidth_right + 'px, 0)',
            });
            slideNow_right = navBtnId_right + 1;
        }
    });
});

function nextSlideRight() {
    if (slideNow_right == slideCount_right || slideNow_right <= 0 || slideNow_right > slideCount_right) {
        $('#slidewrapper-right').css('transform', 'translate(0, 0)');
        slideNow_right = 1;
    } else {
        translateWidth_right = -$('#viewport-right').width() * (slideNow_right);
        $('#slidewrapper-right').css({
            'transform': 'translate(' + translateWidth_right + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth_right + 'px, 0)',
            '-ms-transform': 'translate(' + translateWidth_right + 'px, 0)',
        });
        slideNow_right++;
    }
    setActive()
}

function prevSlideRight() {
    if (slideNow_right == 1 || slideNow_right <= 0 || slideNow_right > slideCount_right) {
        translateWidth_right = -$('#viewport-right').width() * (slideCount_right - 1);
        $('#slidewrapper-right').css({
            'transform': 'translate(' + translateWidth_right + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth_right + 'px, 0)',
            '-ms-transform': 'translate(' + translateWidth_right + 'px, 0)',
        });
        slideNow_right = slideCount_right;
    } else {
        translateWidth_right = -$('#viewport-right').width() * (slideNow_right - 2);
        $('#slidewrapper-right').css({
            'transform': 'translate(' + translateWidth_right + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth_right + 'px, 0)',
            '-ms-transform': 'translate(' + translateWidth_right + 'px, 0)',
        });
        slideNow_right--;
    }
    setActive()
}

function setActive() {
    $('.slide-nav-btn-right').removeClass('active')
    slideNavs_right.each(function (index) {
        if (slideNow_right == index + 1) {
            $(this).addClass('active')
        }
    })
}


// Burger menu
var docHeight = $(document).height();
var footerHeight = $('footer').height();
burgerHeight = docHeight - footerHeight - 130
// $('header .navbar-tags').css('height',burgerHeight)
$('#btn_burger').click(function () {
    $('.navbar-tags').addClass('active')
    $('#btn_burger').addClass('hide')
    $('#btn_burger_close').removeClass('hide')
    $('.main_menu').addClass('hide')
});
$('#btn_burger_close').click(function () {
    $('.navbar-tags').removeClass('active')
    $('#btn_burger_close').addClass('hide')
    $('#btn_burger').removeClass('hide')
    $('.main_menu').removeClass('hide')
});


// Main menu open/close
function main_menu_collapse() {
    menu_width = $('header .navbar').width()
    menu_items = $('.main_menu li')
    menu_width_nav = 0
    menu_items.each(function () {
        menu_width_nav += $(this).width() + 40
    })
    if (menu_width < menu_width_nav) {
        $('header .main_menu').addClass('collapse')
    }
    if (menu_width >= menu_width_nav) {
        $('header .main_menu').removeClass('collapse')
    }
}

$(window).resize(function () {
    main_menu_collapse();
    //nextSlideRight();
})
$('header #more').click(function () {
    $('header .main_menu').toggleClass('open')
})

pop_image = function (e) {
    image = e.attr('src')
    html = "<img src='" + image + "' class='pop_image'>"
    $('.full_image').addClass('active').append(html)
}

pop_gallery = function (e) {
    lis = e.children()
    imgs = []
    lis.each(function () {
        imgs.push($(this).children().attr('src'))
    })
    html = '<div class="gallery gallery_pop"><ul class="image-gallery gallery list-unstyled cS-hidden">'
    for (let i = 0; i < imgs.length; i++) {
        html += '<li data-thumb="' + imgs[i] + '"><img src="' + imgs[i] + '"></li>'
    }
    html += '</ul></div>'
    $('.full_image').addClass('active').append(html)

    var slider_gal = $('.full_image .image-gallery').lightSlider({
        gallery: true,
        item: 1,
        thumbItem: 4,
        slideMargin: 10,
        thumbMargin: 20,
        speed: 2500,
        loop: true,
        onSliderLoad: function (gel) {
            $('.full_image .image-gallery').removeClass('cS-hidden');
	        $('.full_image .image-gallery').css('height', 'auto')
            gel.lightGallery({
                selector: '.full_image .image-gallery .lslide'
            });
        }
    });
    $('.lSPrev').click(function () {
        slider.goToPrevSlide();
    })
    $('.lSNext').click(function () {
        slider.goToNextSlide();
    })

}

pop_image_remove = function () {
    $('.full_image').removeClass('active')
    $('.pop_image').remove()
    $('.full_image .gallery').remove()
}

yt_play = function (e) {
    console.log(e.find('iframe')[0])
    e.find('iframe')[0].contentWindow.postMessage({"api": "play"}, "*");

}

// Inits
$(document).ready(function () {
    if($('.charitable').length > 0) {
        $('.charitable').parent().css('flex-direction','row');
    }
    main_menu_collapse()

    $('.navbar-tags .more').click(function () {
        $(this).parent().toggleClass('active')
        $(this).remove()
    })
    $('.navbar-footer .more').click(function () {
        $(this).parent().toggleClass('active')
        $(this).remove()
    })

    let frames = $('.video-element iframe').add($('.video-block iframe'))
    frames.each(function (i) {
        let html = '<div id="player' + i + '" style="border: 1px solid #c5c5c5;"></div>'
        $(this).parent().prepend(html)
        $(this).remove()
    })
    frames.each(function (i) {
        const vfile = $(this).attr('src')
        var player = new Playerjs({id: "player" + i, file: vfile});
    })
    if ($('.ant-carousel').length > 0) {
	    $ytLinks = $('.slide-element > div:first-child > div> p> a')
        $ytAll = $ytLinks.length
        $ytLeftPos = 0;
        $ytRightPos = 3;
        for (i = $ytLeftPos; i <= $ytRightPos; i++) {
            vfile = $ytLinks[i].innerHTML
            var player = new Playerjs({id: "ytPlayer" + i, file: vfile});
        }
    }
    $('.ant-carousel-arrow-right').click(function () {
        loadMoreYtVideo('right')
    })
    $('.ant-carousel-arrow-left').click(function () {
        loadMoreYtVideo('left')
    })

    $('#btn_search').click(function () {
        $('.form-search').toggleClass('active')
        $('.form-search input').focus()
    })

    $('.gallery ul').click(function () {
        pop_gallery($(this));
    })

    $('.container img').click(function () {
	if (!$(this).hasClass('pop_gal') && $(this).parent()[0].tagName.toLowerCase() !== 'a') {
            pop_image($(this));
	}
    })

    $('.full_image').click(function () {
        pop_image_remove()
    })

});

window.onload = function () {
    $('.gallery li img').addClass('pop_gal')
    $('.ant-carousel-element .slide-element').css('opacity', 1);
};

function loadMoreYtVideo(trend) {
    if (trend == 'left') {
        if ($ytLeftPos == 0) {
            $ytLeftPos = $ytAll - 1
            vfile = $ytLinks[$ytLeftPos].innerHTML
	    console.log(vfile)
            var player = new Playerjs({id: "ytPlayer" + $ytLeftPos, file: vfile});
        } else if ($ytLeftPos > $ytRightPos) {
            $ytLeftPos -= 1
            vfile = $ytLinks[$ytLeftPos].innerHTML
	    console.log(vfile)
            var player = new Playerjs({id: "ytPlayer" + $ytLeftPos, file: vfile});
        }
    } else if (trend == 'right') {
        if ($ytRightPos == $ytAll) {
            $ytRightPos = $ytAll
        } else if ($ytRightPos < $ytLeftPos || $ytLeftPos == 0) {
            $ytRightPos += 1
            vfile = $ytLinks[$ytRightPos].innerHTML
	    console.log(vfile)
            var player = new Playerjs({id: "ytPlayer" + $ytRightPos, file: vfile});
        }

    }
}