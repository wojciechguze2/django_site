

function initPagination(listContainer='.content-container') {
    const $body = $('body'),
        pageLink = '.page-link'

    $body.on('click', pageLink, function(e) {
        e.stopImmediatePropagation()

        if ($(this).parent().hasClass('active')) {  // current page
            return
        }

        const page = $(this).attr('data-page'),
            url = new URL(window.location.href)

        url.searchParams.append('page', page);

        $.get({
            url: url,
            success: function(response) {
                $(listContainer).html(response)
            },
            error: function(xhr, status, exception) {
                console.error(this.constructor.name, xhr, status, exception)
            },
            complete: function() {
            }
        })
    })
}