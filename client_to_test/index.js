const button = document.getElementById("our-films")
const form = document.getElementById("find-film-form")
const filmsList = document.getElementById("list-films")

async function getFilms(e){
   e.preventDefault()
   const options = {
      method: 'GET',
      headers: { "Content-Type": "application/json" },
   } 
   const result = await fetch("http://127.0.0.1:5000/api/films", options);
   const data = await result.json()
   console.log(data)
   renderFilms(data)
}

button.addEventListener("click", getFilms)

form.addEventListener('submit', async (e) => {
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
})

async function deleteFilm(id){
   const options = {
      method: 'DELETE',
      headers: { "Content-Type": "application/json" }
   }
   const result = await fetch(`http://127.0.0.1:5000/api/films/${id}`, options);
   const data = await result.json()
   console.log(data)

}

function renderFilms(films) {
   filmsList.innerHTML=""

   films.map( film => {
      let li = document.createElement('li')
      li.textContent = film.name
      let deleteBttn = document.createElement("button")
      deleteBttn.onclick = function(){ deleteFilm(film.id) }
      deleteBttn.textContent = "X"
      li.appendChild(deleteBttn)
      filmsList.appendChild(li)
   })
}
