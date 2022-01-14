// Save product review 

$(document).ready(function() {
    $('#addForm').submit(function(event) {
        $.ajax({
            data:$(this).serialize(),
            method:$(this).attr('method'),
            url:$(this).attr('action'),
            dataType: 'json',
            success: function(response) {
                if (response.bool == true) {
                    $('.ajaxRes').html('Data has been added');
                    $('#reset').trigger('click');
                };
            }
        })
        event.preventDefault();
    })
})


// Slider for related products 

new Glider(document.querySelector('.glider'), {
    slidesToShow: 1,
    slidesToScroll: 1,
    draggable: true,
    arrows: {
        prev: '.glider-prev',
        next: '.glider-next'
    },
    responsive: [{
        breakpoint: 576,
        settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
        }
    }, {
        breakpoint: 768,
        settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
        }
    }, {
        breakpoint: 992,
        settings: {
            slidesToShow: 4,
            slidesToScroll: 4,
        }
    }]
});

