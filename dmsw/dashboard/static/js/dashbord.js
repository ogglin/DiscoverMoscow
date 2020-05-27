$(document).ready(function () {
    $pid = $('.main_tag select').val();
    $sub_opts = $('.sub_tag option');
    $color_opts = $('.main_color option')
    named_opts();
    change_opts();
    $('.main_tag select').change(function () {
        $pid = $(this).val();
        $('.sub_tag').addClass('active');
        change_opts()
    });

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
        if($sub_opts.eq(i).attr('name') == $pid) {
            $sub_opts.eq(i).addClass('active')
        } else {
            $sub_opts.eq(i).removeClass('active')
        }
    }
    for (i = 0; i < $color_opts.length; i++) {
        if($color_opts.eq(i).attr('name') == $pid) {
            $color_opts.eq(i).addClass('active')
        } else {
            $color_opts.eq(i).removeClass('active')
        }
    }
}