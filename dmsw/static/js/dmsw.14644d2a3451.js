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

//Slider aditional
var slideNow_right = 1;
var slideCount_right = $('#slidewrapper-right').children().length;
var slideInterval_right = 100000;
var navBtnId_right = 0;
var translateWidth_right = 0;
var switchInterval_right = setInterval(nextSlideRight, slideInterval_right);
slideNavs_right = $('.slide-nav-btn-right')
setActive();
$(document).ready(function() {
    setActive();
    $('#viewport-right').hover(function() {
        clearInterval(switchInterval_right);
    }, function() {
        switchInterval_right = setInterval(nextSlide, slideInterval_right);
    });

    $('#next-btn-right').click(function() {
        nextSlideRight();
    });

    $('#prev-btn-right').click(function() {
        prevSlideRight();
    });

    $('.slide-nav-btn-right').click(function() {
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
        if (slideNow_right == index+1) {
            $( this ).addClass('active')
        }
    })
}

// $(window).scroll(function(){
//     scrollTop = window.pageYOffset
//     if (scrollTop >= 390) {
//         $('.slider_block').addClass('sticky')
//     }
//     if (scrollTop < 390) {
//         $('.slider_block').removeClass('sticky')
//     }
// });

// Main menu open/close
function main_menu_collapse() {
    menu_width = $('header nav').width()
    menu_items = $('.main_menu li')
    menu_width_cur = 0
    menu_items.each(function () {
        menu_width_cur += $(this).width() + 40
    })
    if (menu_width < (menu_width_cur + 71.15)) {
        $('header .main_menu').addClass('collapse')
    }
    if (menu_width >= (menu_width_cur + 71.15)) {
        $('header .main_menu').removeClass('collapse')
    }
}
$(window).resize(function() {
    main_menu_collapse();
    nextSlideRight();
})
$('header #more').click(function () {
    $('header .main_menu').toggleClass('open')
})

pop_image = function(e){
    image = e.attr('src')
    html = "<img src='"+ image +"' class='pop_image'>"
    $('.full_image').addClass('active').append(html)
}

pop_gallery = function(e) {
    lis = e.children()
    imgs = []
    lis.each(function () {
        imgs.push($(this).children().attr('src'))
    })
    html = '<div class="gallery gallery_pop"><ul class="image-gallery gallery list-unstyled cS-hidden">'
    for (let i = 0; i < imgs.length; i++) {
        html += '<li data-thumb="'+ imgs[i] +'"><img src="'+ imgs[i] + '"></li>'
    }
    html += '</ul></div>'
    $('.full_image').addClass('active').append(html)

    var slider = $('.full_image .image-gallery').lightSlider({
        gallery:true,
        item:1,
        thumbItem:4,
        slideMargin: 10,
        thumbMargin: 20,
        speed:2500,
        loop:true,
        onSliderLoad: function(el) {
            $('.full_image .image-gallery').removeClass('cS-hidden');
            el.lightGallery({
                selector: '.full_image .image-gallery .lslide'
            });
        }
   });
   $('.lSPrev').click(function () {
        slider.goToPrevSlide();
    })
   $('.lSNext').click( function () {
        slider.goToNextSlide();
   })

}

pop_image_remove = function(){
    $('.full_image').removeClass('active')
    $('.pop_image').remove()
    $('.full_image .gallery').remove()
}

yt_play = function(e) {
    console.log(e.find('iframe')[0])
    e.find('iframe')[0].contentWindow.postMessage({"api":"play"}, "*");

}

// Inits
$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
      loop: true,
      margin: 80,
      nav: true,
    });

    main_menu_collapse()

    $('.ytp-chrome-top').css('display','none')
    yt_elements = $('iframe')
    yt_elements.each(function () {
        $(this).height($(this).width()*0.5625)
    })
    yt_videos = $('.video-block div iframe')
    yt_videos.each(function () {
        $(this).height($(this).width()*0.5625)
    })

    $('#btn_search').click(function () {
        $('.form-search').toggleClass('active')
    })

    $('.gallery ul').click(function () {
        pop_gallery($(this));
    })

    $('.container .two-column img').click(function () {
        pop_image($(this));
    })

    $('.container > img').click(function () {
        pop_image($(this));
    })

    $('.full_image').click(function () {
        pop_image_remove()
    })

    let frames = $('.video-element iframe').add($('.slide-element iframe')).add($('.video-block iframe'))
    frames.each(function (i) {
        let html = '<div id="player'+i+'"></div>'
        // const img = '<img class="yt_play_btn" src="/static/image/play.svg" data="player'+i+'">'
        $(this).parent().prepend(html)
        // $(this).parent().append(img)
        $(this).remove()
    })
    frames.each(function (i) {
        const vfile = $(this).attr('src')
        var player = new Playerjs({id:"player"+i, file: vfile});
    })

    $('.yt_play_btn').click(function () {
        yt_play($(this).parent())
    })
});