function changeContext(page) {

    var grey = 'rgba(255, 255, 255, 0.2)';
    var white = 'white';

    if(!page) {
        $('.welcome').css('display', 'none');
        $('.overview').css('display', 'block');
        $('.select-resume > div').css('background-color', grey);
        $('.select-resume > div + div').css('background-color', white);
    } else {
        $('.welcome').css('display', 'flex');
        $('.overview').css('display', 'none');
        $('.select-resume > div').css('background-color', white);
        $('.select-resume > div + div').css('background-color', grey);
    }
}
