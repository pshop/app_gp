    const buttonSubmit = document.querySelector("#submit");
    const inputQuestion = document.querySelector("#question");

    buttonSubmit.addEventListener("click", ()=>{
        loadXMLDoc(inputQuestion.value);
    });
    document.addEventListener("keydown", (e)=>{
        if (e.key === "Enter"){
            e.preventDefault();
            loadXMLDoc(inputQuestion.value)
        }

    });
    
    function loadXMLDoc(value)
    {
        var req = new XMLHttpRequest();
        req.addEventListener("readystatechange", ()=>{
            if (req.readyState === 4)
            {
                if (req.status != 200)
                {
                    console.error(req.status)
                }
                else
                {
                    const response = JSON.parse(req.responseText);
                    console.log(response);
                    injectQR(response.question, response.response)
                }
            }
        });
    
        req.open('POST', '/ajax');
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        const postVars = 'question='+value;
        req.send(postVars);
        
        return false;
    }

    function injectQR(question, response){
        const container = document.createElement("div");
        container.className = "qr";

        const contQuestion = document.createElement("div");
        contQuestion.className = "q";
        contQuestion.innerHTML = question;

        const contResponse = document.createElement("div");
        contResponse.className = "r" ;
        contResponse.innerHTML = response;

        container.appendChild(contQuestion);
        container.appendChild(contResponse);

        document.querySelector("#chat").appendChild(container);

     }
