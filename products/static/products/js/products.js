// Save product review 

// $(document).ready(function() {
//     $('#addForm').submit(function(event) {
//         $.ajax({
//             data:$(this).serialize(),
//             method:$(this).attr('method'),
//             url:$(this).attr('action'),
//             dataType: 'json',
//             success: function(response) {
//                 if (response.bool == true) {
//                     $('.ajaxRes').html('Data has been added');
//                     $('#reset').trigger('click');
//                 };
//             }
//         })
//         event.preventDefault();
//     })
// })

$("#addForm").submit(function (e) {
    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr('method'),
        url: $(this).attr('action'),
        dataType: 'json',
        success: function (res) {
            if (res.bool == true) {
                $(".ajaxRes").html('Data has been added.');
                $("#reset").trigger('click');
                // Hide Button
                $(".reviewBtn").hide();
                // End

                const timeElapsed = Date.now();
                const today = new Date(timeElapsed);
                const date = today.toDateString();
                console.log(date);

                // create data for review
                var _html = `<i>${res.data.user}</i> &nbsp - &nbsp <small>${date}</small>
                <br>`;
                for (var i = 1; i <= res.data.review_rating; i++) {
                    _html += '<i class="fa fa-star text-warning"></i>';
                }
                `<br> 
                <p>${res.data.review_text}</p>`;

                var _html = '<i>' + res.data.user + '</i> &nbsp - &nbsp <small>' + res.data.date + '</small> <br>';
                for (var i = 1; i <= res.data.review_rating; i++) {
                    _html += '<i class="fa fa-star text-warning"></i>';
                }
                _html += `<br> <p>${res.data.review_text}</p>`;

                // $(".no-data").hide();

                // Prepend Data
                $(".review-current").prepend(_html);

                // Hide Modal
                $("#productReview").modal('hide');

                // AVg Rating
                $(".avg-rating").text(res.avg_reviews.avg_rating.toFixed(1))
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