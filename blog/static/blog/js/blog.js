// Save  comment 
$(document).ready(function () {
    $("#addFormComment").submit(function (e) {
        $.ajax({
            data: $(this).serialize(),
            method: $(this).attr('method'),
            url: $(this).attr('action'),
            dataType: 'json',
            success: function (res) {
                if (res.bool == true) {
                    $("#reset").trigger('click');
                    $("#no-comment").css('display', 'none');
                    $("#addComment").hide();

                    // Generate comment timestamp 
                    const nDate = new Date()
                    var date = nDate.toLocaleString('en-us', {
                            month: 'short'
                        }) + ", " + nDate.getDate() + ", " + nDate.getFullYear() + ", " + nDate.getHours() + ":" +
                        (nDate.getMinutes() < 10 ? '0' : '') + nDate.getMinutes();


                    // Format data to display last comment without refreshing the page
                    var _html = `<hr><small>${res.data.user} &nbsp - &nbsp ${date}</small>`;
                    _html += `<small class="float-right"> 
                    <a class="text-danger delete-comment-btn" href="">Delete</a>
                    </small><br>`
                    _html += `<br> <p>${res.data.comment}</p>`;

                    // Prepend Data
                    $(".comment-current").prepend(_html);

                    // Hide Modal
                    $("#postComment").modal('hide');

                    $('.delete-comment-btn').click(function (e) {
                        e.preventDefault();
                        $(".comment-current").empty();
                        $('#delete-last-comment')[0].click();
                    })
                }
            }
        });
        e.preventDefault();
    });

    // Prevent delete_last_comment view from refreshing the page
    $('#delete-last-comment').on('click', function (e) {
        window.confirm("Are you sure you want to proceed?");
        $.ajax({
            data: $(this).serialize(),
            url: $(this).attr('href'),
            dataType: 'json',
            success: function (res) {
                if (res.bool == true) {
                    $("#addComment").show();
                    $("#no-comment").css('display', 'block');
                }
            }
        });
        e.preventDefault();;
    })
})