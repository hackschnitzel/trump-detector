alert('hlallas')


document.onload=function(){
    document.getElementById('mybutton').addEventListener('click', function (event) {
        event.preventDefault();


        // Do something
        //updateProperties();
        var newName = 'John Smith',
            xhr = new XMLHttpRequest();

        var formData = new FormData(document.getElementById("trumpette"));


//xhr.open('POST', 'check?Title=foo&Text=bar');
        xhr.onload = function () {
            if (xhr.status === 200 && xhr.responseText !== newName) {
                alert('Something went wrong.  Name is now ' + xhr.responseText);
            }
            else if (xhr.status !== 200) {
                alert('Request failed.  Returned status of ' + xhr.status);
            }
        };
        xhr.send(formData);
        return false;
    });


}
