let __CAROUSEL_OBJECTS = [],
    __CAROUSEL_OBJECTS_SHIFTED = [],
    slideTimeout = 1000,
    carouselElementsCounter = 5,
    indexLeft = 0,
    indexRight = 0,
    changeDirectionTimeout = 500,
    timesRepeated = 30


function slideElementRight() {
    indexRight += 1
    let $element = __CAROUSEL_OBJECTS.shift()

    __CAROUSEL_OBJECTS_SHIFTED.push($element)

    $element.css('width', 0)
    setTimeout(function () {$element.css('margin', '0 0.4%')}, slideTimeout / 5)
    setTimeout(function () {$element.css('margin', '0 0.3%')}, slideTimeout / 5)
    setTimeout(function () {$element.css('margin', '0 0.2%')}, slideTimeout / 5)
    setTimeout(function () {$element.css('margin', '0 0.1%')}, slideTimeout / 5)
    setTimeout(function () {$element.css('margin', '0 0')}, slideTimeout / 2)


    if (__CAROUSEL_OBJECTS.length > carouselElementsCounter) {
        setTimeout(slideElementRight, slideTimeout * (indexRight + 1))
    } else if (indexRight < timesRepeated) {
        __CAROUSEL_OBJECTS = __CAROUSEL_OBJECTS_SHIFTED.concat(__CAROUSEL_OBJECTS)
        __CAROUSEL_OBJECTS_SHIFTED = []

        setTimeout(slideElementLeft, changeDirectionTimeout * indexRight)
    }
}


function slideElementLeft() {
    indexLeft += 1
    let $element = __CAROUSEL_OBJECTS.shift()

    __CAROUSEL_OBJECTS_SHIFTED.push($element)

    $element.css('width', '17.5%')
    setTimeout(function () {$element.css('margin', '0 0.1%')}, slideTimeout / 5)
    setTimeout(function () {$element.css('margin', '0 0.2%')}, slideTimeout / 5)
    setTimeout(function () {$element.css('margin', '0 0.3%')}, slideTimeout / 5)
    setTimeout(function () {$element.css('margin', '0 0.4%')}, slideTimeout / 5)
    setTimeout(function () {$element.css('margin', '0 0.5%')}, slideTimeout / 2)

    if (__CAROUSEL_OBJECTS.length > carouselElementsCounter) {
        setTimeout(slideElementLeft, slideTimeout)
    } else if (indexLeft < timesRepeated) {
        __CAROUSEL_OBJECTS = __CAROUSEL_OBJECTS_SHIFTED.concat(__CAROUSEL_OBJECTS)
        __CAROUSEL_OBJECTS_SHIFTED = []

        setTimeout(slideElementRight, changeDirectionTimeout * (indexRight + 1))
    }
}


$(document).ready(function() {
    const $body = $('body'),
          $carouselImages = $('.carousel-image')

    $carouselImages.each(function() {
        __CAROUSEL_OBJECTS.push($(this))
    })

    setTimeout(slideElementRight, slideTimeout)
})