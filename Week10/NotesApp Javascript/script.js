/*
    editbtn d.qS(.edit)
    noteEl
        d.qs(.notes)
    deleteBtn 
        d.qs('.delete')
    main

*/
const notesEl=document.querySelector(".notes");
const editBtn=document.querySelector(".edit");
const deleteBtn=document.querySelector(".delete");
const main=notesEl.querySelector(".main");
const textArea=notesEl.querySelector("textarea");

editBtn.addEventListener("click",()=>{
    main.classList.toggle("hidden");
    textArea.classList.toggle("hidden");
})
