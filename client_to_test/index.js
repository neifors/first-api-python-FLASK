const button = document.getElementById("our-films")
const form = document.getElementById("find-film-form")
const filmsList = document.getElementById("list-films")
const moreFilms = document.getElementById("more-films")


async function getOurFilms(e){
   e.preventDefault()
   const options = {
      method: 'GET',
      headers: { "Content-Type": "application/json" },
   } 
   const result = await fetch("http://127.0.0.1:5000/api/films", options);
   const data = await result.json()
   console.log(data)
   renderOurFilms(data)
}

button.addEventListener("click", getOurFilms)

async function postFilm(e){
   const options = {
      method: 'POST',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
          name: e.target["title"].value,
          year: e.target["year"].value
      })
   }
   const result = await fetch("http://127.0.0.1:5000/api/films", options);
   const data = await result.json()
   console.log(data)
}

form.addEventListener('submit', postFilm)

async function deleteFilm(id){
   const options = {
      method: 'DELETE',
      headers: { "Content-Type": "application/json" }
   }
   const result = await fetch(`http://127.0.0.1:5000/api/films/${id}`, options);
   const data = await result.json()
   console.log(data)

}

function renderOurFilms(films) {
   filmsList.innerHTML=""

   films.map( film => {
      let li = document.createElement('li')
      li.textContent = film.name
      let deleteBttn = document.createElement("button")
      deleteBttn.onclick = function(){ 
         deleteFilm(film.id)
         window.location.reload(true) 
      }
      deleteBttn.textContent = "X"
      li.appendChild(deleteBttn)
      filmsList.appendChild(li)
   })
}

async function getFilms(e){
   e.preventDefault()
   const options = {
      method: 'GET',
      headers: { "Content-Type": "application/json" },
   } 
   const result = await fetch("http://127.0.0.1:5000/outside/api/films", options);
   const data = await result.json()
   console.log(data)
   renderFilms(data)
}

moreFilms.addEventListener("click", getFilms)
const outsideList = document.getElementById("outside-films")

function renderFilms(films) {
   outsideList.innerHTML=""

   films.map( film => {
      let li = document.createElement("li")
      li.textContent = film.title
      outsideList.appendChild(li)
   })
}
