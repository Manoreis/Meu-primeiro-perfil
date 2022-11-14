let count=1;
document.getElementById(radio1).cheked = true;

setInterval (function(){
    nextimage()

},2000) 

function nextimage(){
    count++;
    if (count>5){
        count = 1;
    }

    document.getElementById("radio" +count). cheked= true
}