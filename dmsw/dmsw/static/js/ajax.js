// $( document ).ready(function() {
//     $("#btn").click(
// 		function(){
// 			sendAjaxForm('result_form', 'ajax_form', '.');
// 			return false;
// 		}
// 	);
// });
// function sendAjaxForm(result_form, ajax_form, url) {
// 	console.log($("#"+ajax_form).serialize())
//     $.ajax({
//         url:     url, //url страницы (action_ajax_form.php)
//         type:     "POST", //метод отправки
//         dataType: "html", //формат данных
//         data: $("#"+ajax_form).serialize(),  // Сеарилизуем объект
//         success: function(response) { //Данные отправлены успешно
//         	result = $.parseJSON(response);
//         	$('#result_form').html('email: '+result.email);
//     	},
//     	error: function(response) { // Данные не отправлены
//             $('#result_form').html('Ошибка. Данные не отправлены.');
//     	}
//  	});
// }

$(document).ready(function(){
    var $myForm = $('.subscribe-ajax-form')
    $myForm.submit(function(event){
        event.preventDefault()
        var $formData = $(this).serialize()
        var $thisURL = $myForm.attr('data-url') || window.location.href // or set your own url
        $.ajax({
            method: "POST",
            url: $thisURL,
            data: $formData,
            success: handleFormSuccess,
            error: handleFormError,
        })
    })

    function handleFormSuccess(data, textStatus, jqXHR){
        console.log(data)
        console.log(textStatus)
        console.log(jqXHR)
        $('.data_form').remove()
        $('.result_form').html(data['message']);
        $myForm[0].reset(); // reset form data
    }

    function handleFormError(jqXHR, textStatus, errorThrown){
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)
		$('.result_form').html('Ошибка. Данные не отправлены.');
    }
})

$(document).ready(function () {
    let $AjaxMore = $('.ajax_load_more form')
    $(window).scroll(function(){
        scrollTracking($AjaxMore)
    })

})
let block_show = null;
function scrollTracking(el){
	var wt = $(window).scrollTop();
	var wh = $(window).height();
	var et = el.offset().top;
	var eh = el.outerHeight();
    var $formData = el.serialize()

	if (wt + wh >= et && wt + wh - eh * 2 <= et + (wh - eh)){
		if (block_show == null || block_show == false) {
			console.log('Блок active в области видимости');
			$.ajax({
                method: "POST",
                url: window.location.href,
                data: $formData,
                success: handleSuccess,
                error: handleError,
            })
		}
		block_show = true;
	} else {
		if (block_show == null || block_show == true) {
			console.log('Блок active скрыт');
		}
		block_show = false;
	}
}
function handleSuccess(data, textStatus, jqXHR){
    console.log(data)
    console.log(textStatus)
    console.log(jqXHR)
}
function handleError(jqXHR, textStatus, errorThrown){
    console.log(jqXHR)
    console.log(textStatus)
    console.log(errorThrown)
}