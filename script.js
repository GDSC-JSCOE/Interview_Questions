const div=document.querySelector('.container')
fetch('./index.json')
.then(res=>res.json())
.then(data=>data.map((item)=>{
    console.log(item);
    document.createTextNode(item.question)
    div.appendChild(document.createTextNode(item.question))
    div.appendChild(document.createElement('br'))
    div.appendChild(document.createTextNode(item.answerLink))
    div.appendChild(document.createElement('br'))
    div.appendChild(document.createElement('br'))
}))


