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

function renderFilms(films) {
   outsideList.innerHTML=""

   films.map( film => {
      let li = document.createElement("li")
      li.textContent = film.title
      li.onclick = function(){
         renderMoreInfo(film)
      }
      outsideList.appendChild(li)
   })
}

const moreInfo = document.getElementById("more-info")

function renderMoreInfo(film){
   moreInfo.innerHTML=""
   const overview = document.createElement('p')
   overview.textContent = film.overview
   const title = document.createElement("h2")
   title.textContent = film.title
   const release = document.createElement('p')
   release.textContent = 'Released on: '+film.release_date
   const rating = document.createElement('p')
   rating.textContent = film.vote_average+'/10'

   moreInfo.appendChild(title)
   moreInfo.appendChild(release)
   moreInfo.appendChild(overview)
   moreInfo.appendChild(rating)
}
