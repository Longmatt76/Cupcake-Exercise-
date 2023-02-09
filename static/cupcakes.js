const BASE_URL = "/api/cupcakes";

// generates the html markup using bootstrap for each cupcake
function generateHTML(cupcake) {
  return `<div class="col-4>"<div class="card" style="width: 18rem;">
  <img src="${cupcake.image}" class="card-img-top" width="400px" height="500px">
  <div class="card-body bg-secondary">
  <ul class="list-group list-group-flush">
    <li class="list-group-item bg-light">Flavor: ${cupcake.flavor}</li>
    <li class="list-group-item bg-light">Rating: ${cupcake.rating}</li>
    <li class="list-group-item bg-light">Size: ${cupcake.size}</li>
  </ul>
</div>
  </div>
  </div>
    `;
}
// pings the api requesting data on every cupcake
async function findCupcakes() {
  const res = await axios.get(BASE_URL);
  for (let cupcakeData of res.data.cupcakes) {
    console.log(cupcakeData)
    let newCupcake = $(generateHTML(cupcakeData));
    $("#cupcake_cards").append(newCupcake);
  }
};

// sends a post request to the api containing the data obtained from the form which then 
// uses that data to construct a new instance of cupcake class
async function addCupcake(){
  const flavor = $('#flavor').val();
  const size =  $('#size').val()
  const image =  $('#image').val()
  const rating =  $('#rating').val()

  let data = {'flavor':flavor, 'size': size,'image':image, 'rating':rating};
  const res = await axios.post(BASE_URL, data=data)
  console.log(res)

}
// event listener on the forms' button which calls the addcupcake function onclick
$('#butt').click(addCupcake)

$(findCupcakes);