window.onload=function(){
    document.getElementById('submitbutton').addEventListener('click', function (event) {
        do_ajax()
    });

    function do_ajax() {
        var req = new XMLHttpRequest();
        var result = document.getElementById('isfake');
        req.onreadystatechange = function()
        {
            if(this.readyState === 4 && this.status === 200) {
                var score = JSON.parse(this.responseText)['score'];
                result.innerHTML = score;
                if(parseFloat(score) > parseFloat(0.5)) {
                    result.style.color = "#f44242";
                }
                else {
                    result.style.color = "#13b70b";
                }
            }
        };
        req.open('POST', '/api/check', true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        req.send("Title=" + document.getElementById('Title').value + "&Text=" + document.getElementById('Text').value);
    }
}
