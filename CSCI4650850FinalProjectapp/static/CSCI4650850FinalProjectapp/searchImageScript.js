const access_key ="oWUHDZEGlN7f1DPv7hr36RWTEexfspkFQPsTGaIPLqI";

const form_el = document.querySelector("form");
const input_el = document.getElementById("search-input");
const searchResults_el = document.querySelector(".search-results");
const showMore_el = document.getElementById("show-more-button");

let inputData = "";
let page = 1;

async function searchImages(){
    inputData = input_el.value;
    const dynamicUrl = `https://api.unsplash.com/search/photos?page=${page}&query=${inputData}&client_id=${access_key}`;

    const response = await fetch(dynamicUrl);
    const data = await response.json();

    const results = data.results;

    if(page === 1)
{
    searchResults_el.innerHTML = "";
}
    results.map((result) => {
        const imageWrapper = document.createElement('div');
        imageWrapper.classList.add("search-result");
        const image = document.createElement('img');
        image.src = result.urls.small;
        image.alt = result.alt_description;
        const imageLink = document.createElement('a');
        imageLink.href = result.links.html;
        imageLink.target = "_blank";
        imageLink.textContent = result.alt_description;

        imageWrapper.appendChild(image);
        imageWrapper.appendChild(imageLink);
        searchResults_el.appendChild(imageWrapper);
    });

    page++;
    if(page > 1){
        showMore_el.style.display = "block";
    }
}

form_el.addEventListener("submit", (event) => {
    event.preventDefault();
    page = 1;
    searchImages();
})

showMore_el.addEventListener("click", () => {
    searchImages();
})