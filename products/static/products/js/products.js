

$(document).ready(function () {

    // Show product info or review 
    $(".review-container").css('display', 'none');
    $("#product-details-button").click((e) => {
        e.preventDefault();
        $(".product-details-container").css('display', 'block');
        $(".review-container").css('display', 'none');
        $(".card-body").removeClass('card-scroll');
    })
    $("#product-review-button").click((e) => {
        e.preventDefault();
        $(".product-details-container").css('display', 'none');
        $(".review-container").css('display', 'block');
        $(".card-body").addClass('card-scroll');
    })

    // Save product review 

    $("#addForm").submit(function (e) {
        $.ajax({
            data: $(this).serialize(),
            method: $(this).attr('method'),
            url: $(this).attr('action'),
            dataType: 'json',
            success: function (res) {
                if (res.bool == true) {
                    $("#reset").trigger('click');
                    $("#no-review").css('display', 'none');

                    // Generate review timestamp 
                    const m = new Date()
                    var date = m.toLocaleString('en-us', {
                        month: 'short'
                    }) + ", " + m.getDate() + ", " + m.getFullYear() + ", " + m.getHours() + ":"
                    + (m.getMinutes() < 10 ? '0' : '') + m.getMinutes();


                    // Format data to display last review without refreshing the page
                    var _html = `<hr><small>${res.data.user} &nbsp - &nbsp ${date}</small> <br>`;
                    for (var i = 1; i <= res.data.review_rating; i++) {
                        _html += '<i class="fa fa-star text-warning mb-2 mr-1"></i>';
                    }
                    _html += `<br> <p>${res.data.review_text}</p>`;

                    // Prepend Data
                    $(".review-current").prepend(_html);

                    // Hide Modal
                    $("#productReview").modal('hide');
                }
            }
        });
        e.preventDefault();
    });


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

})