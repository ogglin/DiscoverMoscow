var dop_slideNow = 1;
var dop_slideCount = $('#slidewrapper').children().length;
var dop_slideInterval = 5000;
var dop_navBtnId = 0;
var dop_dop_translateWidth = 0;
var dop_switchInterval = setInterval(dop_nextSlide, dop_slideInterval);
dop_slideNavs = $('.slide-nav-btn')

$(document).ready(function() {
    dop_setActive();
    $('#viewport').hover(function() {
        clearInterval(dop_switchInterval);
    }, function() {
        dop_switchInterval = setInterval(dop_nextSlide, dop_slideInterval);
    });

    $('#next-btn').click(function() {
        dop_nextSlide();
    });

    $('#prev-btn').click(function() {
        dop_prevSlide();
    });

    $('.slide-nav-btn').click(function() {
        $('.slide-nav-btn').removeClass('active')
        $(this).addClass('active')
        dop_navBtnId = $(this).index();

        if (dop_navBtnId + 1 != dop_slideNow) {
            dop_dop_translateWidth = -$('#viewport').width() * (dop_navBtnId);
            $('#slidewrapper').css({
                'transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
                '-webkit-transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
                '-ms-transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
            });
            dop_slideNow = dop_navBtnId + 1;
        }
    });
});


function dop_nextSlide() {
    if (dop_slideNow == dop_slideCount || dop_slideNow <= 0 || dop_slideNow > dop_slideCount) {
        $('#slidewrapper').css('transform', 'translate(0, 0)');
        dop_slideNow = 1;
    } else {
        dop_dop_translateWidth = -$('#viewport').width() * (dop_slideNow);
        $('#slidewrapper').css({
            'transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
            '-ms-transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
        });
        dop_slideNow++;
    }
    dop_setActive()
}

function dop_prevSlide() {
    if (dop_slideNow == 1 || dop_slideNow <= 0 || dop_slideNow > dop_slideCount) {
        dop_dop_translateWidth = -$('#viewport').width() * (dop_slideCount - 1);
        $('#slidewrapper').css({
            'transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
            '-ms-transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
        });
        dop_slideNow = dop_slideCount;
    } else {
        dop_dop_translateWidth = -$('#viewport').width() * (dop_slideNow - 2);
        $('#slidewrapper').css({
            'transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
            '-ms-transform': 'translate(' + dop_dop_translateWidth + 'px, 0)',
        });
        dop_slideNow--;
    }
    dop_setActive()
}

function dop_setActive() {
    $('.slide-nav-btn').removeClass('active')
    dop_slideNavs.each(function (index) {
        if (dop_slideNow == index+1) {
            $( this ).addClass('active')
        }
    })
}

$(window).resize(function() {
    dop_nextSlideRight();
})