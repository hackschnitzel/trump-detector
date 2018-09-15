window.onload=function(){
    document.getElementById('submitbutton').addEventListener('click', function (event) {
        do_ajax()
    });

    function do_ajax() {
        var req = new XMLHttpRequest();
        req.onreadystatechange = function(){
            console.log(this.responseText)
        };
        req.open('POST', '/api/label', true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        req.send("Title=" + document.getElementById('Title').value + "&Text=" + document.getElementById('Text').value + "&Fake=" + document.getElementById('fakeNews').checked);
    }
}
