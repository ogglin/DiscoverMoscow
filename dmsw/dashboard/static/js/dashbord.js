$(document).ready(function () {
    $pathname = window.location.pathname;
    $pid = $('.main_tag select').val();
    $sub_opts = $('.sub_tag option');
    $color_opts = $('.main_color option')
    named_opts();
    change_opts();
    $cur_locale = $('#id_locale').val()
    console.log($cur_locale)
    // if($cur_locale = 'ru') {
        $('.main_tag select').change(function () {
            $pid = $(this).val();
            $('.sub_tag').addClass('active');
            change_opts()
        });
    // } else if($cur_locale = 'en'){
    //
    // }


    //Article list blogindexpageru
    if ($pathname.indexOf('blogindexpageen') > 0) {
        $('#blogindexpageen')[0].click()
    } else if ($pathname.indexOf('blogindexpage') > 0) {
        $('#blogindexpageru')[0].click()
    }


    //Tags
    $tags = $('#id_parent_id option')
    if ($pathname.indexOf('/tagsen/') > 0){
        for (i = 0; i < $tags.length; i++) {
            if (isKyr($tags[i].innerHTML)) {
                $tags.eq(i).css('display', 'none')
            }
        }
    } else if ($pathname.indexOf('/tags/') > 0){
        for (i = 0; i < $tags.length; i++) {
            if (isKyr($tags[i].innerHTML)) {

            } else {
                $tags.eq(i).css('display', 'none')
            }
        }
    }

    $color_tags = $('#id_tag_id option')
    if ($pathname.indexOf('/tagcolorsen/') > 0){
        for (i = 0; i < $color_tags.length; i++) {
            if (isKyr($color_tags[i].innerHTML)) {
                $color_tags.eq(i).css('display', 'none')
            } else {
                console.log('is not cyrilic')
            }
        }
    } else if ($pathname.indexOf('/tagcolors/') > 0){
        for (i = 0; i < $color_tags.length; i++) {
            if (isKyr($color_tags[i].innerHTML)) {
                console.log('is latin')
            } else {
                $color_tags.eq(i).css('display', 'none')
            }
        }
    }

    if ($('.account')[0].innerText.indexOf('admin') > 0) {

    } else {
        $('.nav-main ul .menu-item:nth-child(7) .nav-submenu ul .menu-item:nth-child(6)').addClass('hidden')
        $('.nav-main ul .menu-item:nth-child(7) .nav-submenu ul .menu-item:nth-child(7)').addClass('hidden')
    }
})

function named_opts() {
    for (i = 0; i < $sub_opts.length; i++) {
        if ($sub_opts[i].innerHTML.match('[-]\\d*[-]\\W')) {
            $rep = $sub_opts[i].innerHTML.match('[-]\\d*[-]\\W')[0]
        } else {$rep = ''}

        $html = $sub_opts[i].innerHTML.replace($rep, '')
        $id = parseInt($sub_opts[i].innerHTML.match('[-]\\d*[-]\\W')[0].replace('-', '').trim());
        $sub_opts.eq(i).attr('name', $id)
        $sub_opts.eq(i).html($html)
    }
    for (i = 0; i < $color_opts.length; i++) {
        if($color_opts[i].innerHTML.match('[-]\\d*[-]\\W')){
            $rep = $color_opts[i].innerHTML.match('[-]\\d*[-]\\W')[0]
        } else {$rep = ''}

        $html = $color_opts[i].innerHTML.replace($rep, '')
        $id = parseInt($color_opts[i].innerHTML.match('[-]\\d*[-]\\W')[0].replace('-', '').trim())
        $color_opts.eq(i).attr('name', $id)
        $color_opts.eq(i).html($html)
    }
}

function change_opts() {
    for (i = 0; i < $sub_opts.length; i++) {
        if($sub_opts.eq(i).attr('name') == $pid || $sub_opts.eq(i).attr('name') == 'NaN') {
            $sub_opts.eq(i).addClass('active')
        } else {
            $sub_opts.eq(i).removeClass('active')
        }
    }
    for (i = 0; i < $color_opts.length; i++) {
        if($color_opts.eq(i).attr('name') == $pid || $sub_opts.eq(i).attr('name') == 'NaN') {
            $color_opts.eq(i).addClass('active')
        } else {
            $color_opts.eq(i).removeClass('active')
        }
    }
}

function isKyr(str) {
    return /[а-яё]/i.test(str);
}