// get template (index.html) elements
const buttonSubmit = document.querySelector("#submit");
const inputQuestion = document.querySelector("#question");
const containerChat = document.querySelector("#chat");
const animation = document.querySelector("#animation");

// Action when i click the button
buttonSubmit.addEventListener("click", ()=>{
    sendMsg();
});

// Action when i press Return button
document.addEventListener("keydown", (e)=>{
    if (e.key === "Enter"){
        e.preventDefault();
        sendMsg();
    }
});

//
function sendMsg() {
    // get and clear content of input question
    const msgClient = clearTextArea(inputQuestion);

    // create a div to caontain the user question
    const msgClientElementContainer = document.createElement("div");
    // add class container
    msgClientElementContainer.className = "q-container";

    // prepare the question to inject in the question container
    const msgClientElement = document.createElement("div");
    msgClientElement.className = "q" ;
    msgClientElement.innerText = msgClient;

    // puts the question class 'q' in the container 'q-container'
    msgClientElementContainer.appendChild(msgClientElement);

    // Put the client's question in the chat container
    containerChat.appendChild(msgClientElementContainer);

    // delete the bot 'speak' animation state
    animation.classList.remove("speak");
    // run the 'wait' animation state
    animation.classList.add("wait");

    // scroll down the {containerChat} automaticaly
    scrollDown();

    // init the http request to the server and inject server answers in the {containerChat}
    loadXMLDoc(msgClient);
}

// init the http request to the server and inject server answers in the {containerChat}
function loadXMLDoc(value)
{
    // create a new XMLHttpRequest object
    const req = new XMLHttpRequest();

    // listen the status change during the request to the server
    req.addEventListener("readystatechange", ()=>{
        // when we get the answer 4 (meaning everything went well)
        if (req.readyState === 4)
        {
            if (req.status != 200)
            {
                console.error(req.status)
            }
            else
            {
                // get {.responseText} of the {req} object and make it a JSON
                const response = JSON.parse(req.responseText);

                //inject values got from the server and put it in {containerChat}
                injectQR(response.response1, response.image, response.response2);

                // update bot animation state
                animation.classList.remove("wait");
                animation.classList.add("speak");
            }
        }
    }, true); // asynchronous request

    // init requets
        req.open('POST', '/ajax');
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        // built the string send to the server with the textarea value
        const postVars = 'question='+value;

    // send the request
    req.send(postVars);
    
    return false;
}


function injectQR(response1, image, response2){
    // response 1
    const constReponse1ElementContainer = document.createElement("div");
    constReponse1ElementContainer.className = "r-container";

    const constReponse1 = document.createElement("div");
    constReponse1.className = "r" ;
    constReponse1.innerHTML = response1;

    // image
    const imgContainer = document.createElement("div");
    imgContainer.className = "r-container img";

    const constReponseImg = document.createElement("div");
    constReponseImg.className = "r img" ;

    const img = document.createElement("img");
    img.src = image;

    // response 2
    const constReponse2ElementContainer = document.createElement("div");
    constReponse2ElementContainer.className = "r-container";

    const constReponse2 = document.createElement("div");
    constReponse2.className = "r" ;
    constReponse2.innerHTML = response2;

    // inject msg in view
    constReponse1ElementContainer.appendChild(constReponse1);
    constReponseImg.appendChild(img);
    imgContainer.appendChild(constReponseImg);
    constReponse2ElementContainer.appendChild(constReponse2);

    containerChat.appendChild(constReponse1ElementContainer);
    containerChat.appendChild(imgContainer);
    containerChat.appendChild(constReponse2ElementContainer);

    scrollDown();
 }

// return content of a text area element
// and clear it
function clearTextArea(areaElement = document.querySelector("textarea")) {
    const contentToReturn = areaElement.value;
    areaElement.value = "";
    return contentToReturn.replace(/</g,"&lt;").replace(/>/g,"&gt;"); // prevent script injection
 }

 function scrollDown() {
     containerChat.scrollTop = containerChat.scrollHeight;
 }
