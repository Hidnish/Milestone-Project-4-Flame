$(document).ready(function () {

    // Sidenav for xs to medium screen sizes from: https://github.com/frontendfunn/bootstrap-4-sidebar
    $('.navbar-toggler, .overlay, .close-nav').on('click', function () {
        $('.mobileMenu, .overlay').toggleClass('open mobileMenuOpen');
    });

    // Dropdown slide effect from: https://newbedev.com/adding-a-slide-effect-to-bootstrap-dropdown
    $('.dropdown').on('show.bs.dropdown', function () {
        if ($(window).width() <= 992) {
            $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
        } else {
            $(this).find('.dropdown-menu').first().stop(false, false).fadeIn('fast');
        }
    });
    // Add slideUp animation to Bootstrap dropdown when collapsing.
    $('.dropdown').on('hide.bs.dropdown', function () {
        if ($(window).width() <= 992) {
            $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
        } else {
            $(this).find('.dropdown-menu').first().stop(true, true).fadeOut('fast');
        }
    })

    // 
    $(document).scroll(function () {
        if ($(this).scrollTop() >= $(".navbar").height()) {
            $(".navbar").addClass('scrolled');
            $(".navbar").removeClass('navbar-bg');
        } else {
            $(".navbar").removeClass('scrolled');
            $(".navbar").addClass('navbar-bg')
        }
    });

    // Page Loader 
    $(window).ready(function () {
        $(".loader").fadeOut("slow")
        $(".loader2").fadeOut("fast");
    });

    // Modal to ask for action confirmation (i.e. delete)
    $('.are-you-sure').click(function(e) {
        e.preventDefault();
        if (window.confirm("Are you sure you want to proceed?")) {
            location.href = this.href;
        }
    });
});