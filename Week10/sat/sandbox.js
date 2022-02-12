//http req method

//1. create a request method
const request=new XMLHttpRequest();
//create request object. used to send to the server


//2. give ardument: request methid,request url
request.open("GET","https://jsonplaceholder.typicode.com/todos");
//this only opens up the request

request.send();

//Track the progress of this request
//"evetn listener"+"reasy state change"
request.addEventListener("readystatechange",()=>{
    if(request.readyState===4){
        console.log("Ho gai")
        console.log(request.responseText)
    }
    
})
